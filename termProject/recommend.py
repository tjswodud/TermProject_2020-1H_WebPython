import os
import io
import sys
import urllib.request
import requests
import re
import webbrowser as wb

class Recommend:
    searchWord = ''
    titleList = []
    linkList = []
    def showUrl(self):
        newSearchWord = self.searchWord + '사용 후기'
        encText = urllib.parse.quote(newSearchWord)
        url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)

        response = urllib.request.urlopen(request)
        responseCode = response.getcode()

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
                    # print(titleResultResponse, '------------ ', str(num), sep=" ")
                    num += 1
                    self.titleList.append(titleResultResponse)

                elif responseBody.startswith(b'"link"'): # link만 추출
                    linkResult = responseBody.decode('utf-8') # 자연어 변환
                    newLinkResult = str(linkResult) # byte - string 변환

                    linkResultResponse = re.sub('<.+?>', '', newLinkResult, 0, re.I|re.S)
                    linkResultResponse = re.sub('"link":', '', linkResultResponse, 0, re.I|re.S)
                    linkResultResponse = re.sub(',', '', linkResultResponse)
                    linkResultResponse = re.sub('"', '', linkResultResponse)
                    linkResultResponse = re.sub('\\\\', '', linkResultResponse)
                    linkResultResponse = linkResultResponse.strip()
                    self.linkList.append(linkResultResponse)
                else:
                    continue
        else:
            print('Error Code:' + responseCode) # Error Code Print

        # usersChoice = int(input('원하는 블로그 후기의 번호를 입력하세요: ')) # user의 선택
        # wb.open(self.linkList[usersChoice - 1]) # Blog Open

        # usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ') # 선택지

"""
        while usersChoice2 != 'n':
            if usersChoice2 == 'y': # 다른 후기도 본다면
                usersChoice = int(input('원하는 블로그 후기의 번호를 입력하세요: ')) # 위 내용 반복
                wb.open(self.linkList[usersChoice - 1])
                usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ') # usersChoice2 초기화
            elif usersChoice2 != 'y' and usersChoice2 != 'n': # 다른 문자를 입력했을 경우
                print('y / n 중에 골라 주십시오.')
                usersChoice2 = input('다른 후기도 보시겠습니까? (y/n) ')
        print('검색을 종료합니다.') # if usersChoice2 == 'n'
"""
