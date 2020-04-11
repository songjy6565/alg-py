def solution(words):
    answer = 0
    words = sorted(words)
    length = len(words)
    target = 'dummy'
    index = 0
    while True:
        #print(index, length, answer, words)
        if length <= 1:
            if target == words[0][0]:
                answer += 2
                return answer
            answer += 1
            return answer
        if index >= length:
            index = 0
            target = 'dummy'
            continue
        if target != words[index][0]:
            if index != 0:
                return answer+solution(words[0:index])+solution(words[index:])
            if index == length-1:
                answer += 1
                words.pop(index)
                length -= 1
                continue
            if words[index][0] == words[index+1][0]:
                target = words[index][0]
                if len(words[index]) != 1:
                    words[index] = words[index][1:]
                    answer += 1
                    index += 1
                    continue
                else:
                    answer += 1
                    words.pop(index)
                    length -= 1
                    continue
            else:
                answer += 1
                words.pop(index)
                length -= 1
                continue
        else:
            if len(words[index]) != 1:
                words[index] = words[index][1:]
                answer += 1
                index += 1
                continue
            else:
                answer += 1
                words.pop(index)
                length -= 1
                continue
    return answer