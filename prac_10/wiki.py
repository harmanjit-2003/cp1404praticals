# wiki.py

import wikipedia

def search_wikipedia():
    while True:
        title = input("Enter a page title or search phrase (or press enter to quit): ")
        if not title:
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"Title: {page.title}\nSummary: {page.summary}\nURL: {page.url}")
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation error. Please be more specific or choose one of the following options:\n{e.options}")
        except wikipedia.PageError:
            print("Page not found. Please try a different search term.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_wikipedia()
