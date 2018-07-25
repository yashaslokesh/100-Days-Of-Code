import webbrowser

def search():
    search_query = input("Enter your query to search YouTube: ")
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open_new_tab(url)

if __name__=="__main__":
    search()