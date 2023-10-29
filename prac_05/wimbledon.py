def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            year, champion, country, runner_up, _, _ = parts
            data.append((year, champion, country))
    return data

def find_champions(data):
    champions = {}
    for _, champion, _ in data:
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions

def find_countries(data):
    countries = set()
    for _, _, country in data:
        countries.add(country)
    return countries

def main():
    data = read_data("wimbledon_champions.csv")
    champions = find_champions(data)
    countries = find_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    sorted_countries = sorted(countries)
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(sorted_countries)
    print(countries_str)

if __name__ == "__main":
    main()
