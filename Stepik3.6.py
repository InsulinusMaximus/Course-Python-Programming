#1
'''
import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/237.txt'.strip())
str = r.text
count = 0
for i in str.splitlines():
    count+=1

print(count)
'''
#2
'''
import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
count = 0
while True:
    if not r.text.startswith('We'):
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
        count += 1
        continue
    else:
        print(r.text)
        print(count)
        break
'''

