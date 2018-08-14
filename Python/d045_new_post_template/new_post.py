"""
    Creates a markdown file, after asking the user some basic questions, to create a new post
"""

import datetime
import textwrap

def create_new_post(title, date, category, authors, summary):
    if not date.strip():
        date = datetime.datetime.today().strftime("%Y-%m-%d")
    slug = slug = '-'.join(map(str.lower, title.split()))

    header = f"""
        Title: {title}
        Date: {date}
        Modified: {date}
        Category: {category}
        Slug: {slug}
        Authors: {authors}
        Summary: {summary}

        This is my blog post!

            #!python
            print("Enter your code here")
    """

    with open(f"{slug}.md","w") as f:
        f.write(textwrap.dedent(header))

def main():
    title = input("Enter a title for your article: ")
    date = input("Enter a date (YYYY-MM-DD) to use or leave blank to use current time: ")
    category = input("Enter a category for your article: ")
    authors = input("Enter the authors of this post, separated by commas: ")
    summary = input("Enter a summary for this article (short please!): ")

    create_new_post(title, date, category, authors, summary)

if __name__ == '__main__':
    main()