#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
//N개의 정수가 주어졌을 때, X라는 정수가 존재하는지 리턴

int main() {
	//A집합
	int n, m;
	int tmp;
	map<int, bool> hash;

	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		hash[tmp] = true;
	}
	//B의 숫자들이 A집합에 존재하는지 순차적으로 출력 (1)
	cin >> m;
	int find;
	for (int i = 0; i < m; i++) {
		cin >> find;
		if (hash[find]) cout << 1 << "\n";
		else cout << 0 << "\n";
	}
	return 0;
}
