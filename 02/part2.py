#!/usr/local/bin/python3

def doubles_and_triple (s):
    
    counts = dict()
    
    # print(s)
    for letter in s:
        # print(letter)
        counts[letter] = 1 if letter not in counts else counts[letter] + 1
    
    double = False
    triple = False
    
    for count in counts.values():
        if count == 2:
            double = True
        if count == 3:
            triple = True
    
    return (double, triple)

def string_diff (a, b):
    difference = 0
    
    for i in range(0,len(a)):
        if a[i] != b[i]:
            difference += 1
    
    return difference

lines = []

with (open('input.txt', 'r')) as f:
    for line in f:
        lines.append(line.strip())

counts = dict()

doubles = list()
triples = list()

for line in lines:
    (double, triple) = doubles_and_triple(line)
    if double:
        doubles.append(line)
    elif triple:
        triples.append(line)

ids = doubles.copy()
ids.extend(triples)

for a in ids:
    for b in ids:
        d = string_diff(a, b)
        if (d == 1):
            print(a, b)
