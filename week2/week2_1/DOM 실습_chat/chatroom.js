
const chatInput = document.getElementById("chat-input");
const hashtagButton = document.getElementById("hashtag");
const sendButton = document.getElementById("btn-send");
const bubblesContainer = document.getElementById("chat-bubble");

chatInput.focus(); /* 시작과 동시에 채팅 인풋창에 커서가 떠있도록! */

// TODO_1: 입력된 값이 있다면 해시태그 대신 전송 버튼이 뜬다
chatInput.addEventListener("input", (event) => {
    const existInput = event.target.value !== "";
    sendButton.style.display = existInput ? "block" : "none";
    /* input event가 없는 상황 */
    hashtagButton.style.display = existInput ? "none" : "block";
    /* input event가 있는 상황 */
});

chatInput.addEventListener("keypress", (event) => {
    /* keypress를 누른 상황 */
    if(event.code === "Enter") {
        sendButton.click(); /* Enter 누르면 전송버튼이 클릭되도록! */
    }
});

// TODO_2: 엔터 버튼을 눌렀을 때(클릭 시) 전송 버튼이 눌린 것과 똑같이 작동을 한다
// 입력된 값은 버블로 띄우기 + input 창 비우기
// 나 -> 교육팀장 -> 나 순회를 해야함

let isMyMessage = true;
sendButton.addEventListener("click", () => {
    if (chatInput.value === "") return;
     
    const bubble = document.createElement("div");

    // 버블 생성
    if (isMyMessage) {
        /* 본인의 버블을 생성 (html 클래스 이름을 참조하여!) */
        bubble.className = "my-bubble-content";
        const bubbleContent = document.createElement("div");
        bubbleContent.className = "my-bubble";
        bubbleContent.innerText = chatInput.value;
        /* 버블 띄우기 */
        bubble.appendChild(bubbleContent);
    }
    else {
        /* 상대의 버블을 생성 (html 클래스 이름을 참조하여!) */
        bubble.className = "your-bubble";
        const bubbleImageContainer = document.createElement("div");
        bubbleImageContainer.className = "profile";
        const bubbleImage = document.createElement("img");
        bubbleImage.src = "./img/profile.png";

        const bubbleContent = document.createElement("div");
        bubbleContent.className = "bubble-content";
        const bubbleName = document.createElement("div");
        bubbleName.className = "name";
        bubbleName.innerText="교육팀장님";
        const bubbleValue = document.createElement("div");
        bubbleValue.className="bubble";
        bubbleValue.innerText = chatInput.value;

        /* 버블 띄우기 위해 입력받은 정보 저장 */
        bubbleImageContainer.appendChild(bubbleImage);
        bubbleContent.appendChild(bubbleName);
        bubbleContent.appendChild(bubbleValue);
        bubble.appendChild(bubbleImageContainer);
        bubble.appendChild(bubbleContent);
        /* 정보 저장한 변수를 버블로 띄우기(추가하기) */
    }
    /* 컨테이너에 버블 붙이기 */
    bubblesContainer.appendChild(bubble);
    bubblesContainer.scrollTop = bubblesContainer.scrollHeight;

    /* 버블 생성 후 입력창 리셋 */
    chatInput.value="";
    hashtagButton.style.display = "block";
    sendButton.style.display = "none";

    isMyMessage = !isMyMessage; /* 순서를 번갈아 가며 채팅하기 위함! */
})