from aoc import get_input

data = get_input(2).splitlines()
checksum = 0

for line in data:
    numbers = list(map(int, line.split()))
    checksum += max(numbers) - min(numbers)

print(checksum)

checksum_2 = 0
for line in data:
    numbers = list(map(int, line.split()))
    for i, num_1 in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            bigger, smaller = (num_1, numbers[j]) if num_1 > numbers[j] else (numbers[j], num_1)
            if bigger % smaller == 0:
                checksum_2 += bigger // smaller

print(checksum_2)