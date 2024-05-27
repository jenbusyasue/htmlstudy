# ex = [[1, 3], [0, 6], [5, 6], [4, 8], [6, 7], [9, 15]]

j = int(input())
ex = [list(map(int, input().split())) for _ in range(j)]
ex.sort()
count = 1 # 최대 회의 갯수
meeting_end_time = ex[0][1]

i = 1
print(ex)
while i < j:
    if meeting_end_time > ex[i][0]:
        i += 1
    else:
        meeting_end_time = ex[i][1]
        count += 1
        i += 1

print(count)
