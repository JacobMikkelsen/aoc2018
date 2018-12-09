#!/usr/local/bin/python3

import re
from datetime import datetime

def read_input(filepath):
    lines = []
    with open(filepath, 'r') as f:
        for line in f:
            lines.append(line.strip())
    
    return lines

def parse_input(lines):
    line_pattern = re.compile("\\[(.*?)\\] (.*)")
    guard_pattern = re.compile("Guard #(\\d+)")
    
    guard_shifts = dict()
    
    lines = sorted(lines)
    guard = None
    
    for line in lines:
        # print(line)
        line_match = re.match(line_pattern, line)
        timestamp = parse_timestamp(line_match.group(1))
        event = line_match.group(2)
        event_letter = event[0]
        
        if (event_letter == 'G'):
            guard_match = re.match(guard_pattern, event)
            guard = guard_match.group(1)
            # print(guard)
        elif (event_letter == 'f'):
            if guard not in guard_shifts:
                guard_shifts[guard] = dict()
            
            if (timestamp.date()) not in guard_shifts[guard]:
                guard_shifts[guard][timestamp.date()] = ['a'] * 60
            
            for minute in range(timestamp.minute, 60):
                guard_shifts[guard][timestamp.date()][minute] = 's'
            # print("Guard", guard, "on", str(timestamp.date()), "-", guard_shifts[guard][timestamp.date()])
        elif (event_letter == 'w'):
            for minute in range(timestamp.minute, 60):
                guard_shifts[guard][timestamp.date()][minute] = 'a'
            # print("Guard", guard, "on", str(timestamp.date()), "-", guard_shifts[guard][timestamp.date()])

    return guard_shifts

def parse_timestamp(time_string):
    return datetime.strptime(time_string, "%Y-%m-%d %H:%M")

def find_sleepiest_minute(guard_shifts, guard):
    minutes = [0] * 60
    for date in guard_shifts[guard]:
        for i in range(len(guard_shifts[guard][date])):
            minutes[i] += 1 if guard_shifts[guard][date][i] == 's' else 0
    
    sleepiest_minute = None
    for i in range(len(minutes)):
        if sleepiest_minute == None or minutes[i] > sleepiest_minute[1]:
            sleepiest_minute = (i, minutes[i])
    
    # print(sleepiest_minute)
    return sleepiest_minute

def find_most_consistent_guard(guard_shifts):
    
    guard_minute_times = None
    for guard in guard_shifts:
        (minute, times) = find_sleepiest_minute(guard_shifts, guard)
        # print(guard, minute, times)
        if guard_minute_times == None or times > guard_minute_times[2]:
            guard_minute_times = (guard, minute, times)
    return (guard_minute_times[0], guard_minute_times[1])


file_input = read_input('input.txt')
# print(file_input)

guard_shifts = parse_input(file_input)

(most_consistent_guard, minute) = find_most_consistent_guard(guard_shifts)

answer = int(most_consistent_guard) * int(minute)
print(answer)
