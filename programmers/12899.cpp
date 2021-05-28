#include <string>
#include <vector>

using namespace std;
//모든 수를 표현할 때 1,2,4만 사용
//3진법을 생각 (0,1,2 대신 1,2,4라는 느낌으로)


string solution(int n) {
    string answer = "";
    //3으로 나누고 그에 맞는 숫자를 더해줌
    while(n > 0){
        //나눠떨어질 때는 나누고 몫 -1을 해줌
        if(n % 3 == 0){
            answer = "4" + answer;
            n = n / 3 - 1;
        }
        else{
            answer = to_string(n%3) + answer;
            n = n / 3;
        }
    }
    
    return answer;
}
