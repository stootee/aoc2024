def part1(list1, list2):
    differences = []
    for n in range(len(list1)):
        differences.append(abs(list1[n] - list2[n]))

    part1 = sum(differences)
    print("part1", part1)