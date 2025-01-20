// TODO_1: 버튼을 불러온다 -> 버튼이 클릭되는지 확인한다
// TODO_2: 버튼을 클릭할 때, 숫자를 불러온다 -> 숫자 값을 바꾼다

const minusbutton = document.getElementById('minus_button');
const plusbutton = document.getElementById('plus_button');
const counter = document.getElementById('counter');

/*
잘 뜨는지 확인용~!
console.log(minusbutton);
console.log(plusbutton);
console.log(counter);
*/

minusbutton.addEventListener("click", () => {
    counter.innerText = Number(counter.innerText)-1;
});

plusbutton.addEventListener("click", () => {
    counter.innerText = Number(counter.innerText)+1;
});