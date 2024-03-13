import random
import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS books (
                name TEXT,
                number_of_pages INTEGER,
                type TEXT,
                category TEXT
                )""")

book_names = [
    "Whispers of the Forgotten",
    "Echoes of Eternity",
    "Shadows of Destiny",
    "The Serpent's Whisper",
    "Echoes from the Abyss",
    "Forgotten Dreams",
    "Whispers of the Moonlight",
    "Secrets of the Silent Forest",
    "Echoes of the Lost Kingdom",
    "The Enigma of Elysium"
]

for i in range(10):
    name = book_names[i]
    number_of_pages = random.randint(100, 1000)
    cur.execute("INSERT INTO books (name, number_of_pages) VALUES (?, ?)", (name, number_of_pages))

conn.commit()

cur.execute("SELECT AVG(number_of_pages) FROM books")
average_pages = cur.fetchone()[0]
print("Average number of pages:", average_pages)

cur.execute("SELECT name FROM books WHERE number_of_pages = (SELECT MAX(number_of_pages) FROM books)")
max_pages_book = cur.fetchone()[0]
cur.execute("SELECT MAX(number_of_pages) FROM books")
max_number = cur.fetchone()[0]
print("Book with the maximum number of pages:", max_pages_book, "- number of pages: ", max_number)

conn.close()
