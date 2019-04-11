# Git린이 Github 사용기

## **준비물 :**

**Terminal**

* Editor: vim, emacs, nano

(vim 기본 설명: https://zeddios.tistory.com/122)

## 1. Git 사용 환경 세팅

* ssh-keygen : 을 이용하여 사용자 ID / PW 일일이 입력하지 않아도 된다.

( SSH key 설정 참고 : <https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>)

* Github 사이트 Setting 들어가서 설정해서 id_rsa.pub안의 key를 복사/붙여넣기 하면 된다.
* 환경 설정 방법 :vim 에디터로 직접 들어가서 [alias] 탭에 설정값 추가 가능
  * vim ~/.gitconfig 



## 2. Git 주요 사용 명령어

*  git log --oneline --decorate --graph --all

* git branch -r :

  * -r : remote상에 있는 branch를 다 보여줌
  * -a : local / remote 상에 있는 모든 branch 보여줌

* git chekout (branch):

  * checkout 자체가 HEAD를 이동시키는 것

* git pull options repository ref : (ex) git pull origin develop-sjs)

  * Remote repository 상의 HEAD와 내 branch가 일치하지 않을 수 있으므로 변경사항 업데이트를 위해 우선 pull 부터 먼저 하자

* git add -p 파일이름.py 

  * 부분적으로 파일 선택하여 untracked -> tracked 로 변경 

    (git add . 하면 모든 파일이 add 되므로 하면 안됨!)

  * line 별로 변경사항을 나누어 y,q,s에 따라 hunk 덩어리 설정.

    (y: yes?/ keep going , q: Quit?, s:split) 

* git commit -s -v 

  * tracked 파일을 staged로 변경하기 위해 commit을 진행.

    (git commit -m "blahblah" 보다는 -s : sign-off +  -v : 한번더 체크로 변경사항 설명)

  * 이 안에서 편집기에 따라 사용 방법이 조금 다름

    * vim 인 경우 : a로 편집 모드 -> 수정 사항 입력 -> :w 저장 -> :q 나가기 (vi :x)
    * nano 인 경우 : 수정 사항 입력 -> ctrl+o 저장 -> ctrl+x 나가기

* git push option remote repositor

  * 현재 staged 된 commit을 설정한 remote repository에 push함

  *  (ex: git push origin develop-sjs) : 내가 작업한 branch에서 remote 상의 develop-sjs branch로 push 함. 이 때 Github 관리자에게 Pull Request가 날아감

    

# Git의 특징

1. DVCS : 분산형 버전 관리 시스템 (Distributed Version Control System)

   ![image-20190331195936969](/Users/jongsun/Library/Application Support/typora-user-images/image-20190331195936969.png)

2. 로컬에서 명령 실행: 로컬에서 히스토리를 읽어오므로 **비행기** 에서도 **커밋(commit)**이 가능하다(!!)
3. 

용어 

1. Commited / Modified / Staged

![image-20190331200825103](/Users/jongsun/Library/Application Support/typora-user-images/image-20190331200825103.png)

2. Local 과 Remote는 다릅니다.

   **Remote 란??** 인터넷이나 네트워크 어딘가에 있는 저장소 (?) == Github 처럼 push하고 pull 할 수 있는 장소

   Q) 그럼 로컬 시스템에 있는 리모트와 네트워크에 있는 리모트는 뭐가 다른건가

   origin : 처음 **리모트**의 이름. 리모트의 URL을 가르키는 포인터? 

   ​	fetch:

   ​	push:

   HEAD : **커밋** 을 가르키는 포인터?

   master: 처음 **브랜치** 의 이름.

   

![image-20190331193502743](/Users/jongsun/Library/Application Support/typora-user-images/image-20190331193502743.png)

처음 파일을 clone 하면 워킹 디렉토리에 tracked & unmodified 상태이다.

Q) 그럼 워킹 디렉토리의 파일을 untracked로 만들고 싶으면 지우는 방법 밖에 없는건가?

A) clone 후에 새 파일을 생성하면 untracked 일 것./ .gitignore 로 해당 형식 무시하는 것도 방법일 듯

modifed 되었어도, stage에 없다면 nothing to commit(=snapshot)이라고 뜰 것. (=add 된게 없다)

3. git diff는 수정했지만, unstaged 인 것들을 가져온다. (difference between modified and staged)
   * Staged 된 것은 보여주지 않는다! Unstaged 만 보여줌 (아니면 git diff --staged)

4. git pull 과 fetch의 차이

pull은 remote repo에서 workspace로 바로 가져오는 것이고,

fetch는 remote repos에서 local repo로 가져오는 것임.

Q) 그럼 local repo와 remote repo 차이가 뭐지??

![image-20190331201929079](/Users/jongsun/Library/Application Support/typora-user-images/image-20190331201929079.png)

5. 파일을 삭제하려면 git rm을 사용하고, commit 해야 한다. git rm 은 staged 상태의 tracked 파일을 지우는 것이다.
   * staged 상태로 만드는 것은 add 뿐만 아니라 rm도 마찬가지!
6. 이름 바꾸기 : git mv from_file to_file
   * 이는 다음의 세줄과 같다
     * mv readme.md readme
     * git rm readme.md
     * git add readme



# 시작

1. git clone으로 이미 만들어져 있는 git 저장소를 가져오는 경우
2. 아직 git으로 버전 관리를 시작하지 않은 로컬 디렉토리를 하나 선택해 git 저장소로 사용하는 방법 (git init으로 .git 스켈레톤 파일 생성)