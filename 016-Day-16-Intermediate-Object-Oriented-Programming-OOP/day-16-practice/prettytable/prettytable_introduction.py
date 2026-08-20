#!/usr/bin/env python3
"""
prettytable-introduction.py
Comprehensive demo of PrettyTable & ColorTable.
Automatically disables colours when output is not a terminal (e.g., redirected to file).
"""

import sys
from prettytable import PrettyTable, TableStyle
from prettytable.colortable import ColorTable, Themes

# ---------- Detect if we are in a terminal that supports colour ----------
USE_COLOR = sys.stdout.isatty()

def print_separator(title):
    print("\n" + "=" * 70)
    print(f"   {title}")
    print("=" * 70 + "\n")

# ---------- Sample data ----------
pokemon_data = [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
    ["Bulbasaur", "Grass/Poison"],
    ["Jigglypuff", "Normal/Fairy"],
    ["Meowth", "Normal"],
    ["Psyduck", "Water"],
    ["Growlithe", "Fire"],
    ["Machop", "Fighting"],
    ["Geodude", "Rock/Ground"],
]
field_names = ["Pokemon Name", "Type"]

# ---------- Theme name mapping (human readable) ----------
theme_names = {
    Themes.DEFAULT: "DEFAULT",
    Themes.DYSLEXIA_FRIENDLY: "DYSLEXIA_FRIENDLY",
    Themes.EARTH: "EARTH",
    Themes.GLARE_REDUCTION: "GLARE_REDUCTION",
    Themes.HIGH_CONTRAST: "HIGH_CONTRAST",
    Themes.LAVENDER: "LAVENDER",
    Themes.OCEAN: "OCEAN",
    Themes.OCEAN_DEEP: "OCEAN_DEEP",
    Themes.PASTEL: "PASTEL",
}

# ---------- 1. Basic PrettyTable ----------
print_separator("1. BASIC PRETTYTABLE (DEFAULT STYLE)")
table = PrettyTable()
table.field_names = field_names
for row in pokemon_data:
    table.add_row(row)
print(table)

# ---------- 2. Alignment ----------
print_separator("2. ALIGNMENT: LEFT, CENTER, RIGHT")
table_align = PrettyTable()
table_align.field_names = field_names
for row in pokemon_data:
    table_align.add_row(row)

table_align.align["Pokemon Name"] = "l"
table_align.align["Type"] = "r"
print("Left for Name, Right for Type:")
print(table_align)

table_align.align["Pokemon Name"] = "c"
table_align.align["Type"] = "c"
print("\nBoth columns centered:")
print(table_align)

# ---------- 3. Border Styles ----------
print_separator("3. BORDER STYLES (TableStyle)")
styles = [
    TableStyle.DEFAULT,
    TableStyle.SINGLE_BORDER,
    TableStyle.DOUBLE_BORDER,
    TableStyle.ORGMODE,
    TableStyle.MARKDOWN,
    TableStyle.PLAIN_COLUMNS,
    TableStyle.MSWORD_FRIENDLY,
    TableStyle.RANDOM,
]

for style in styles:
    t = PrettyTable()
    t.field_names = field_names
    for row in pokemon_data[:5]:
        t.add_row(row)
    t.set_style(style)
    print(f"Style: {style.name}")
    print(t)
    print("-" * 50)

# ---------- 4. Sorting ----------
print_separator("4. SORTING BY A COLUMN")
table_sort = PrettyTable()
table_sort.field_names = field_names
for row in pokemon_data:
    table_sort.add_row(row)

table_sort.sortby = "Pokemon Name"
print("Sorted by Pokemon Name (A-Z):")
print(table_sort)

table_sort.sortby = "Type"
print("\nSorted by Type (A-Z):")
print(table_sort)

# ---------- 5. Title & Horizontal Rules ----------
print_separator("5. TITLE & HORIZONTAL RULES")
table_title = PrettyTable()
table_title.field_names = field_names
for row in pokemon_data[:6]:
    table_title.add_row(row)
table_title.title = "My Pokemon Collection"
table_title.hrules = 1
print("With title and frame rules:")
print(table_title)

table_div = PrettyTable()
table_div.field_names = field_names
for idx, row in enumerate(pokemon_data[:6]):
    if idx == 1:                     # divider after second row
        table_div.add_row(row, divider=True)
    else:
        table_div.add_row(row)
print("\nWith a manual divider after the second row:")
print(table_div)

