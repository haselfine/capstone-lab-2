class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if self.books.__contains__(title): #searches list for identical items
            print(f'The list of published books already contains "{title}"')
        else:
            self.books.append(title)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No published books'
        return f'Author name: {self.name}. Published books: {book_list}'


wendy = Author('Wendy Dendy')
wendy.publish('The Third Book')

print(wendy)

wendy.publish('The Third Book')