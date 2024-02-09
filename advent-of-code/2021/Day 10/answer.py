from utils import data
import numpy

if __name__ == '__main__':
    data = read_input("input.txt")
    data = [line.strip() for line in data]
    open_list = ['[', '<', '{', '(']
    close_list = [']', '>', '}', ')']
    scorecard = { '(': 1,
                  '[': 2,
                  '{': 3,
                  '<': 4,
                  ')': 3,
                  ']': 57,
                  '}': 1197,
                  '>': 25137 }
    
    score_p1 = 0
    scores_p2 = []
    for i, line  in enumerate(data):
        stack = []
        corrupt = False
        for char in line:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                pos = close_list.index(char)
                if (len(stack) > 0) and \
                    (open_list[pos] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    score_p1 += scorecard[char]
                    corrupt = True
                    break
        
        completion_score = 0
        if not corrupt:
            while stack:
                completion_score *= 5
                completion_score += scorecard[stack.pop()]
            scores_p2.append(completion_score)

    scores_p2.sort()
    print(f"Part 1: {score_p1}")
    print(f"Part 2: {scores_p2[len(scores_p2) // 2]}")
    
                

    



    


