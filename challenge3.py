import pyperclip
import re
text = pyperclip.paste()
word = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text)
print(''.join(word))
