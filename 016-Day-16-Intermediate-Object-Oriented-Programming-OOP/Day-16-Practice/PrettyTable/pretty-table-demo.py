from prettytable import PrettyTable, TableStyle  # note: no underscore
from prettytable.colortable import ColorTable, Themes

table = ColorTable()
# style = TableStyle('DOUBLE_BORDER')

pokemon_list = [["Pikachu", "Electric"], ["Squirtle", "Water"], ["Charmander", "Fire"]]

table.field_names = ["Pokemon Name", "Type"]
for pokemon in pokemon_list:
    table.add_row(pokemon)


table.align = "l"
table.set_style(TableStyle.DOUBLE_BORDER)  # or any other style
table.theme = Themes.LAVENDER
print(table)
