// 빈 객체 생성하기
const car = new Object;

// key:value 로 이루어진 속성을 가지는 객체 정의
const myCar = {
    wheels: 4
}
console.log(myCar.wheels); // 객체.속성으로 속성에 접근 가능
console.log(myCar["wheels"]); // 대괄호를 이용한 접근
const howManyWheel = "wheels";
console.log(myCar[howManyWheel]); // 변수를 이용할 땐, 따옴표 사용X

// 객체 복사는 "참조" 복사!
let truck = {
    wheels:4
};

let myBike = truck; // 객체를 "참조" 복사함
truck.price = 500000; // 복사된 객체에 새로운 속성 추가

console.log(truck);
console.log(myBike); // truck과 동일한 속성 값 출력 => "참조" 복사했기 때문.

let mySeconCar = Object.assign({}, car); // "car" 객체를 독립적으로 복사해옴 (car 변경사항이 더 이상 적용되지 않음)
let myThridCar = {...car};  // 마찬가지로, car 객체를 독립적으로 복사함.

// 반복문 - break
while(true) {
    let randomNumber = parseInt((Math.random()*6)+1);
    console.log(randomNumber);
    if(randomNumber === 6) {
        break;
    }
}
console.log("6이 출력되어 프로그램이 종료되었습니다.");