import requests
import re


class ProcessingFile:

    def __init__(self, url):
        self.url = url

    """
    Downloads the text file from the provided URL.

    Returns:
        str or None: The content of the downloaded file as text, or None if an error occurs.
    """
    def download_file(self):
        try:
            response = requests.get(self.url)
            # Raise an exception for unsuccessful HTTP status codes.
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print("An error occurred while downloading the text file:", e)
            return None

    """
    Processes the content of the text file to extract coordinates and image dimensions.

    Args:
        text (str): The content of the text file to process.

    Returns:
        tuple: A tuple containing the width, height, and coordinates extracted from the text file.
    """
    def process_file(self, text):
        coordinates = []
        width, height = None, None

        # Splitting the text into lines.
        lines = text.split('\n')

        # Ignoring comments and empty lines.
        for line in lines:
            if line.startswith('#') or not line.strip():
                continue

            if 'Rozmer obrazku' in line:
                # Extracting image dimensions.
                dimensions = re.findall(r'\d+', line)
                width = int(dimensions[0])
                height = int(dimensions[1])
                continue

            # Extracting coordinates.
            coords = re.findall(r'([+-]?\d*\.\d+|[+-]?\d+)', line)
            formatted_coords = []
            for val in coords:
                x = float(val)
                formatted_coords.append((x, None))
            coordinates.extend(formatted_coords)

        for i in range(len(coordinates)):
            x, y = coordinates[i]
            if y is None:
                if x < 0:
                    coordinates[i] = (x, height)
                else:
                    coordinates[i] = (x, 0)

        return width, height, coordinates
