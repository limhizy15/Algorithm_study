# 영화감독 숌
# 브루트포스

'''
666이 많이 들어간 제목..
종말의 숫자 = 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
N번째 종말의 숫자.....
'''

'''
666부터 10000까지 for문 돌려서 해당 수가 종말의 숫자인지.. 확인
=> while True로 변경
cnt로 세고 N번째가 등장하면 print하고 break
'''

n = int(input())

cnt = 0
num = 666
while True:
    # 종말의 숫자..
    if '666' in str(num):
        cnt += 1
    # 만약 cnt가 n과 일치하면 찾고자하는 거니까..
    if cnt == n:
        print(num)
        break
    num += 1

# 틀린 원인 : N 최대값 착각.. for문말고 while로 바꿈