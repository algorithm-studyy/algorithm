const fs = require('fs');

// 테스트용 파일 경로
const inputFile = 'test/input.txt';

// 제출용 파일 경로
const inputFile = '/dev/stdin';

// 문자 하나만 입력받을때
const input = fs.readFileSync(inputFile).toString();

// 한칸 띄어쓰기로 구분
const input = fs.readFileSync(inputFile).toString().split(' ');

// 줄바꿈으로 구분
const input = fs.readFileSync(inputFile).toString().split('\n');

// 인풋값이 숫자일때
const input = fs
  .readFileSync(inputFile)
  .toString()
  .split('\n')
  .map(function (a) {
    return +a;
  });
