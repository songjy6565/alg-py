def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            count += 1
        if s[i] == 'y' or s[i] == 'Y':
            count -= 1
    if count == 0:
        return True
    return False