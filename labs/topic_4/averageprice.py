from lab_requests import readbooks

#notworking

books = readbooks()
total = 0
count = 0

for book in books:
    print(book)
