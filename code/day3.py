# Load file
f = open("data/day3_input.txt", "r")
data = f.read().splitlines()

def part_1(data):
    gamma = []
    epsilon = []
    len_row = len(data[0])
    for i in range(len_row):
        count_zero = 0
        count_one = 0
        for d in data:
            if d[i] == '0':
                count_zero += 1
            elif d[i] == '1':
                count_one += 1
        if count_zero > count_one:
            gamma.append('0')
        else:
            gamma.append('1')
    for g in gamma:
        if g == '0':
            epsilon.append('1')
        else:
            epsilon.append('0')
    gamma = ''.join(gamma)
    gamma = int(gamma, 2)
    epsilon = ''.join(epsilon)
    epsilon = int(epsilon, 2)
    print (f"part 1 answer: {gamma*epsilon}")

def part_2(data, oxy):
    len_row = len(data[0])
    for i in range(len_row):
        count_zero = 0
        count_one = 0
        for d in data:
            if d[i] == '0':
                count_zero += 1
            elif d[i] == '1':
                count_one += 1
        if oxy:
            if count_zero > count_one:
                decider = '0'
            else:
                decider = '1'
        else:
            if count_zero > count_one:
                decider = '1'
            else:
                decider = '0'
        data = [d for d in data if d[i] == decider]
        if len(data) <= 1:
            break
    rating = int(data[0], 2)
    return rating
    


part_1(data)
oxy = part_2(data, True)
co = part_2(data, False)
print (f"part 2 answer: {oxy*co}")
