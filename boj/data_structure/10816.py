'''
숫자카드 : 정수하나가 적혀있는 카드
상근 -> 숫자카드 N개
정수 M개가 주어졌을 때 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지
'''

'''
N
N개의 숫자카드
M
M개의 찾을 숫자
'''

'''
N개를 딕셔너리에 {1:cnt} 형태로 저장하고 찾을 때 인덱싱으로 ..
'''

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

# 해쉬
sang_cards = {}
for i in range(n):
    if cards[i] in sang_cards:
        sang_cards[cards[i]] += 1
    else:
        sang_cards[cards[i]] = 1

for item in search:
    if item in sang_cards:
        print(sang_cards[item], end=" ")
    else:
        print(0, end=" ")


# print(sang_cards)
# print(cards)
# print(search)
