"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    res = []
    index = 0
    for num in line:
        res.append(0)
        if num != 0:
            res[index] = num
            index += 1
    
    for dummy_num in range(len(res)-1):
        if res[dummy_num] == res[dummy_num+1]:
            res[dummy_num] *= 2
            res.append(0)
            res.pop(dummy_num+1)
    return res



#print merge([2,0,2,2])
print merge([2,0,2,4])
print merge([0,0,2,2])
print merge([2,2,0,0])
print merge([2,2,2,2,2])
print merge([8,16,16,8])

