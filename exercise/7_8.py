# n = 떡의 개수, m = 요청한 떡의 길이
n, m = map(int, input().split())
array = list(map(int, input().split()))
# 떡을 길이 기준 내림차순 정렬

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid + 1
