#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
//3시 28분 시작
//그림의 난이도 = 영역의 수 (영역 = 상하좌우로 같은 색인 부분)
//그림에 몇 개의 영역이 있는지, 가장 큰 영역의 넓이는 얼마인지 계산
//3시 44분 종료

//bfs
//1. 사진을 탐색하면서 탐색 기준점을 정한다. (어느 영역에도 속하지 않고, 방문 안한곳)
//2. 기준점과 상하좌우로 연결된 같은 색(값)을 큐에 넣는다. (어느 영역에도 속하지 않고, 방문 안한곳)
//3. 기준점 별로 방문횟수를 세고 다 탐색하고 나서 최대탐색수를 갱신한다.

vector<vector<bool>> vis;
vector<vector<int>> picture;
int dy[4]={-1,1,0,0};
int dx[4]={0,0,-1,1};
int m; int n;

int bfs(int y, int x){
    queue<pair<int,int>> q;
    q.push({y,x});
    vis[y][x] = true;
    int cnt = 1;
    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int cy = cur.first;
        int cx = cur.second;
        
        for(int dir = 0; dir < 4; dir++){
            int ny = cy + dy[dir];
            int nx = cx + dx[dir];
            if(ny < 0 || ny >= m || nx < 0 || nx >= n) continue;
            if(vis[ny][nx]) continue;
            if(picture[ny][nx]==0)continue;
            if(picture[ny][nx] != picture[cy][cx]) continue;
            
            vis[ny][nx] = true;
            q.push({ny, nx});
            cnt += 1;
            
        }
    }
    return cnt;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
//m: 세로, n: 가로, picture: 그림 정보
vector<int> solution(int M, int N, vector<vector<int>> p) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    picture = p;
    m = M; n = N;
    //vis 초기화
    vis.assign(picture.size(), vector<bool>(picture[0].size(), false));
   
    //기준점 정하기
    int temp;
    for(int i = 0; i < picture.size(); i++){
        for(int j = 0; j < picture[0].size(); j++){
            if(vis[i][j]) continue;
            if(picture[i][j] == 0) continue;
            temp = bfs(i, j);
            if(temp > max_size_of_one_area) max_size_of_one_area = temp;
            number_of_area += 1;
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
