from utils import *

# -------------- Define Helper Functions Here
def part_1(data):
    nice = 0
    nice_list = []
    
    for string in data:
        vowelCount = 0
        hasConsec = False
        hasBadStrings = False
        
        for i, char in enumerate(string):
            if char in ["a", "e", "i", "o", "u"]:
                vowelCount += 1
            
            if i < len(string) - 1:
                if char == string[i + 1]:
                    hasConsec = True
                
                if char + string[i + 1] in ["ab", "cd", "pq", "xy"]:
                    hasBadStrings = True
                    
        if vowelCount >= 3 and hasConsec and not hasBadStrings:
            nice += 1
            nice_list.append(string)
            
    print(nice)
    #print(nice_list)
    
def part_2(data):
    
    #data = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    niceCount = 0
    niceList = []
    
    for string in data:
        hasSeperated = False
        hasTwoPairs = False
        pairCounter = dict()

        print(string)
        
        for i, char in enumerate(string):
            
            # check letter sep by letter 'efe'
            if i < len(string) - 2:
                if char == string[i + 2]:
                    hasSeperated = True
                    
            # check for two pairs of letters
                pair = char + string[i + 1]
                j = i + 2 
                while j < len(string) - 1:
                    cPair = string[j] + string[j + 1]
                    if cPair == pair:
                        hasTwoPairs = True
                        break
                    j += 1

            if hasSeperated and hasTwoPairs:
                niceCount += 1
                niceList.append(string)
                break
            
    print(niceCount)

# -------------- Main Entry Point
if __name__ == "__main__":
    data = read_input("input.txt")
    #part_1(data)
    
    part_2(data)