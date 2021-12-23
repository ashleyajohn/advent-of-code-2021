# Load file
f = open("data/day1_input.txt", "r")
data = f.read().splitlines()
data = [ int(x) for x in data ]

def part_1(data):
    prev = data[0]
    count_increase = 0
    for d in data:
        if d > prev:
            count_increase += 1
        prev = d
    print (f"part 1 answer: {count_increase}")

def part_2(data, window):
    prev_sum = sum(data[0:window])
    count_increase = 0

    for i in range(1, len(data) - window + 1):
        if sum(data[i:i+window]) > prev_sum:
            count_increase += 1
        prev_sum = sum(data[i:i+window])
    print (f"part 2 answer: {count_increase}")

part_1(data)
part_2(data, 3)