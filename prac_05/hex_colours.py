# Define a dictionary of color names and their corresponding hex codes
COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUAMARINE": "#7FFFD4",
    "BLUEVIOLET": "#8A2BE2",
    "CORAL": "#FF6F61",
    "DARKORCHID": "#9932CC",
    "GOLD": "#FFD700",
    "HOTPINK": "#FF69B4",
    "LIGHTSEAGREEN": "#20B2AA",
    "MIDNIGHTBLUE": "#191970",
}

while True:
    color_name = input("Enter a color name (or blank to exit): ").upper()  # Convert input to uppercase
    if color_name == "":
        break  # Exit the loop when Enter is pressed

    # Look up the color code using the dictionary and handle invalid color names
    color_code = COLORS.get(color_name, "Invalid color name")
    print(f"{color_name}: {color_code}")
