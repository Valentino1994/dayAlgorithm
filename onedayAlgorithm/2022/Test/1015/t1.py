def solution(source):

    answer = ''
    copySource = source

    while copySource:
        dest = []
        for s in copySource:
            if s not in dest:
                dest.append(s)
                copySource = copySource.replace(s, "", 1)

        answer += "".join(sorted(dest))

    return answer

source = "execute"

print(solution(source))
