class Author:
    def __init__(self, name): #initialize object
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No published books' #if no books, says 'No published books'
        return f'Author name: {self.name}. Published books: {book_list}'


wendy = Author('Wendy Dendy')
wendy.publish('The Third Book')

print(wendy)
