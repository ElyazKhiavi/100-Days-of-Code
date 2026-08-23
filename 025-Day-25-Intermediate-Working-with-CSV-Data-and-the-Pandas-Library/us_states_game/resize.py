from PIL import Image

# 1. Resize your GIF to the exact pixel size you want (e.g., 500x500)
img = Image.open('./blank_states_img.gif')
img = img.resize((2175,1473))   # change these numbers to whatever you need
img.save('./big_blank_states_img.gif')

