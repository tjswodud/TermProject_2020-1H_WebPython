import os
import sys
import urllib.request
import requests
import re

client_id = "secret"
client_secret = "secret"

searchWord = input("검색할 단어를 입력하세요: ")
newSearchWord = searchWord + '후기'

encText = urllib.parse.quote(newSearchWord)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
responseCode = response.getcode()
if responseCode == 200:
    print('------------------Crawling Result-----------------')
    responseBodys = response.readlines()
    for responseBody in responseBodys:
        if responseBody.startswith(b'"title"'): # title만 추출
            titleResult = responseBody.decode('utf-8') # 자연어로 변환
            newTitleResult = str(titleResult) # byte - string 변환
            
            # 불필요한 문자열, 태그 제거          
            titleResultResponse = re.sub('<.+?>', '', newTitleResult, 0, re.I|re.S)
            titleResultResponse = re.sub('"title":', '', titleResultResponse, 0, re.I|re.S)
            titleResultResponse = re.sub(',', '', titleResultResponse)
            titleResultResponse = re.sub('"', '', titleResultResponse)
            
            print(titleResultResponse.strip()) # 출력
        elif responseBody.startswith(b'"link"'): # link만 추출
            linkResult = responseBody.decode('utf-8') # 자연어로 변환
            newLinkResult = str(linkResult) # byte - string 변환
            
            # 불필요한 문자열, 태그 제거
            linkResultResponse = re.sub('<.+?>', '', newLinkResult, 0, re.I|re.S)
            linkResultResponse = re.sub('"link":', '', linkResultResponse, 0, re.I|re.S)
            linkResultResponse = re.sub(',', '', linkResultResponse)
            linkResultResponse = re.sub('"', '', linkResultResponse)
            linkResultResponse = re.sub('\\\\', '', linkResultResponse)
            
            print(linkResultResponse.strip())
            print()
        else:
            continue
            
    print('--------------------------------------------------')
else:
    print('Error Code:' + responseCode)
