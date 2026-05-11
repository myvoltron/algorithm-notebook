def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        h_index = len(citations) - i
        if citations[i] >= h_index:
            answer = h_index
            break
    return answer
