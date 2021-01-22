# pandas == panel datas (패널 자료)
# numpy 기반으로 만들어졌으며 데이터 분석을 위한 효율적인 데이터 구조를 제공
# 1차원 배열 - Series
# 2차원 배열 - DataFrame


import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
# read_html() 웹 페이지에서 테이블 형태의 데이터를 추출하는 함수

summer = df[1].iloc[:,:5]   # 모든 행에 대해, 앞에서 5개의 열 슬라이싱
summer.columns = ['경기수', '금', '은', '동', '계']

# 금메달 기준으로 정렬
print(summer.sort_values('금', ascending=False))

summer.to_excel('하계올림픽메달.xlsx')