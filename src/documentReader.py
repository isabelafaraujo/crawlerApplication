from bs4 import BeautifulSoup
import codecs

teste = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


def readHTMLFile(path):
    f = codecs.open(path, 'r', encoding='utf8')
    return f.read()


def interpreterHTMLFile(file, path):
    complete_path = path + '.parser'

    tree = BeautifulSoup(file, complete_path)

    good_html = tree.prettify()

    print(good_html)


document = readHTMLFile('crawler/How the Provincial Nominee Program works.html')
relative_path = 'html'
interpreterHTMLFile(document, relative_path)