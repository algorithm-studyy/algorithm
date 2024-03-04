import re
print(re.search('abc', 'abcdef'))  # <re.Match object; span=(0, 3), match='abc'>
print(re.search('abc', 'abcdefabc'))  # <re.Match object; span=(0, 3), match='abc'>
print(re.search('abc', 'ababcdefabc'))