import pyperclip
import re
text = pyperclip.paste()
words = re.findall("\w", text)
count = {}
for i in words:
    count[i] = count.get(i, 0)+1
print(count)

