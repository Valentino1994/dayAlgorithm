import re

# 딕셔너리로 했으면 풀렸다.
def solution(registered_list, new_id):
    answer = ''
    characters = re.findall('[a-z]+', new_id)
    while True:

        temp = []
        S = ''

        if new_id not in registered_list:
            answer = new_id
            return answer

        numbers = re.findall('[0-9]+', new_id)

        if not numbers:
            new_id = characters[0] + '1'
        else:
            new_id = characters[0] + str(int(numbers[0])+1)

registered_list = ["apple", "apple1", "orange", "banana3"]
new_id = "apple"
registered_list1 = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
new_id1 = "cow"
registered_list2 = ["bird99", "bird98", "bird101", "gotoxy"]
new_id2 = "bird98"
print(solution(registered_list, new_id))
print(solution(registered_list1, new_id1))
print(solution(registered_list2, new_id2))