from PIL import Image

file = Image.open("./logo.png")
file = file.resize((600, 567))
file.save("./big_logo.png")
