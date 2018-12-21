# KMP (Knuth Morris Pratt) Algorithm for pattern matching

def patternArray(arr):
    pArr = [0 for x in range(len(arr))]
    i = 1
    j = 0
    while i < len(arr):
        if arr[i] == arr[j]:
            j += 1
            pArr[i] = j
            i += 1
        else:
            if j!=0:
                j = pArr[j-1]
            else:
                pArr[i]= 0
                i+=1
    return pArr

def kmp_algo(text, pattern):
    match = patternArray(pattern)
    print match
    lengthText= len(text)
    lengthPattern = len(pattern)
    t = 0 # index for text
    p = 0 # index for pattern both start with first char
    if text[t] == pattern[p]:
        t += 1
        p += 1
    if p == lengthPattern:
        print 'pattern occurs at '+ t-p
        p = match[p-1]
    elif t < lengthText and pattern[p] != text[t]:
        if p != 0:
            p = match[p-1]
        else:
            t += 1

text = "abcabceabcabc"
pattern = "abcab"

kmp_algo(text, pattern)