// TODO_1: 슬라이더 불러오기 -> 슬라이더가 어디까지 갔는지 인식
// TODO_2: 글자 불러오기 -> 슬라이더 이동 값만큼 굵기(weight) 조절

const slider = document.getElementById("text_slider");
const container = document.getElementById("container");

const texts = container.children;

console.log(slider);
console.log(container);
console.log(texts);

slider.addEventListener("input", (event) => {
    console.log(event.target.value);
    /* 
    map은 배열 자체 메소드 (for 보다 주로 사용)
    배열의 요소 여러 개를 하나씩 꺼내옴 
    */
    Array.from(texts).map((text) => {
        text.style.fontWeight = event.target.value * 10;
    });
});
