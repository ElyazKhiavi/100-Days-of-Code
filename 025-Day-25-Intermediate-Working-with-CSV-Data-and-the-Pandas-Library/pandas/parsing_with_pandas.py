import pandas as pd

data = pd.read_csv("./weather_data.csv")


# # DataFrame
# # data_dict = data.to_dict()
# # print(data_dict)

# # Series
# data_list = data["temp"].to_list()
# print(data_list)


# # Manually
# # data_list = data['Temp'].to_list()
# # average  = round(sum(data_list)/len(data_list),2)


# # Pandas Method
# average = data["temp"].mean()
# print(f"Average Temp This Week: {average:.2f}")

# max = data["temp"].max()
# print(f"Max Temp This Week: {max:.2f}")


# ## Same!
# print(data["condition"])
# print(data.condition)


# # Getting Rows

# print(data[data.day == "Saturday"])

# ### Getting the row that had the max tem

# print(data[data.temp == data.temp.max()])

# ### Getting data from the selected row

# day = data[data.day == "Saturday"]
# print(day.condition)


def c_to_f(temp):
    """Formula (0°C × 9/5) + 32 = 32°F"""
    return (temp * 9 / 5) + 32


monday = data[data.day == "Monday"]
# print(monday.temp[2]) # !!!!
print(c_to_f(monday.temp.item()))
