    using System;
    using System.Collections.Generic;

    public class Solution {
        public string[] solution(string[] players, string[] callings) {
            Dictionary<string, int> p = new Dictionary<string, int>();


            for (int i = 0; i < players.Length; i++) {
                p[players[i]] = i;
            }

            foreach (var call in callings) {
                int index = p[call];
                p[call] -= 1;
                p[players[index - 1]] += 1;
                string temp = players[index];
                players[index] = players[index - 1];
                players[index - 1] = temp;

            }
            return players;
        }
    }