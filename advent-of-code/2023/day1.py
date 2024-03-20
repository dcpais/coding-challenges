text = ""

with open("day1.txt", "r") as f:
    text = f.readlines()

letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def firstDigit(string):
    for char in string:
        if char.isnumeric():
            return char

total = 0
for line in text:
    total += int(firstDigit(line) + firstDigit(line[::-1]))

print(total)