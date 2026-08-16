# Word Counter Program

try:
    with open("article.txt", "r") as file:
        content = file.read()

    words = len(content.split())
    lines = len(content.splitlines())
    characters = len(content)

    print("Number of Words:", words)
    print("Number of Lines:", lines)
    print("Number of Characters:", characters)

except FileNotFoundError:
    print("article.txt file not found.")