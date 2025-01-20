let level = 'A';

switch (level) {
    case 'A':
        console.log('장학금 100만원');
        break;
    case 'B':
        console.log('징학금 80만원');
        break;
    default:
        console.log('장학금 40만원');
        break;
} // 출력: 장학금 50만원

const permissions = title === '부장' || title === '과장'?
    title === '부장'? ['근로시간', '초과근무 승인', '수당'] : ['근로시간', '수당']:
    ['근로시간'];