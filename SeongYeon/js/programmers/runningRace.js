function solution(players, callings) {
  const rankingByName = {};

  players.forEach((player, ranking) => {
    rankingByName[player] = ranking;
  });

  callings.forEach((call) => {
    const newRanking = rankingByName[call] - 1;
    const loser = players[newRanking];

    rankingByName[call] = newRanking;
    rankingByName[loser] = newRanking + 1;

    players[newRanking] = call;
    players[newRanking + 1] = loser;
  });

  return players;
}
