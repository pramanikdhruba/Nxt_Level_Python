# Magic/Dunder Methods
#   1.Create a class Book with attributes title and author .
#       i.Implement __str__() so that printing the object displays "Title by Author" .
#       ii.Implement __len__() so that len(book) returns the length of the title.
#   2.Create two Book objects and test these methods

# 1. Create a class Book
class Book:
    """Represents a book with title and author.""" 
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # 1.1 Implement __str__()
    def __str__(self):
        """Returns 'Title by Author'.""" 
        return f"{self.title} by {self.author}"

    # 1.2 Implement __len__()
    def __len__(self):
        """Returns the length of the title."""
        return len(self.title)

# 2. Create two Book objects and test
print("--- Testing Magic/Dunder Methods ---")
book1 = Book("1984", "George Orwell") 
book2 = Book("Dune", "Frank Herbert") 

# Test __str__()
print(f"Book 1 str: {book1}") 
print(f"Book 2 str: {book2}") 

# Test __len__()
print(f"Length of Book 1's title: {len(book1)}") 
print(f"Length of Book 2's title: {len(book2)}") 