#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isPossible(const vector<vector<string>>& park park, int y, int x,int mat) {
    if (y + mat > park.size() || x + mat > park[0].size()) {
        return false;
    }
    
    for (int i = y; i < y + mat; i++) {
        for (int j = x; j < x + mat; j++) {
            if (park[i][j] != "-1") {
                return false;
            }
        }
    }
    return true;
}

int solution(vector<int> mats, vector<vector<string>> park) {
    int answer = -1;
    
    for (int i = 0; i < park.size(); i++) {
        for (int j = 0; j < park[i].size(); j++) {
            if (park[i][j] != "-1") {
                continue;
            }
            for (int mat: mats) {
                if (isPossible(park, i, j, mat)) {
                    answer = max(mat, answer);
                }
            }
        }
    }
    
    return answer;
}