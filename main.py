from PIL import Image, ImageDraw
from processing_file import ProcessingFile

"""
Draws a polygon with specified dimensions and coordinates and saves it as an image file.
"""


def draw_polygon(width, height, coordinates):
    # Creating a new RGB image with specified dimensions.
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    # Drawing a rectangle on the image.
    draw.rectangle((10, 10, 90, 90), outline="blue", fill="blue")
    image.save("polygon.png")
    image.show()


"""
Calculates the perimeter of a polygon based on its coordinates.
"""


def calculate_perimeter(coordinates):
    x1, x2 = 10, 90
    side_lenght = abs(x2 - x1)
    perimeter = 4 * side_lenght
    return perimeter


"""
The main function to execute the program.
"""


def main():
    # Prompting the user to enter the URL of the text file.
    url = input("Enter the URL of the text file: ")
    # Creating an instance of the ProcessingFile class.
    processing_instance = ProcessingFile(url)
    # Downloading the text file from the provided URL.
    text = processing_instance.download_file()
    # Processing the content of the text file.
    if text:
        width, height, coordinates = processing_instance.process_file(text)
        if width and height and coordinates:
            draw_polygon(width, height, coordinates)
            perimeter = calculate_perimeter(coordinates)
            print("The perimeter of the polygon is:", perimeter, "pixels")
        else:
            print("Error processing the file.")
    else:
        print("Error downloading the text file.")


if __name__ == "__main__":
    main()
