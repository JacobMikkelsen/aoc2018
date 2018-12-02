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

with (open('input.txt', 'r')) as f:
    lines = f.readlines()

counts = dict()

doubles = list()
triples = list()

for line in lines:
    (double, triple) = doubles_and_triple(line)
    if double:
        doubles.append(line)
    if triple:
        triples.append(line)
    # print(double, triple)

print(len(doubles) * len(triples))
