from selenium import webdriver
from selenium.webdriver.common.keys import Keys ## web crowing = web 페이지 데이터 가져오기 !1). 조작 시나리오 확인
from selenium.webdriver.common.by import By
import time

url = 'https://www.google.co.kr/' ## (2) selenium 코드 > 1. 접속할 사이트 지정 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb') ## 2. 페이지 내에서 데이터 접근 or 검색 실행
search_box.send_keys('KBO 한국시리즈')                         ##  페이지 내 엘리먼트 조작 (#AAPjFqb) > 엘리먼트 찾기
search_box.send_keys(Keys.RETURN)                             ## 마우스, 키 입력
time.sleep(20)
