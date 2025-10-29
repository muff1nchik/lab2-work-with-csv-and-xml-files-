import csv


def count_lines(book_file):
    counter = 0
    reader = csv.DictReader(book_file, delimiter=';')
    for row in reader:
        if len(row["Book-Title"]) > 30:
            counter +=1
    return counter


with open("books-en.csv", encoding="latin-1") as book_file:
    print(count_lines(book_file))

    