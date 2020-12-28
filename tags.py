import random

with open('tags.txt', 'r') as f:
    lines = f.readlines()

# clean \n
lines = [l.strip() for l in lines]

# clean duplicates if any
lines = list(set(lines))

with open('tags.txt', 'w') as f:
    for line in lines:
        f.writeline(line)

# shuffle
random.shuffle(lines)
print(lines[:30])

lines_out = lines[:30]
lines_out = [l + ' ' for l in lines_out]

with open('tags_out.txt', 'w') as f:
    f.writelines(lines_out)
