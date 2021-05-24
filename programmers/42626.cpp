#include <string>
#include <vector>
#include <queue>
using namespace std;
//3시 19분 시작
//스코빌 지수가 낮은 두 개의 음식 -> 섞어 -> 모든 음식이 K이상의 지수를 가지게 (몇 번 섞어야하는지)

//1. 스코빌 지수를 기준으로 우선순위 큐에 저장
//2. 숫자가 낮은 거 두 번 pop
//3. 새로 섞어서 나온 지수를 큐에 넣어준다
//4. 최소값이 K이상이면 종료 , 아니면 또한다!

//3시 27분 끝

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue <int, vector<int>, greater<int>> pq;
    for(int i = 0; i < scoville.size(); i++){
        pq.push(scoville[i]);
    }
    
    //최소 값이 K보다 작을 때 섞음
    while(pq.top() < K){
        //pq의 크기가 1이면 더 이상 스코빌 지수 못바꿈
        if(pq.size() <= 1){
            answer = -1;
            break;
        }
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        int mix = first + second * 2;
        pq.push(mix); 
        answer += 1;
    }
    
    return answer;
}
