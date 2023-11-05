import csv
from operator import attrgetter


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # This could be converted to a date object if needed
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"Project: {self.name}, "
                f"Start Date: {self.start_date}, "
                f"Priority: {self.priority}, "
                f"Cost Estimate: ${self.cost_estimate:,.2f}, "
                f"Completion: {self.completion_percentage}%")

    def is_complete(self):
        return self.completion_percentage == 100


def load_projects_from_string(data):
    # Split the input data into lines and then process each line
    projects = []
    lines = data.strip().split('\n')
    for line in lines[1:]:  # Skip the header line
        parts = line.split('\t')  # Assuming the data is tab-separated
        projects.append(Project(*parts))
    return projects


def save_projects_to_csv(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.cost_estimate,
                             project.completion_percentage])


def main():
    data = """Name	Start Date	Priority	Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100"""

    projects = load_projects_from_string(data)

    # Display all projects
    print("All Projects:")
    for project in projects:
        print(project)

    # Sort by priority and display
    projects.sort(key=attrgetter('priority'))
    print("\nProjects sorted by priority:")
    for project in projects:
        print(project)

    # Save to CSV
    save_projects_to_csv('projects.csv', projects)
    print("\nProjects saved to projects.csv")


if __name__ == '__main__':
    main()
