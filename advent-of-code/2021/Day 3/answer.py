from utils import *

def oxygen_rating(data: List[str]) -> str:
    
    filtered = data.copy()
    for digit in range(12):
        selected = []
        count = 0
        for number in filtered:
            if number[digit] == '1':
                count += 1
        
        mostCommon = '1' if (count >= len(filtered) / 2) else '0'

        for number in filtered:
            if number[digit] == mostCommon:
                selected.append(number)

        if len(selected) == 1:
            return selected[0]
        
        filtered = selected.copy()

def co2_rating(data: List[str]) -> str:
    
    filtered = data.copy()
    for digit in range(12):
        selected = []
        count = 0
        for number in filtered:
            if number[digit] == '1':
                count += 1
        
        mostCommon = '0' if (count >= len(filtered) / 2) else '1'

        for number in filtered:
            if number[digit] == mostCommon:
                selected.append(number)

        if len(selected) == 1:
            return selected[0]
        
        filtered = selected.copy()



if __name__ == '__main__':
    data = read_input("input.txt")
    #Organize data
    for i in range(len(data)):
        if data[-1] == '\n':
            data[i] = data[i][:-1]

    favoured = []
    #Get count of each digit being
    for digit in range(12):
        count = 0
        for number in data:
            if number[digit] == '1':
                count += 1
        favoured.append(count)
        count = 0 

    #Construct gamma and epsilon
    gamma = ''
    epsilon = ''
    totalNums = len(data) / 2
    for i in range(len(favoured)):
        gamma += '1' if favoured[i] > totalNums else '0'
        epsilon += '0' if favoured[i] > totalNums else '1'
    
    power = int(gamma, 2) * int(epsilon, 2)
    print(f"Part 1: power rating = {power}")

    #PART 2:
    o2Rating = oxygen_rating(data)
    co2Rating = co2_rating(data)
    print(f"Part 2: life support rating = {int(o2Rating, 2) * int(co2Rating, 2)}")



