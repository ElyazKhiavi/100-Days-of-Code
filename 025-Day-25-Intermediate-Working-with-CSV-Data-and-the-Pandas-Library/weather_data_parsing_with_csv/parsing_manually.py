# Weather
# parsing_csv_manually

with open("./weather_data.csv", "r") as f:
    lines = []

    for line in [line.replace("\n", "").split(",") for line in f.readlines()]:
        new_day = {}
        new_day["day"] = line[0]
        new_day["temp(c)"] = line[1]
        new_day["condition"] = line[2]
        lines.append(new_day)


print(lines)
