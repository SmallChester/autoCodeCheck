import csv
import urllib.request
from bs4 import BeautifulSoup

"""
according to html's lineNum --- res code
read file find similar function report the line



确定函数名称
确定错误行号  找到对应错误代码的行号 错误代码 对应在函数名称下面的多少行
"""

# Python program to convert a list
# to string using join() function

# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = "\n"
    # return string
    return (str1.join(s))


def find_function():
    pass

def visitUrl(url):
    resp = urllib.request.urlopen(url)
    htmls = resp.read().decode("utf-8")
    return htmls

def saveHtml(file_name, file_text):
    with open(file_name.replace('/', '_') + '.html', 'w', encoding='utf-8') as f:
        f.write(file_text)

def visitHtmlFile(urlname):
    with open(urlname.replace('/', '_'), 'r', encoding='utf-8') as f:
        htmlpage=f.readlines()
        # Driver code
        # s = ['Geeks', 'for', 'Geeks']
        htmlpage=listToString(htmlpage)
        return htmlpage

with open('bug reports - numpy-f2py.csv','r',encoding='utf-8') as f:
    row = csv.DictReader(f, delimiter = ',')
    # titles=next(row)
    # print(titles)
    """
    ,function,line,length,url,file,s_function,s_line,status,error type
    """
    for line in row:
        print(line['file'])
        print(line['function'])
        print(line)
        funcname=line['function']
        url=line['url']
        htmlpage = visitHtmlFile(url)
        """ 
        # get html from url
        htmlpage=visitUrl(url)
        saveHtml(url,htmlpage)
        print(htmlpage)
        """
        soup=BeautifulSoup(htmlpage,'html.parser')
        print(soup)

        pass
        """http:__192.168.5.61:20000_report-c53a24.html#EndPath.html"""