string = input("Enter the value: ")
import collections
results = collections.Counter(string)
for k,v in results.items():
    print(k,v,sep='', end='')