# ---------- 6. ColorTable: Built‑in Themes ----------
print_separator("6. COLORTABLE – BUILT‑IN THEMES")
themes = [
    Themes.DEFAULT,
    Themes.DYSLEXIA_FRIENDLY,
    Themes.EARTH,
    Themes.GLARE_REDUCTION,
    Themes.HIGH_CONTRAST,
    Themes.LAVENDER,
    Themes.OCEAN,
    Themes.OCEAN_DEEP,
    Themes.PASTEL,
]

if USE_COLOR:
    for theme in themes:
        ct = ColorTable()
        ct.field_names = field_names
        for row in pokemon_data[:5]:
            ct.add_row(row)
        ct.set_style(TableStyle.DOUBLE_BORDER)
        ct.theme = theme
        # Print human‑readable theme name
        theme_name = theme_names.get(theme, "Unknown")
        print(f"Theme: {theme_name}")
        print(ct)
        print("-" * 50)
else:
    print("Colour themes are only visible in a terminal.")
    print("Here are the same tables in plain text (PrettyTable with DOUBLE_BORDER style):")
    for theme in themes:
        t = PrettyTable()
        t.field_names = field_names
        for row in pokemon_data[:5]:
            t.add_row(row)
        t.set_style(TableStyle.DOUBLE_BORDER)
        print(f"Theme would be: {theme_names.get(theme, 'Unknown')}")
        print(t)
        print("-" * 50)

# ---------- 7. ColorTable: Manual Colour Customisation ----------
print_separator("7. COLORTABLE – MANUAL COLOUR CUSTOMISATION")

if USE_COLOR:
    manual_table = ColorTable()
    manual_table.field_names = field_names
    for row in pokemon_data[:5]:
        manual_table.add_row(row)

    manual_table.header_color = "yellow"
    manual_table.border_color = "magenta"
    manual_table.row_colors = ["green", "blue", "red", "cyan", "white"]
    print("Custom colors: yellow header, magenta borders, alternating row colours:")
    print(manual_table)

    # Row background colours
    manual_bg = ColorTable()
    manual_bg.field_names = field_names
    for row in pokemon_data[:5]:
        manual_bg.add_row(row)

    manual_bg.header_color = "cyan"
    manual_bg.border_color = "blue"
    manual_bg.row_colors = ["white", "black"]
    manual_bg.row_styles = ["on_blue", "on_white"]
    print("\nWith row background colours (blue/white backgrounds):")
    print(manual_bg)
else:
    print("Manual colour customisation requires a terminal. Use --color=always if needed.")
    print("Here is a plain example with DOUBLE_BORDER style:")
    t = PrettyTable()
    t.field_names = field_names
    for row in pokemon_data[:5]:
        t.add_row(row)
    t.set_style(TableStyle.DOUBLE_BORDER)
    print(t)

# ---------- 8. Combining style + theme ----------
print_separator("8. COLORTABLE WITH CUSTOM BORDER STYLE AND THEME")
if USE_COLOR:
    ct_combined = ColorTable()
    ct_combined.field_names = field_names
    for row in pokemon_data[:6]:
        ct_combined.add_row(row)
    ct_combined.set_style(TableStyle.MARKDOWN)
    ct_combined.theme = Themes.OCEAN_DEEP
    print("Markdown border style + OCEAN_DEEP theme:")
    print(ct_combined)
else:
    t = PrettyTable()
    t.field_names = field_names
    for row in pokemon_data[:6]:
        t.add_row(row)
    t.set_style(TableStyle.MARKDOWN)
    print("Markdown border style (no colours):")
    print(t)

# ---------- 9. Export formats ----------
print_separator("9. EXPORT TO DIFFERENT TEXT FORMATS")
export_table = PrettyTable()
export_table.field_names = field_names
for row in pokemon_data[:4]:
    export_table.add_row(row)

print("HTML format:")
print(export_table.get_html_string())

print("\nJSON format (as list of dicts):")
print(export_table.get_json_string())

print("\nCSV format (comma separated):")
print(export_table.get_csv_string())

# ---------- 10. Bonus: random style + random theme ----------
print_separator("10. BONUS: RANDOM STYLE + RANDOM COLOURS")
import random
if USE_COLOR:
    random_table = ColorTable()
    random_table.field_names = field_names
    for row in pokemon_data:
        random_table.add_row(row)
    random_table.set_style(TableStyle.RANDOM)
    random_table.theme = random.choice(themes)
    print("Random border style and a random theme:")
    print(random_table)
else:
    random_table = PrettyTable()
    random_table.field_names = field_names
    for row in pokemon_data:
        random_table.add_row(row)
    random_table.set_style(TableStyle.RANDOM)
    print("Random border style (no colours):")
    print(random_table)

print("\n" + "=" * 70)
print("   End of PrettyTable & ColorTable demonstration")
print("=" * 70)