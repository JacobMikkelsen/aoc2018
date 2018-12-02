#!/usr/local/bin/python3

frequencies = dict()
frequency = 0
lines = []

with (open('input.txt')) as f:
    lines = f.readlines()

i = 0
length = len(lines)

while True:
    value = int(lines[i])
    frequency += value
    
    if (frequency in frequencies):
        print(frequency)
        break;
    
    frequencies[frequency] = True
    
    i = (i + 1) % length

