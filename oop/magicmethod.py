class Book:
    def __init__(self, title, author,num_page):
        self.title = title
        self.author = author
        self.num_page = num_page


    def __str__(self):
        return f" '{self.title}' by {self.author} "
    

    def __eq__(self, other): # nhung ham dc xay dung san
        return self.title == other.title and self.author == other.author
        
book1 = Book('The Godfather', 'Mario Puzo', 300)
book2 = Book('The Godfather', 'Mario Puzo', 500)




print(book1.__str__())

print(book1 == book2)

