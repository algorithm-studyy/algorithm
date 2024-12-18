#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <vector>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    unordered_map<string, int> userIndexMap;
    for (int i = 0; i < id_list.size(); i++) {
        userIndexMap[id_list[i]] = i;
    }
    
    unordered_map<string, unordered_set<string>> userReports;
    for (const string& id : id_list) {
        userReports[id] = unordered_set<string>();
    }
    
    for (const string& r : report) {
        stringstream ss(r);
        string reporter, reportedUser;
        ss >> reporter >> reportedUser;
        
        userReports[reporter].insert(reportedUser);
    }
    
    unordered_map<string, int> reportCount;
    for (const auto& [reporter, reportedUsers] : userReports) {
        for (const string& reportedUser : reportedUsers) {
            reportCount[reportedUser]++;
        }
    }
    
    vector<int> answer(id_list.size(), 0);
    for(const auto& [reporter, reportedUsers] : userReports) {
        for (const string& reportedUser : reportedUsers) {
            if (reportCount[reportedUser] >= k)
                answer[userIndexMap[reporter]]++;
        }
    }
    return answer;
}