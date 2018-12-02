#!/usr/local/bin/python3

frequency = 0

with (open('input.txt')) as f:
    for line in f:
        line = line.strip()
        line = line.replace("+", "")
        
        value = int(line)
        frequency += value

print(frequency)
