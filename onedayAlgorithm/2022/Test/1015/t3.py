import sys
sys.setrecursionlimit(100000)

def solution(paper, n):
    answer = -2

    def dfs(paper, fold_point, fold_count):
        nonlocal answer

        if fold_count >= n:
            answer = max(answer, max(paper))
            return

        if len(paper) == 1:
            answer = max(answer, paper[0])
            return

        new_paper = fold(paper, fold_point)

        for i in range(len(new_paper)):
            dfs(new_paper[:], i, fold_count + 1)

    def fold(now_paper, fold_point):
        leftIndex = fold_point
        rightIndex = fold_point + 1

        # 접을 포인트가 paper의 길이 / 2보다 크면 오른쪽에서 왼쪽으로 접음
        if fold_point >= int(len(now_paper)/2):
            # 오른쪽에서 왼쪽으로 접을 경우 rightIndex가 len(paper)-1까지 가면 끝남
            # 그리고 leftIndex 쪽에 값을 넣어줌
            while rightIndex <= len(now_paper) - 1:
                now_paper[leftIndex] += now_paper[rightIndex]
                leftIndex -= 1
                rightIndex += 1

            # 반환은 0부터 fold_point를 포함한 리스트
            return now_paper[:fold_point+1]

        # 그게 아니라면 왼쪽에서 오른쪽으로 접음
        else:
            # 왼쪽에서 오른쪽으로 접을 경우 leftIndex가 0이 되면 끝남
            # 그리고 rightIndex 쪽에 값을 넣어줌
            while leftIndex >= 0:
                now_paper[rightIndex] += now_paper[leftIndex]
                leftIndex -= 1
                rightIndex += 1

            # 반환은 fold_point부터 마지막까지
            return now_paper[fold_point+1:]

    for i in range(len(paper)):
        dfs(paper[:], i, 0)

    return answer

paper = [7, 3, 5, -2, 9]
n = 2

paper1 = [10, -10]
n1 = 1

paper2 = [1, 2, 4, 8, 16]
n2 = 3

paper3 = [7, 3, -7, 5, -3]
n3 = 2

print(solution(paper, n))
print(solution(paper1, n1))
print(solution(paper2, n2))
print(solution(paper3, n3))