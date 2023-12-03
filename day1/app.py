import re

with open("day1/input.txt") as input:

    inp = input.read().splitlines()

# part 1

# calibration_sum = 0

# for cal in inp:
#     numbers_only = re.sub("[^0-9]", "", cal)
#     calibration_sum += int(numbers_only[0] + numbers_only[-1])

# print(calibration_sum)

# part 2


def text_to_num(txt):

    number_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }


    for k, v in number_map.items():
        if txt.find(k) == 0:
            return v

calibration_sum = 0

for cal in inp:
    cal_numbers = []
    print(cal)
    for x in range(len(cal)):
        if cal[x].isnumeric():
            cal_numbers.append(int(cal[x]))
        else:
            print(cal[x:])

            num = text_to_num(cal[x:])
            if num:
                cal_numbers.append(num)

    print(cal_numbers)
    calibration_sum += int(str(cal_numbers[0]) + str(cal_numbers[-1]))

print(calibration_sum)
    