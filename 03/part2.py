#!/usr/local/bin/python3

import re

pattern = re.compile("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)")

rows = columns = 1000

fabric = list()

for row in range(0, rows):
    rowList = list()
    for col in range(0, columns):
        rowList.append(list())
    fabric.append(rowList)

lines = list()
with open("input.txt", "r") as f:
    for line in f:
        m = re.match(pattern, line)
        lines.append({
            "id":int(m.group(1)),
            "x":int(m.group(2)),
            "y":int(m.group(3)),
            "w":int(m.group(4)),
            "h":int(m.group(5))})

overlaps = dict()

for line in lines:
    s = line["id"]
    x = line["x"]
    
    overlapping = False
    
    while x < line["x"] + line["w"]:
        y = line["y"]
        while y < line["y"] + line["h"]:
            fabric[x][y].append(line["id"])
            
            if (len(fabric[x][y]) > 1):
                overlapping = True
                for sd in fabric[x][y]:
                    overlaps[sd] = True
            
            y += 1
        x += 1
    
    overlaps[s] = overlapping

count = 0
for row in fabric:
    for col in row:
        if len(col) > 1:
            count += 1

print(count)

for s in overlaps:
    if not overlaps[s]:
        print(s)
