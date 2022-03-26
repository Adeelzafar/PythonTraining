fhand = open('nfile.txt')
count = 0
for line in fhand:
  if line.startswith('h'):
    print(line)
#hello world
