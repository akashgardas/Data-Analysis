class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book_id, title):
        self.books[book_id] = title
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
    
    def search_book(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
        else:
            return None
    
    def update_title(self, book_id, title):
        if book_id in self.books:
            self.books[book_id] = title 

    def display_books(self):
        print('Book\tTitle')
        print('-'*30)
        for book, title in self.books.items():
            print(f'{book}\t{title}')
    
    def count_books(self):
        return len(self.books) 
    
    def search_book_by_title(self, title):
        return self.books.containsValue(title)

# Testing   
# Sample Library Data
data = {
    101: "The Great Gatsby",
    102: "To Kill a Mockingbird",
    103: "1984",
    104: "Pride and Prejudice",
    105: "The Catcher in the Rye",
    106: "The Lord of the Rings",
    107: "Harry Potter and the Sorcerer's Stone",
    108: "The Hobbit",
    109: "Moby Dick",
    110: "War and Peace"
}

library = Library()

for book, title in data.items():
    library.add_book(book, title)

library.display_books()

library.remove_book(103)

print(library.search_book(102))

library.display_books()