text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text=text.strip().lower()
# print(text)
text =text.replace('!','.')
# print(text)
a = text.split('.')
for i in range(len(a)):
    a[i] = a[i].strip()
    if a[i]=='': a.remove(a[i])
print(a)
first = a[0].split()
print(first)
print(text.count('python'))
start = a[0].startswith("python")
end = a[0].endswith("language")
print(start, end)
print(len(text), text.count('a'), text.find("data"))
words = text.replace('.','').replace(',','').split()
print(words)
newText = ''
for i in words:
    newText += i + '-'
newText=newText[:-1]
d = {}
for i in newText.split('-'):
    if i not in d:
        d[i] = newText.count(i)
print(d)

def clean(text):
    return text.replace('.','').replace(',','').replace('!','').replace('?','').lower().strip()
print(clean('   Hello, World,      '))
