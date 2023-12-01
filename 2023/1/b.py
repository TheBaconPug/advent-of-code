from aocd import submit, get_data

input_text = get_data().splitlines()

# first letter in word + number + last letter in word
number_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

total = 0

for line in input_text:
    for word, replacement in number_map.items():
        line = line.replace(word, replacement)

    digits = [char for char in line if char.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)
submit(total, "b")
