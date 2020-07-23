# ^_^ coding:utf-8 ^_^

"""
Reversal Distance
http://rosalind.info/problems/rear/

Given: A collection of at most 5 pairs of permutations, all of which have length 10.
Return: The reversal distance between each permutation pair.
"""

def _get_reverse_array(s):
    reverse_arrays = []
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            r_list = s[i:j+1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j+1:])
    return reverse_arrays


def _get_reversal_distance(s1, s2, distance):
    # reverse s1 to s2, and reverse s2 to s1 at same time.
    if s1 & s2:
        return distance
    # get the reveral array of s1.
    new_s1 = set()
    for s in s1:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s1.add(tuple(r))
    # get the reveral array of s2.
    new_s2 = set()
    for s in s2:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s2.add(tuple(r))
    # thus we reverse s1 and s2 at same time, so distance plus 2. 
    distance += 2
    # if s1 and the reversal array of s2 has the same array, distance substract 1.
    if s1 & new_s2:
        return distance-1
    # if s2 and the reversal array of s1 has the same array, distance substract 1.
    if s2 & new_s1:
        return distance-1
    # if reversal array of s1 and the reversal array of s2 has the same array, return distance.
    if new_s1 & new_s2:
        return distance
    
    distance = _get_reversal_distance(new_s1, new_s2, distance)
    return distance


if __name__ == "__main__":
    # test
    # a = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
    # b = [5, 2, 3, 1, 7, 4, 10, 8, 6, 9]
    # distance, s1, s2 = 0, set(), set()
    # s1.add(tuple(a)), s2.add(tuple(b))
    # d = _get_reversal_distance(s1, s2, distance) # 4
    # print(d)

    # load data
    with open("../data/rosalind_rear.txt", "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines() if line.strip()]
    for i in range(0, len(lines), 2):
        a = [l for l in lines[i]]
        b = [l for l in lines[i+1]]
        distance, s1, s2 = 0, set(), set()
        s1.add(tuple(a)), s2.add(tuple(b))
        d = _get_reversal_distance(s1, s2, distance)
        print(d)

    print("done!")

