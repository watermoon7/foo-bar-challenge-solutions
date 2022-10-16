def solution(s):
    salutes = 0
    forward = []
    backward = []
    for char in s:
        forward.append('>' if char == '>' else '-')
        backward.append('<' if char == '<' else '-')

    for i in range(len(s)):
        for o in range(len(s)):
            if forward[-1-o] == '>':
                if o == 0:
                    forward[-1-o] = '-'
                else:
                    forward[-1-o] = '-'
                    forward[-o] = '>'
                    if backward[-o] == '<':
                        salutes += 1

        for o in range(len(s)):
            if backward[o] == '<':
                if o == 0:
                    backward[0] = '-'
                else:
                    backward[o] = '-'
                    backward[o-1] = '<'
                    if forward[o-1] == '>':
                        salutes += 1

    return 2*salutes
