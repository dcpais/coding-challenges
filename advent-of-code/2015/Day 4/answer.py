from utils import *
import hashlib

# -------------- Define Helper Functions Here


# -------------- Main Entry Point
if __name__ == "__main__":
    data = "bgvyzdsv"
    
    for i in range(10000000):
        hashStr = data + str(i)
        cHash = hashlib.md5(hashStr.encode()).hexdigest()
        if cHash[:6] == "000000":
            print(i)
            break
    