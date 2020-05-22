# 전체적인 디자인 개선 (글꼴, 버튼 위치 등)
# 검색 시 검색 버튼 + Enter으로 동작되도록 개선
# 검색 결과 중 URL에 버튼 기능 추가 (버튼 동작은 추후 Update 예정)

import os
import sys
import urllib.request
import requests
import re
import tkinter as tk
import tkinter.font
import webbrowser as wb

window = tk.Tk()
basicFont = tkinter.font.Font(family = "Do Hyeon", size = 20)
resultFont = tkinter.font.Font(family = "Do Hyeon", size = 15)
window.title('제품 추천 프로그램')
window.geometry('640x400+100+100')
window.resizable(True, True)

def enterProcess(event):
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
       responseBodys = response.readlines()
       rowNumber = 4
       for responseBody in responseBodys:
           if responseBody.startswith(b'"title"'): # title만 추출
               titleResult = responseBody.decode('utf-8') # 자연어로 변환
               newTitleResult = str(titleResult) # byte - string 변환
            
               # 불필요한 문자열, 태그 제거          
               titleResultResponse = re.sub('<.+?>', '', newTitleResult, 0, re.I|re.S)
               titleResultResponse = re.sub('"title":', '', titleResultResponse, 0, re.I|re.S)
               titleResultResponse = re.sub(',', '', titleResultResponse)
               titleResultResponse = re.sub('"', '', titleResultResponse)

               l4 = tk.Label(window, text = titleResultResponse.strip(), font = resultFont, foreground = '#C40000')
               l4.grid(row=rowNumber, column=0)
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
               linkResultResponse = linkResultResponse.strip()
            
               # l4 = tk.Button(window, text = linkResultResponse.strip(), font = resultFont, relief = 'solid', command = urlOpen(linkResultResponse))
               l4 = tk.Button(window, text = linkResultResponse, font = resultFont, relief = 'solid')
               l4.grid(row=rowNumber, column=0)
               
               rowNumber = rowNumber + 1
           else:
               continue
   else:
       l6 = tk.Label(window, text = 'Error Code:' + responseCode, font = resultFont)
       l6.grid(row=1, column=2)

def buttonProcess():
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
        responseBodys = response.readlines()
        rowNumber = 4
        for responseBody in responseBodys:
            if responseBody.startswith(b'"title"'): # title만 추출
                titleResult = responseBody.decode('utf-8') # 자연어로 변환
                newTitleResult = str(titleResult) # byte - string 변환
            
                # 불필요한 문자열, 태그 제거          
                titleResultResponse = re.sub('<.+?>', '', newTitleResult, 0, re.I|re.S)
                titleResultResponse = re.sub('"title":', '', titleResultResponse, 0, re.I|re.S)
                titleResultResponse = re.sub(',', '', titleResultResponse)
                titleResultResponse = re.sub('"', '', titleResultResponse)

                l4 = tk.Label(window, text = titleResultResponse.strip(), font = resultFont, foreground = '#C40000')
                l4.grid(row=rowNumber, column=0)
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
                linkResultResponse = linkResultResponse.strip()
            
                # l4 = tk.Button(window, text = linkResultResponse.strip(), font = resultFont, relief = 'solid', command = urlOpen(linkResultResponse))
                l4 = tk.Button(window, text = linkResultResponse, font = resultFont, relief = 'solid')
                l4.grid(row=rowNumber, column=0)
                rowNumber = rowNumber + 1
            else:
                continue
    else:
        l6 = tk.Label(window, text = 'Error Code:' + responseCode, font = resultFont)
        l6.grid(row=1, column=2)

'''
def urlOpen(link):
    wb.open(link)
'''

t1 = tk.Label(window, text = '원활한 쇼핑을 위한 추천 서비스', relief = 'solid', background= 'yellow', font = basicFont)
t1.grid(row = 0, column = 0)

e1 = tk.Entry(window) # 검색 창
e1.bind('<Return>', enterProcess)
e1.grid(row = 1, column = 0)
b1 = tk.Button(window, text = "검색", font = basicFont, command = buttonProcess) # 검색 버튼
b1.grid(row = 1, column = 1)
l1 = tk.Label(window, text = '')
l2 = tk.Label(window, text = '결과:', font = basicFont) # 결과 출력
l2.grid(row = 2, column = 0)

client_id = "MxAYTCOsbligdEvHngib"
client_secret = "3iRpVzgyLb"

window.mainloop()
