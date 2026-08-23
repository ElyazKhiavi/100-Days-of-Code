import pandas as pd

data = pd.read_csv("./squirrel_data.csv")
squirrel_count = {'color':[],'count':[]}
fur_color_list = data["Primary Fur Color"].to_list()
for squirrel in fur_color_list:
    if squirrel in squirrel_count["color"]:
        squirrel_count["count"][squirrel_count['color'].index(squirrel)] += 1
    else:
        squirrel_count['color'].append(squirrel)
        squirrel_count['count'].append(1)


new_data = pd.DataFrame(squirrel_count)
new_data.to_csv('squirrel_count.csv')