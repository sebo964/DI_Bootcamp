# Instructions :

# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems()
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)

# p.getVisibleItems()
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

alphabetlist = "abcdefghijklmnopqrstuvwxyz"

alphabetlist = [*alphabetlist]

Pagination_size = 4

the_current_page_is = 0


class Pagination:
    def __init__(self, alphabetlist, Pagination_size):
        self.alphabetlist = alphabetlist
        self.Pagination_size = Pagination_size
        self.totalPages = len(alphabetlist) / Pagination_size
        self.currentPage = 1

    def getVisibleItems(self):
        return self.alphabetlist[0 : self.Pagination_size]

    def nextPage(self):
        if self.currentPage >= self.totalPages:
            return print("You are on the last page")
        self.currentPage += 1
        return self

    def prevPage(self):
        if self.currentPage <= 1:
            return print("You are on the first page")
        self.currentPage -= 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        self.currentPage = pageNum
        return self
