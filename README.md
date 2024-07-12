# U.S.EDAP
United States Economy Data Analysis Program

개발 참고 사항 : datetime 형식 : %Y-%m

<h3>프로젝트 요약</h3> :  
미국의 1980년대부터 현재까지의 경제지표 데이터 및 기사를 크롤링하고 데이터를 시각화하여 분석한다. 경제 지표 간의 연관성과 특정한 기간 동안의 기사 키워드를 추출해 경제 지표와 경제 위기 및 경기와의 연관성을 분석 및 해설하고자 한다.  
  
<h3>크롤링 대상</h3> : 
  1. 경제 지표 : Feds 결정금리, CPE 물가지수, 채권(13 week T-bill) 수익률, 주가지수(S%P500), 비트코인, 금 시세 총 6가지 항목  => 이하 각 금리, 물가, 채권, 주가, 비트코인, 금으로 서술한다.
  3. 기사 : 2000-08-18 ~ 현재

<h3>크롤링 사이트</h3> : 
  1. Investing.com : 금리, 물가
  2. Yahoo finanace : 채권, 주가, 비트코인, 금
  3. News Archive : 기사 

<h3>개발환경</h3> 
  1. Colab
  2. 언어 : Python
  3. 크롤링 :
  4. 데이터 시각화 :

<h3>프로젝트 설계도</h3>
StarUml class diagram으로 작성했다.
<img width="500" height="500" scr = "https://github.com/catree42/U.S.EDAP/blob/main/classDiagram_EDAP.png?raw=true"/>



