# Load file
f = open("data/day2_input.txt", "r")
data = f.read().splitlines()

def part_1(data):
    forward_status = 0
    depth_status = 0
    for d in data:
        direction, amount = d.split(' ')
        if direction == 'forward':
            forward_status += int(amount)
        if direction == 'down':
            depth_status += int(amount)
        if direction == 'up':
            depth_status -= int(amount)
    print (f"part one answer: {forward_status * depth_status}")

def part_2(data):
    forward_status = 0
    depth_status = 0
    aim = 0

    for d in data:
        direction, amount = d.split(' ')
        if direction == 'forward':
            forward_status += int(amount)
            depth_status += int(amount) * aim
        if direction == 'down':
            aim += int(amount)
        if direction == 'up':
            aim -= int(amount)
    print (f"part two answer: {forward_status * depth_status}")

part_1(data)
part_2(data)