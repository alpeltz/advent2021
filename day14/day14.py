from collections import Counter
from collections import defaultdict
import threading
import math
def insert_chars(pairs,rules, chars):
    new_pairs=defaultdict(int)
    removed_pairs=defaultdict(int)
    for pair in pairs:
        if pair in rules:
            char = rules[pair]
            new_pairs[pair[0] + char] += pairs[pair]
            new_pairs[char+pair[1]] += pairs[pair]
            removed_pairs[pair] += pairs[pair]
            chars[char] += pairs[pair]
    return new_pairs, removed_pairs
with open("input.txt") as f:
    lines = f.readlines()
    template = lines[0].strip()
    #skip the blank between template and rules
    rules={}
    for line in lines[2:]:
        pair,insert=line.strip().split(" -> ")
        rules[pair] = insert
    pairs=defaultdict(int)
    chars=defaultdict(int)
    for (i,c) in enumerate(template):
        if i != len(template)-1:
            pairs[template[i:i+2]]+=1
        chars[c] +=1
    for i in range(40):
        if (i%2 ==0):
            print("Progress: ", i/40)
        new_pairs,removed_pairs = insert_chars(pairs,rules,chars)
        for p in new_pairs:
            pairs[p] += new_pairs[p]
        for p in removed_pairs:
            pairs[p] -= removed_pairs[p]
    max_c=chars[max(chars,key=chars.get)]
    min_c=chars[min(chars,key=chars.get)]
    print(max_c-min_c)
