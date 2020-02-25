from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = 44827 #on second run, change num = 2
pattern = re.compile("and the next nothing is (\d+)")
while True:
    content = urlopen(uri%num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)
