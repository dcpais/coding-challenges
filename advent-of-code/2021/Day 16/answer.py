from __future__ import annotations
from utils import *

def read_packet(data: str, start_idx: int) -> List:
    pass

if __name__ == '__main__': 
    data = read_input("input.txt")
    bits = bin(int(data[0].strip(), 16))[2:]

    #Part 1:
    idx = 0
    versions = []
    type_ids = []
    while idx < len(bits) - 1:
        v = bits[idx : idx + 3]; idx += 3
        versions.append(v)

        tid = bits[idx : idx + 3]; idx += 3
        type_ids.append(tid)

        if tid == "100":
            literal = ""
            while idx < len(bits) - 1:
                seg = bits[idx : idx + 5]; idx += 5
                literal += seg[1:]
                if seg[0] == "0":
                    print(f"Packet (Literal): {literal} -> {int(literal, 2)}")
                    break
            continue
        
        lid = bits[idx]; idx += 1
        if lid == "1":
            





    


    
