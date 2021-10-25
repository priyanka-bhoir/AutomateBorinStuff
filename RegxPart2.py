import re

message = 'Call me 415-555-1011 tommorrow, or at 415-555-1234 for my office line.'

phoneNumeber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
m = phoneNumeber.search(message)

print(m.group())

m = phoneNumeber.findall(message)
print(m)
