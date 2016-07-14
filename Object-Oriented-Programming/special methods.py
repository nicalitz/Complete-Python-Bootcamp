# SPECIAL METHODS:
# Methods are not called directly but by special python syntax

class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):      #function is executed when an instance of the object is printed
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):      #function execute when then length of a book instance is queried
        return self.pages

    def __del__(self):      #function is executed when an instance of the object is deleted
        print "The {} book is destroyed".format(self.title)

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print book
print len(book)
del book