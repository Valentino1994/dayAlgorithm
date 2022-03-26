def solution(sentences, n):
    answer = -1

    possible_sentences = []

    for sentence in sentences:
        tmp = []
        score = len(sentence)
        for s in sentence:
            if s not in tmp and s != " ":
                tmp.append(s.lower())
            if s.upper() == s and s != " ":
                score += 1
                if "shift" not in tmp:
                    tmp.append("shift")

        if len(tmp) <= n:
            possible_sentences.append([score, sentence, tmp])

    # 최댓값을 구하는 법으로 점수가 큰 것을 정렬하고, 범위를 좁혀가면서 계산하는 것으로 했다.
    new_arr = sorted(possible_sentences)[::-1]
    for i in range(len(new_arr)):
        tmp = 0
        now_key = []
        for j in range(i, len(new_arr)):
            for string in new_arr[j][2]:
                if string not in now_key:
                    now_key.append(string)
            if len(now_key) <= n:
                tmp += new_arr[j][0]

            else:
                break

        if tmp > answer:
            answer = tmp

    # 완성할 수 있는 문자열이 없었다면 0을 리턴한다.
    if answer == -1:
        return 0

    return answer