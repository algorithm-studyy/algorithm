#include <string>
#include <vector>

using namespace std;

vector<int> fold(vector<int> bill) {
    if (bill[0] > bill[1]) {
        bill[0] /= 2;
    } else {
        bill[1] /= 2;
    }
    return bill;
}

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;
    while (!((wallet[0] >= bill[0] && wallet[1] >= bill[1]) || 
            (wallet[0] >= bill[1] && wallet[1] >= bill[0]))) {
       
        bill = fold(bill);
        answer++;
    }
    return answer;
}