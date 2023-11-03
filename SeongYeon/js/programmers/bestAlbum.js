function solution(genres, plays) {
  const answer = [];
  const total = {};
  const music = {};

  for (let i = 0; i < genres.length; i++) {
    const genre = genres[i];

    if (!music[genre]) {
      total[genre] = plays[i];
      music[genre] = [i];
    } else {
      total[genre] = total[genre] + plays[i];

      if (plays[music[genre][0]] < plays[i]) {
        music[genre][1] = music[genre][0];
        music[genre][0] = i;
      } else if (!music[genre][1] || plays[music[genre][1]] < plays[i]) {
        music[genre][1] = i;
      }
    }
  }

  Object.entries(total)
    .sort(([, a], [, b]) => b - a)
    .forEach((entry) => {
      music[entry[0]].forEach((index) => answer.push(index));
    });

  return answer;
}
