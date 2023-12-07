# List of colour variables with their names
import sys
sys.path.append("/home/rj/brand_colours/")
from brand_colours.brand_colours import *

blues = {var: value for var, value in globals().items() if var.startswith('blue')}
yellows = {var: value for var, value in globals().items() if var.startswith('yellow')}
greys = {var: value for var, value in globals().items() if var.startswith('grey')}
lightblues = {var: value for var, value in globals().items() if var.startswith('lightblue')}
teals = {var: value for var, value in globals().items() if var.startswith('teal')}

all_colours = blues | yellows | greys | lightblues | teals

# Create a string to store all the HTML blocks
html_blocks = ""

# for col_name in all_colours.keys():
# print(col_name, all_colours[col_name], all_colours[col_name].hex())

# Loop through the colour data and generate HTML for each colour
for i, col_name in enumerate(all_colours.keys(), start=1):
    html_block = f"""
    <div class="color-box" style="background-color: {all_colours[col_name].hex()}">
        {col_name}
    </div>
    """
    html_blocks += html_block

    # add line break every 6 boxes
    if i % 6 == 0:
        html_blocks += "<br>"

# Create a complete HTML page with a grid of colour boxes
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .color-box {{
            width: 100px;
            height: 100px;
            text-align: center;
            line-height: 100px;
            font-size: 18px;
            font-family: monospace;
            color: white;
            display: inline-block;
            margin: 5px;
        }}
    </style>
</head>
<body>
    {html_blocks}
</body>
</html>
"""

# Save the HTML to a file or display it
with open("colour_box_grid.html", "w") as file:
    file.write(html_template)


