def solution(S):
    lookup = {'{':'}','(':')','[':']'}
    stack =[]

    for s in S:
        if s in lookup.keys():
            stack.append(lookup[s])
        
        if s in lookup.value():
            if not stack:
                return 0
            if s != stack.pop():
                return 0

    if stack:
        return 0
    return 1

