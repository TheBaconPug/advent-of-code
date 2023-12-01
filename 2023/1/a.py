from aocd import submit, get_data

input_text = get_data().splitlines()

total = 0

for line in input_text:
    digits = [char for char in line if char.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)
submit(total, "a")
