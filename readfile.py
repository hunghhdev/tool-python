num_lines = sum(1 for line in open('demofile2.txt'))
print(num_lines)

with open('demofile2.txt') as foo:
    num_lines = len(foo.readlines())

print(num_lines)
