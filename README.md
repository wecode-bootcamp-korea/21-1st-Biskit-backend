![스크린샷 2021-06-20 오후 3 56 59](https://user-images.githubusercontent.com/73716178/122665086-3a8b0180-d1e0-11eb-8ac0-064b0fcfa6ab.png)

# Biskit front-end team 입니다!
요리키트를 판매하는 이커머스 플랫폼인  [CJ COOKIT](https://www.cjcookit.com/pc/main) 클론 프로젝트

# 프로젝트 소개
- 📢준비된 식재료로 만든 요리키트를 판매하는 사이트인 CJ 쿡킷 사이트를 클론한 **"biskit(비스킷)"** 프로젝트

## 프로젝트 계획 및 기간
📆 2021.6.7 ~ 6.18
- 필수적으로 구현하기로 한 사항 : 회원가입, 로그인, 전체 상품페이지 리스트, 상품별 상세페이지, 장바구니
- 추가적으로 구현 된 사항 : 상품 검색(프론트앤드는 미구현)

## 페이지별 기능 Demo
### [회원가입]
![비스킷 회원가입](https://user-images.githubusercontent.com/73716178/122664662-bfc0e700-d1dd-11eb-90c0-1488e700f75d.gif)
### [로그인/로그아웃]
![비스킷 로그인:로그아웃](https://user-images.githubusercontent.com/73716178/122664543-17128780-d1dd-11eb-8b9d-5ab11fa72bec.gif)
### 메인 배너 슬라이드
![메인리뷰슬라이드](https://user-images.githubusercontent.com/73716178/122664644-9c963780-d1dd-11eb-8caa-6855bd334c8b.gif)
### [제품 상세 페이지]
![비스킷 제품상세페이지](https://user-images.githubusercontent.com/73716178/122664656-af107100-d1dd-11eb-8997-97fb06401656.gif)
### [메뉴 리스트]
![비스킷 메뉴리스트](https://user-images.githubusercontent.com/73716178/122664658-b46dbb80-d1dd-11eb-966e-baadd6be4c96.gif)
### [장바구니 기능 구현]
![비스킷 장바구니](https://user-images.githubusercontent.com/73716178/122664783-61e0cf00-d1de-11eb-8fbc-4491bee09b18.gif)

### Biskit Demo 유튜브 링크
<a href="https://www.youtube.com/watch?v=SE_5vtrBrsg">
    <img src="http://img.shields.io/badge/-YouTube-FF0000?style=flat&logo=YouTube&link=https://https://www.youtube.com/watch?v=SE_5vtrBrsg/"
        style="height : auto; margin-left : 10px; margin-right : 10px;"/>
</a>

## 구현 기능 상세

#### Users app

- `bcrypt`를 이용한 비밀번호 암호화 기능 구현
- `PyJWT`를 이용해 로그인시 JWT 발급 기능 구현
- 정규표현식을 사용한 유효성 검사 기능 구현

#### Products app
- 쿼리파라미터를 사용해 카테고리별, 정렬, 페이지네이션 기능 구현
- 상품별 리뷰 등 상세정보 제공 기능 구현
- 상품 검색 기능 구현

#### Orders app
- 장바구니 추가, 삭제, 선택삭제 기능 구현
- 각 사용자별 장바구니 목록 기능 구현
- `transaction`을 이용해 결과가 무결성을 가지도록 구현

## 🛠 사용한 기술

Front-End :<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white"/></a> <img src="https://img.shields.io/badge/React_Router-CA4245?style=flat-square&logo=ReactRouter&logoColor=white"/></a> <img src="https://img.shields.io/badge/SCSS-CC6699?style=flat-square&logo=SASS&logoColor=white"/></a> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a>

Back-End : <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/></a> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></a> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=JSONWebTokens&logoColor=white"/></a>

## 🛠 사용한 툴

Common : <img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white"/></a> <img src="https://img.shields.io/badge/Trello-0052CC?style=flat-square&logo=Trello&logoColor=white"/></a> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white"/></a> <img src="https://img.shields.io/badge/PostMan-FF6C37?style=flat-square&logo=PostMan&logoColor=white"/></a>

## 👥 팀원

- 프론트 : [권오현](https://github.com/im667), [신미영](https://github.com/smy0102), [전건우](https://github.com/fghjjkl32) (비스킷 프론트앤드팀 [깃허브](https://github.com/wecode-bootcamp-korea/21-1st-Biskit-frontend))
- 벡엔드 : [김민규](https://github.com/SkyStar-K), [박창현](https://github.com/chp9419), [송준](https://github.com/riassuc), [이아란](https://github.com/araaaaan)
 

## Reference
이 프로젝트는 [쿡킷(COOKIT)](https://www.cjcookit.com/pc/main) 사이트를 참조하여 학습목적으로 만들었습니다.
실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
