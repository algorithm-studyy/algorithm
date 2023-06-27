// Time: 42.86, Memory: 62.86

function reorderLogFiles(logs: string[]): string[] {
  logs.sort((a, b) => {
    if (!isNaN(Number(b.split(' ')[1]))) {
      return !isNaN(Number(a.split(' ')[1])) ? 0 : -1;
    }
  });

  logs.sort((a, b) => {
    if (!isNaN(Number(a.split(' ')[1]))) return 0;

    const splittedA = a.split(' ');
    const splittedB = b.split(' ');
    const identifierA = splittedA.shift();
    const identifierB = splittedB.shift();

    for (let i = 0; i < splittedA.length && i < splittedB.length; i++) {
      if (splittedA[i] < splittedB[i]) return -1;
      if (splittedA[i] > splittedB[i]) return 1;
    }

    if (splittedA.length < splittedB.length) return -1;
    if (splittedA.length > splittedB.length) return 1;

    if (identifierA < identifierB) return -1;
    if (identifierA > identifierB) return 1;

    return 0;
  });

  return logs;
}
