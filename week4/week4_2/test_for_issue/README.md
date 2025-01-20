## 피로그래밍 22기 협업 툴 세션

- 이슈 만들기
- 코드 리팩토링 진행하기

```
1. 클론 받을 폴더로 이동 후 저장소 클론
아래 명령어를 사용해 지정된 저장소를 클론합니다:

git clone https://github.com/taeyeoxn/Piro22_Coop.git

2. 기존 .git 디렉토리 삭제
클론한 디렉토리로 이동한 후 기존 Git 설정을 초기화하기 위해 .git 디렉토리를 삭제합니다:

cd Piro22_Coop
rm -rf .git

3. 프로젝트 디렉토리 초기화
새로운 Git 저장소를 생성합니다:

git init

4. 새 레포지토리 생성 및 연결
GitHub에서 새로운 저장소를 생성한 후, 저장소 URL을 복사합니다.
아래 명령어를 사용해 새로운 저장소를 연결합니다:

git remote add origin <새로운-레포지토리-URL>

5. 연결 상태 확인
연결된 원격 저장소 정보를 확인합니다:

git remote -v
```
