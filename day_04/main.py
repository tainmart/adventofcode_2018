import re
from collections import Counter

data = [i for i in open('input').readlines()]
data.sort()

guards = {}

def getGuard(line):
    id_guard = re.search("#\d*", line)
    return id_guard.group(0)[1:]

def getMinutes(line):
    minutes = re.search(":\d*", line)
    return int(minutes.group(0)[1:])

if __name__ == "__main__":
    for line in data:
        if line.find("Guard") != -1:
            guard = getGuard(line)
        if line.find("falls asleep") != -1:
            begin = getMinutes(line)
        if line.find("wakes up") != -1:
            end = getMinutes(line)
            for i in range(begin, end):
                guards.setdefault(guard, []).append(i)

    sleepy_guard = max(guards, key=lambda x: len(guards[x]))
    sleepy_minute = Counter(guards[sleepy_guard]).most_common()[0][0]
    print("Guard id {:s} * minute {:d} = {:d}"
          .format(sleepy_guard, sleepy_minute, int(sleepy_guard) * sleepy_minute))
    print("-------------------")
    sleepy_guard2 = max(guards, key=lambda x: Counter(guards[x]).most_common()[0][1])
    sleepy_minute2 = Counter(guards[sleepy_guard2]).most_common()[0][0]
    print("Guard id {:s} * minute {:d} = {:d}"
          .format(sleepy_guard2, sleepy_minute2, int(sleepy_guard2) * sleepy_minute2))
