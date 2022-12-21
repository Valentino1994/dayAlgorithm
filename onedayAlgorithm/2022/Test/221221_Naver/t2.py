from itertools import groupby

def solution(S, C):
    # Implement your solution here
    letter_groups = [[k, len(list(g))] for k, g in groupby(S)]
    answer = 0
    letter_start_index = 0
    for letter_group in letter_groups:
        now_letter_continuity = letter_group[1]

        if now_letter_continuity == 1:
            letter_start_index += now_letter_continuity
            continue

        list_of_continuous_letter = C[letter_start_index : now_letter_continuity+letter_start_index]
        answer += sum(list_of_continuous_letter) - max(list_of_continuous_letter)
        letter_start_index += now_letter_continuity

    return answer

S = 'abccbd'
C = [0, 1, 2, 3, 4, 5]
print(solution(S, C))