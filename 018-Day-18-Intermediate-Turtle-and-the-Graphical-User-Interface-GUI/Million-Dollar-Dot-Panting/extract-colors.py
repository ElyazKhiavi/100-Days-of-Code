import colorgram



rgb_list = []
colors = colorgram.extract("./Million-Dollar-Dot-Panting/Damien_Hirsts_Spot_Paintings.png", 12)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r,g,b))


print(colors)
print(rgb_list)

