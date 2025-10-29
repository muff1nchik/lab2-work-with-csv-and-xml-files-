import csv
import random


INPUT_FILE = "books-en.csv"
OUTPUT_FILE = "result.txt"
QUANTITY = 20


def dict_maker(file):
    with open(file, encoding="latin-1") as book_file:
        reader = csv.DictReader(book_file, delimiter=";")
        dictionary = [row for row in reader]
    return dictionary


def str_maker(dictionary):
    author = dictionary["Book-Author"].strip()
    title = dictionary["Book-Title"].strip()
    year = dictionary["Year-Of-Publication"].strip()
    return f"{author}. {title} - {year}"


def saver(reference, path):
    with open(path, "w", encoding="utf-8") as file:
        for i, ref in enumerate(reference, 1):
            file.write(f"{i} {ref}\n")

    
books = dict_maker(INPUT_FILE)
select = random.sample(books, QUANTITY)
reference = [str_maker(row) for row in select]
saver(reference, OUTPUT_FILE)