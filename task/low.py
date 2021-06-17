s  = input('Enter the value: ')
import re
d = min(re.findall('\d+', s))
e = s.replace(d, "MIN")
print(e)
