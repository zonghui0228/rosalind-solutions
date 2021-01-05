# ^_^ coding:utf-8 ^_^

"""
Find the distance between a pattern and a set of strings.
url: http://rosalind.info/problems/ba2h/

Given: A DNA string Pattern and a collection of DNA strings Dna.
Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
"""

def calculateHammingDistance(a, b)
    hd = 0
    for i in 0...(a.length)
        if a[i] != b[i]
            hd += 1
        end
    end
return hd
end

def DistanceBetweenPatternAndStrings(pattern, strings)
    distance = 0
    k = pattern.length
    strings.each do |string|
        hammingDistance = Float::INFINITY
        for i in 0...(string.length-k+1)
            k_pattern = string[i..i+k]
            hd = calculateHammingDistance pattern, k_pattern
            if hammingDistance > hd
                hammingDistance = hd
            end
        end
        distance += hammingDistance
    end
return distance
end

aFile = File.new("../data/rosalind_ba2h.txt", "r")
    pattern = aFile.readline.strip()
    strings = aFile.readline.strip().split(" ")
aFile.close

distance = DistanceBetweenPatternAndStrings pattern, strings
puts distance
