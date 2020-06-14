# recommend.py / shopping.py Class로 변환, import
# 각 클래스의 메소드를 함수로 선언

import recommend
import shopping

productRecommend = recommend.Recommend()
productRecommend.client_id = "MxAYTCOsbligdEvHngib"
productRecommend.client_secret = "3iRpVzgyLb"

print('----------원활한 쇼핑을 위한 제품 추천 서비스----------')
productRecommend.searchWord = input('검색어를 입력하세요: ')

productRecommend.showUrl()

shoppingSite = shopping.Shopping()
shoppingSite.client_id = "MxAYTCOsbligdEvHngib"
shoppingSite.client_secret = "3iRpVzgyLb"

shoppingSite.finalProduct = input('쇼핑 사이트에서 찾고자 하는 제품의 제품명을 위 제목에서 복사-붙여넣기 해주세요: ')

shoppingSite.goToShopSite()

print('즐거운 쇼핑 되십시오. 프로그램을 종료합니다.')
