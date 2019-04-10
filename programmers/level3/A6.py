def mycompare(str1, str2):
    for i in range(len(str1)):
        if str1[:i] == str2[:i] and str1[i+1:] == str2[i+1:]:
            return True
    return False

def search(words, candidate):
    n = len(candidate)
    next = []
    for i in range(n):
        a = candidate.pop(0)
        for j in range(len(words)):
            if mycompare(a, words[j]):
                next.append(j)
        next.sort(reverse=True)
        for b in next:
            candidate.append(words.pop(b))
        next = []
    return words, candidate

def solution(begin, target, words):
    answer = 0
    candidate = [begin]
    while len(candidate) > 0:
        if target in candidate:
            return answer
        words, candidate = search(words, candidate)
        answer += 1
    return 0