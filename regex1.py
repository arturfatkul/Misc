import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{3}')
mo = phoneNumRegex.search('My number is 415-453-323.')
print('Phone number found: ' + mo.group())
