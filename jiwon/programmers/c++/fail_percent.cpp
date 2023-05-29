#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    map<int, int> sucess;
    vector<pair<int, double>> stageClear;
    for (int i = 1; i <= N; i++) sucess.insert(make_pair(i, 0));
    for (int &i: stages) sucess.insert(make_pair(stages[i], ++sucess.at(stages[i])));
    int total = stages.size();
    double value;
    for (int i = 1; i <= N; i++) {
        if (total > 0) value = (double)sucess.at(i) / (double)total;
        else value = 1;
        stageClear.push_back(make_pair(i, value));
        total -= sucess.at(i);
    }
    return answer;

}