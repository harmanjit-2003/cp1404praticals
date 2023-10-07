def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            code, lecturer, students = parts
            students = int(students)
            data.append([code, lecturer, students])
    return data

def display_subject_details(data):
    for subject in data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

def main():
    filename = "subject_data.txt"
    data = get_data(filename)
    display_subject_details(data)

if __name__ == "__main__":
    main()
