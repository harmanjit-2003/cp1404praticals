

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year,Pointer Arithmetic
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()
        # All other lines are language data
        for line in in_file:
            parts = line.strip().split(',')
            # Reflection and Pointer Arithmetic are stored as strings (Yes/No) and we want a Boolean
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"  # Updated for Pointer Arithmetic
            # Construct a ProgrammingLanguage object using the elements
            # year should be an int
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            # Add the language we've just constructed to the list
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip the header line
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            reflection = row[2] == "Yes"
            pointer_arithmetic = row[4] == "Yes"  # Updated for Pointer Arithmetic
            language = ProgrammingLanguage(row[0], row[1], reflection, int(row[3]), pointer_arithmetic)
            print(language)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        # Add 'pointer_arithmetic' to the named tuple definition
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            language = Language._make(row)
            print(language)


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    with open("languages.csv", "r", newline='') as in_file:
        in_file.readline()  # Skip the header line
        # Add 'pointer_arithmetic' to the named tuple definition
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(language)


# Uncomment the function you want to run
# main()
# using_csv()
# using_namedtuple()
# using_csv_namedtuple()

