from PIL import Image

ascii_chars = ["@ ", "# ", "S ", "% ", "? ", "* ", "+ ", "; ", ": ", ", ", ". "]

with Image.open("Donut.jpg") as image:

    X, Y = image.size
    image = image.convert("L")
    
    output = ""

    for y in range(Y):
        for x in range(X):
            brightness = image.getpixel((x, y))
            output += ascii_chars[int(brightness / 25)]
        output += "\n"

with open("ascii_image.txt", "w") as file:
    file.write(output)