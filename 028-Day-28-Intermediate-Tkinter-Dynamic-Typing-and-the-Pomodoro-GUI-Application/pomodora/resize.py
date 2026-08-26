from PIL import Image


file = Image.open('./tomato.png')
file = file.resize((600,669))
file.save('./big_tomato.png')