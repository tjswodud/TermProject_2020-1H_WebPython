# tkinter 모듈 제거, 잠시 gui 구현 중단
# User의 선택으로 후기 블로그 url에 접속할 수 있도록 구현함.
# 반복문, 조건문으로 다른 후기도 볼 것인지 물어보고, 다시 선택이 가능하도록 구현함.
# 프로그램 종료 구현
# Editor : Changed from Python IDLE -> Atom Editor

import os
import io
import sys
import urllib.request
import requests
import re
import webbrowser as wb

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

client_id = "MxAYTCOsbligdEvHngib"
client_secret = "3iRpVzgyLb"

print('----------원활한 쇼핑을 위한 제품 추천 서비스----------')
searchWord = input('검색어를 입력하세요: ')
newSearchWord = searchWord + '구매 후기'
encText = urllib.parse.quote(newSearchWord)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
responseCode = response.getcode()

titleList = []
linkList = []
num = 1

if responseCode == 200:
    responseBodys = response.readlines()

    for responseBody in responseBodys:
        if responseBody.startswith(b'"title"'): # title만 추출
            titleResult = responseBody.decode('utf-8') # 자연어 변환
            newTitleResult = str(titleResult) # byte - string 변환

            titleResultResponse = re.sub('<.+?>', '', newTitleResult, 0, re.I|re.S)
            titleResultResponse = re.sub('"title":', '', titleResultResponse, 0, re.I|re.S)
            titleResultResponse = re.sub(',', '', titleResultResponse)
            titleResultResponse = re.sub('"', '', titleResultResponse)
            print(titleResultResponse, '------------ ', str(num), sep=" ")
            num += 1
            titleList.append(titleResultResponse)

        elif responseBody.startswith(b'"link"'): # link만 추출
            linkResult = responseBody.decode('utf-8') # 자연어 변환
            newLinkResult = str(linkResult) # byte - string 변환

            linkResultResponse = re.sub('<.+?>', '', newLinkResult, 0, re.I|re.S)
            linkResultResponse = re.sub('"link":', '', linkResultResponse, 0, re.I|re.S)
            linkResultResponse = re.sub(',', '', linkResultResponse)
            linkResultResponse = re.sub('"', '', linkResultResponse)
            linkResultResponse = re.sub('\\\\', '', linkResultResponse)
            linkResultResponse = linkResultResponse.strip()
            linkList.append(linkResultResponse)
        else:
            continue
else:
    print('Error Code:' + responseCode)

usersChoice = int(input('원하는 블로그 후기의 번호를 입력하세요: ')) # user의 선택
wb.open(linkList[usersChoice - 1])

usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ')

while usersChoice2 != 'n':
    if usersChoice2 == 'y':
        usersChoice = int(input('원하는 블로그 후기의 번호를 입력하세요: '))
        wb.open(linkList[usersChoice - 1])
        usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ')
    elif usersChoice2 != 'y' and usersChoice2 != 'n':
        print('y / n 중에 골라 주십시오.')
        usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ')
    elif usersChoice2 == 'n':
        print('프로그램을 종료합니다.')

print('프로그램을 종료합니다.')
