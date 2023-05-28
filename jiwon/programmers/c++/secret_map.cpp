#include <string>
#include <iostream>
#include <vector>
#include <deque>

using namespace std;


vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for (int i = 0; i < arr1.size(); i++) {
        int num = arr1[i] | arr2[i];
        deque<string> q(n);
        string str = "";
        while (num > 0) {
            if (num % 2 == 1) q.push_back("#");
            else q.push_back(" ");
            num /= 2;
        }
        while (q.size() < n * 2) q.push_back(" ");
        while (q.size() > 0) {
            str.append(q.back());
            q.pop_back();
        }
        answer.push_back(str);

    }
    return answer;
}