def part2(list1, list2):
    similarity = 0
    for x in list1:
        similarity += x * list2.count(x)

    print("part2:", similarity)