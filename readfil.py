fhand = open('nfile.txt')
count = 0
for line in fhand:
  count = count + 1
print('Line Count:', count)
#1
fhand = open('nfile.txt')
inp = fhand.read()
print(len(inp))
#11
