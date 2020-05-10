import os
import sys
import urllib.request
import requests
import re
import tkinter as tk

window = tk.Tk()
window.title('제품 추천 프로그램')

def process():
    searchWord = e1.get()
    newSearchWord = searchWord + '후기'
    encText = urllib.parse.quote(newSearchWord)
    url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    responseCode = response.getcode()
    if responseCode == 200:
        l3 = tk.Label(window, text = "------------------Crawling Result-----------------")
        l3.grid(row=1, column=2)
        
        responseBodys = response.readlines()
        rowNumber = 2
        for responseBody in responseBodys:
            if responseBody.startswith(b'"title"'): # title만 추출
                titleResult = responseBody.decode('utf-8') # 자연어로 변환
                newTitleResult = str(titleResult) # byte - string 변환
            
                # 불필요한 문자열, 태그 제거          
                titleResultResponse = re.sub('<.+?>', '', newTitleResult, 0, re.I|re.S)
                titleResultResponse = re.sub('"title":', '', titleResultResponse, 0, re.I|re.S)
                titleResultResponse = re.sub(',', '', titleResultResponse)
                titleResultResponse = re.sub('"', '', titleResultResponse)

                l4 = tk.Label(window, text = titleResultResponse.strip())
                l4.grid(row=rowNumber, column=2)
                rowNumber = rowNumber + 1
            elif responseBody.startswith(b'"link"'): # link만 추출
                linkResult = responseBody.decode('utf-8') # 자연어로 변환
                newLinkResult = str(linkResult) # byte - string 변환
            
                # 불필요한 문자열, 태그 제거
                linkResultResponse = re.sub('<.+?>', '', newLinkResult, 0, re.I|re.S)
                linkResultResponse = re.sub('"link":', '', linkResultResponse, 0, re.I|re.S)
                linkResultResponse = re.sub(',', '', linkResultResponse)
                linkResultResponse = re.sub('"', '', linkResultResponse)
                linkResultResponse = re.sub('\\\\', '', linkResultResponse)
            
                l4 = tk.Label(window, text = linkResultResponse.strip())
                l4.grid(row=rowNumber, column=2)
                rowNumber = rowNumber + 1
            else:
                continue
            
        l5 = tk.Label(window, text = '--------------------------------------------------')
        l5.grid(row=rowNumber + 1, column=2)
    else:
        l6 = tk.Label(window, text = 'Error Code:' + responseCode)
        l6.grid(row=1, column=2)

e1 = tk.Entry(window)
e1.grid(row=1, column=1)
b1 = tk.Button(window, text = "검색", command = process)
b1.grid(row=2, column=1)
l1 = tk.Label(window, text = '')
l2 = tk.Label(window, text = '결과:')
l2.grid(row=1, column=2)

client_id = "MxAYTCOsbligdEvHngib"
client_secret = "3iRpVzgyLb"

window.mainloop()
