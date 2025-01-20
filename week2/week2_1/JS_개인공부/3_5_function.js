// 익명 함수
const greet = function() {
    console.log("안녕하세요! 저는 익명 함수입니다.");
};
greet();

// 네이밍 함수
const factorial = function calcFactorial(n) {
    if(n<=1) return 1;
    return n*calcFactorial(n-1); // 재귀호출
};
console.log(factorial(3));

function sum(a,b) {
    return a+b;
} // 일반 함수
const sum = (a,b) => a+b; // 화살표 함수

function minus(a,b) {
    return a-b;
}
const minus = (a,b) => {return a-b}; // 블록 사용 시, return 필요

// 콜백함수
function prepareFood(callback) {
    console.log("음식을 준비 중입니다...");
    setTimeout(() => {
        console.log("음식 준비 완료!");
        callback();
    }, 2000);
}
function eatFood() {
    console.log("음식을 먹습니다!");
}
prepareFood(eatFood);