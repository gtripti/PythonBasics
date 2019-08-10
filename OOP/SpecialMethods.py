myList = [1,2,3,4]
len(myList)
print(myList)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages = pages
    # return string
    def __str__(self):
        return self.title + " by " + self.author
    # return length
    def __len__(self):
        return self.pages    

myBook = Book('Pyhton Rocks','Jose',200)
# print
print(myBook)
# length
len(myBook)
# delete an instance
del myBook
