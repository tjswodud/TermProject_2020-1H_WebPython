# 기존 계획(Naver Shopping API 활용) 폐지, webbrowser 모듈 활용, url open에 집중
# User가 후기를 본 후 제품명을 입력하면, 해당 제품의 Naver Shopping 사이트로 연결

import io
import os
import sys
import requests
import urllib.request
import re
import webbrowser as wb

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Shopping:
    def goToShopSite(self):
        url = 'https://search.shopping.naver.com/search/all?query=' + self.finalProduct

        wb.open(url)

        userChoice = input('다른 결과가 필요하시다면 제품명을 입력해 주세요 (제품명 or Exit): ')

        while userChoice != 'Exit':
            url = 'https://search.shopping.naver.com/search/all?query=' + userChoice
            wb.open(url)
            userChoice = input('다른 결과가 필요하시다면 제품명을 입력해 주세요 (제품명 or Exit): ')
