'''
[문제]
전화번호 목록이 주어질 때, 어떤 전화번호가 다른 전화번호의 접두사가 되는 경우 false를 return

[풀이]
처음생각 : 그냥 폰북을 for문 2번으로 탐색해볼까? > 백퍼센트 터진다
-> 그럼 정렬해서 자기거 이후것만 보면서 탐색하면? 정확도는 100%지만 효율성테스트에서 시간초과
-> 어차피 정렬된 상태이니 phonebook[i]와 phonebook[i+1]만 보면되겠다. -> 효율성테스트 통과
=> 근데.. 이게 해시를 이용한 풀이인가?

[해시를 이용한 풀이 (검색)]
출처 : https://huidea.tistory.com/6
1. 전화번호를 모두 딕셔너리로 생성
2. phone_book을 탐색하면서 전화번호 하나꺼냄
1) 얘를 하나씩 뜯으면서 ex) "0", "01", "010" ... 
2) 딕셔너리에서 검색..
=> 문자열 뜯어서 비교해볼 생각은 못했었는데 신기함!
'''

def solution(phone_book):
    answer = True
    
    # 전화번호부 정렬
    phone_book.sort()
    n = len(phone_book)
    
    # 전화번호부를 탐색하면서
    for i in range(n-1):
        # 접두어로 할 문자열 하나 찾고
        cur = phone_book[i]
        # 그 다음 문자열의 접두사인지 여부 파악
        if phone_book[i+1].startswith(cur):
            answer = False
            break  
            
    return answer