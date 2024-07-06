import re

text = "Hello example@gmail.com example2@gmial.com"
pattern = r"(?P<username>\w+)@(?P<domain>\w+).(?P<top_level_domain>\w+)"

print(re.search(pattern, text).groupdict())