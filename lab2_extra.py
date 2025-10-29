import csv

def finder(book_file):
    reader = csv.DictReader(book_file, delimiter=";")
    publishing = []
    for row in reader:
        if row["Publisher"] in publishing:
            continue
        else:
            publishing.append(row["Publisher"])
    return publishing

def populad_books(book_file):
    book_file.seek(0)
    reader = csv.DictReader(book_file, delimiter=";")
    books = []
    for row in reader:
        books.append((row["Book-Title"], row["Downloads"]))
    books.sort(key= lambda x: x[1], reverse=True)
    return books[:20]

with open("books-en.csv", encoding="latin-1") as book_file:
    print(*finder(book_file), sep=", ")
    print("\n20 The most popular books: \n")
    for i, (title, downloads) in enumerate(populad_books(book_file), 1):
        print(f"{i}. {title} - {downloads} downloads")

