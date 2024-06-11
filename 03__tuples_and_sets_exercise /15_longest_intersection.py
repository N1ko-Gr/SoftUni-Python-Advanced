first_set = set()
second_set = set()

longest_intersection = set()

for _ in range(int(input())):

    line = input().split("-")
    first_start, first_end = line[0].split(",")
    second_start, second_end = line[1].split(",")

    first_set = set(int(x) for x in range(int(first_start), int(first_end) + 1))
    second_set = set(int(x) for x in range(int(second_start), int(second_end) + 1))

    current_set = first_set.intersection(second_set)

    if len(current_set) > len(longest_intersection):
        longest_intersection = current_set


print(f"Longest intersection is {''.join(str(list(longest_intersection)))} with length {len(longest_intersection)}")