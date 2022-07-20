from bs4 import BeautifulSoup
import codecs


def readHTMLFile(path):
    f = codecs.open(path, 'r', encoding='utf8')
    return f.read()


def interpreterHTMLFile(file):
    tree = BeautifulSoup(file, 'html.parser')

    good_html = tree.prettify()

    return good_html


document = readHTMLFile('crawler/How the Provincial Nominee Program works.html')
print(interpreterHTMLFile(document))
