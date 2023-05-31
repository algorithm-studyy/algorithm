#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

bool compare(pair<int, double> a, pair<int, double> b) {
    if (a.second > b.second) return true;
    else if (a.second < b.second) return false;
    if (a.first < b.first) return true;
    else if (a.first > b.first) return false;
    return true;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    map<int, int> sucess;
    vector<pair<int, double>> stageClear;
    for (int i = 1; i <= N + 1; i++) sucess.insert(make_pair(i, 0));
    for (int &i: stages) sucess.insert(make_pair(i, ++sucess.at(i)));
    int total = stages.size();
    double value;
    for (int i = 1; i <= N; i++) {
        if (total > 0) value = (double)sucess.at(i) / (double)total;
        else value = 0;
        stageClear.push_back(make_pair(i, value));
        total -= sucess.at(i);
    }

    sort(stageClear.begin(), stageClear.end(), compare);
    for (pair<int, double> &i: stageClear) answer.push_back(i.first);
    return answer;
}
