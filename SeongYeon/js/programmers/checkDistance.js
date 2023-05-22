function solution(places) {
  const res = [];
  const map = [];

  places.forEach((place) => {
    for (let i in place) {
      map[i] = place[i].split('');
    }
    res.push(getIsPerfect(map));
  });

  return res;
}

const getIsPerfect = (map) => {
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (map[i][j] === 'P') {
        if (i < 4 && map[i + 1][j] === 'P') return 0;
        if (j < 4 && map[i][j + 1] === 'P') return 0;
        if (i < 4 && j < 4 && map[i + 1][j + 1] === 'P') {
          if (!(map[i + 1][j] === 'X' && map[i][j + 1] === 'X')) return 0;
        }
        if (i < 4 && j > 0 && map[i + 1][j - 1] === 'P') {
          if (!(map[i + 1][j] === 'X' && map[i][j - 1] === 'X')) return 0;
        }
        if (i < 3 && map[i + 2][j] === 'P' && map[i + 1][j] !== 'X') return 0;
        if (j < 3 && map[i][j + 2] === 'P' && map[i][j + 1] !== 'X') return 0;
      }
    }
  }
  return 1;
};
