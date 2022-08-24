#DATA STRUCTURE - STACK IMPLEMENTATION
# ENTRY AND EXIT FROM ONE SIDE ONLY


class WebPage:

    def __init__(self, title, domain, url):
        self.title = title
        self.domain = domain
        self.url = url
        self.next_page = None
        self.previous_page = None

    def show(self):
        print("===========")
        print(self.title, self.domain, self.url)
        print("===========")

class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Stack created")

    def push(self, page):
        self.size += 1
        if self.head is None:
            self.head = page
            self.tail = page
        else:
            self.tail.next_page = page
            page.previous_page = self.tail
            self.tail = page

    def pop(self):
        self.size -= 1
        temp = self.tail
        self.tail = self.tail.previous_page
        self.tail.next_page = None
        del temp

    def peek(self, option=1):
        if option == 1:
            return self.tail
        else:
            return self.head

    def iterate(self):
        temp = self.tail
        while True:
            temp.show()
            temp = temp.previous_page

            if temp.previous_page is None:
                temp.show()
                break


stack = Stack()

stack.push(WebPage(title="helo", domain="hi", url="nahhh"))
stack.push(WebPage(title="whats", domain="nooos", url="yoo"))
stack.push(WebPage(title="kcsks", domain="hijjjj", url="cdc"))

stack.pop()
stack.peek().show()
stack.iterate()

