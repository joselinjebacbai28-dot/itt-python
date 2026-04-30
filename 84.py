from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
   
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

  
    def handle_data(self, data):
        # The task says: do not print if data is just a newline
        if data != '\n':
            print(">>> Data")
            print(data)


n = int(input())
html_string = ""
for _ in range(n):
    html_string += input().rstrip() + '\'
parser = MyHTMLParser()
parser.feed(html_string)
parser.close()
