numbers = []

file = open("DEMO_17.txt", encoding="utf-8")

for item in file:
    current_number = int(item)
    numbers.append(current_number)

file.close()

min_number = 1000000

for item in numbers:
    if item >= 10 and item <= 99:
        if item < min_number:
            min_number = item

count_pairs = 0
max_sum = 0

for i in range(len(numbers) - 1):
    el1 = numbers[i]
    el2 = numbers[i + 1]

    sum_els = el1 + el2

    if ((el1 >= 10 and el1 <= 99) and not (el2 >= 10 and el2 <= 99)) or (
        not (el1 >= 10 and el1 <= 99) and (el2 >= 10 and el2 <= 99)
    ):
        if sum_els % min_number == 0:
            count_pairs += 1

            if sum_els > max_sum:
                max_sum = sum_els

print(count_pairs)
print(max_sum)
