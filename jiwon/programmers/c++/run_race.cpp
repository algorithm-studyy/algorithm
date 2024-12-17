#include <string>
#include <map>
#include <vector>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    map<string, int> race;
    
    for (int i = 0; i < players.size(); i++){
        race[players[i]] = i;
    }
    
    for (const auto& c : callings) {
        int i = race[c];
        race[c] -= 1;
        string temp = players[i - 1];
        race[temp] += 1;
        players[i - 1] = players[i];
        players[i] = temp;
    }
    
    return players;
}