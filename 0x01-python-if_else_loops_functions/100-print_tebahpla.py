#!/usr/bin/python3
x = 0
for i in reversed(range(97, 123)):
    print('{:c}'.format(i - x), end='')
    if x == 0:
        x = 32
    else:
        x = 0
