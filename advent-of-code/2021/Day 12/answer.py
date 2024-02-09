from utils import *

class Path(object): 
    def __init__(self, path):
        self.path = path 
        
    def get_current(self):
        return self.path[-1]

def get_small_count(path):

    count = dict()

    for tunnel in path:
        if not tunnel.islower():
            continue
        if tunnel not in count.keys():
            count[tunnel] = 1
        else:
            count[tunnel] += 1
        
    for val in count.values():
        if val >= 2:
            return False

    return True

if __name__ == "__main__":

    data = read_input("input.txt")
    tunnels = dict()

    for tunnel in data:
        caves = tunnel.strip().split("-")
        if caves[0] not in tunnels.keys():
            tunnels[caves[0]] = []
        if caves[1] not in tunnels.keys():
            tunnels[caves[1]] = []
        tunnels[caves[0]].append(caves[1])
        tunnels[caves[1]].append(caves[0])

    #print(tunnels)

    frontier = [Path(["start"])]
    completed = []
    while frontier:
        
        current = frontier.pop(0)
        #print(current.path)
        #print(f"{current.get_current()}: {tunnels[current.get_current()]}")
        for neighbour in tunnels[current.get_current()]:
            #print(neighbour)
            if neighbour == "end":
                completed.append(current.path + ["end"])
                continue
            elif neighbour == "start":
                continue
            elif neighbour.isupper():
                frontier.append(Path(current.path + [neighbour]))
                continue
            elif neighbour.islower():
                if neighbour in current.path:
                    if not get_small_count(current.path):
                        continue
                frontier.append(Path(current.path + [neighbour]))
    


    #for path in completed:
    #    print(path)
    print(len(completed))



    
