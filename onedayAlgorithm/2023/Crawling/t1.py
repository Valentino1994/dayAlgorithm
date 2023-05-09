from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

def findEveryLink():
    result = {"category": [], "link": [], "contact": [], "title": []}

    page_num = 1
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    while page_num < 3:
        # link = f'https://www.mule.co.kr/bbs/info/recruit?page={page_num}&userid=&isAdmin=false&isPartner=false&of=wdate&od=desc&'
        job_link = f'https://www.mule.co.kr/bbs/info/recruit?page={page_num}&map=list&mode=list&region=&start_price=&end_price=&qf=title&qs=&category=%EB%A9%A4%EB%B2%84%EA%B5%AC%EC%A7%81&ct1=&ct2=&ct3=&store=&options=&soldout=&sido=&gugun=&dong=&period=6&of=wdate&od=desc&userid=&isAdmin=false&isPartner=false&'
        # band_link = f'https://www.mule.co.kr/bbs/info/recruit?page={page_num}&map=list&mode=list&region=&start_price=&end_price=&qf=title&qs=&category=%EB%A9%A4%EB%B2%84%EA%B5%AC%EC%9D%B8&ct1=&ct2=&ct3=&store=&options=&soldout=&sido=&gugun=&dong=&period=6&of=wdate&od=desc'
        driver.get(job_link)
        elements = driver.find_elements(By.CSS_SELECTOR, "#board > div.board-list-wrapper.cf > table > tbody > tr")
        our_category = ["멤버구인", "멤버구직"]
        for element in elements:
            category = element.find_elements(By.CSS_SELECTOR, "td")
            for cat in category:
                if cat.text in our_category:
                    next = element.find_element(By.CSS_SELECTOR, "td > a")
                    next_link = next.get_attribute("href")
                    if next.text not in result["title"]:
                        result["category"].append(cat.text)
                        result["link"].append(next_link)
                        result["title"].append(next.text)

        page_num += 1

    return result

every_link = findEveryLink()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# contact_case = ["카톡", "KAKAO", "kakao", "@",
#                 "010", "01공", "01영", "0일0", "영10", "공10",
#                 "0일공", "0일영", "공1영", "공1공", "영일0", "공일0",
#                 "공일공", "공일영", "영일공", "영일영"]
#
# # link를 각각 열어보면서 crawling을 시작함
for i in range(len(every_link["link"])):
    now_link = every_link["link"][i]
    driver.get(now_link)

    try:
        # link에 들어갔을 때 연락처 보기 버튼이 있는 경우 -> click, sleep(2)
        contact_button = driver.find_element(By.CSS_SELECTOR, "#tel-number > div.value.pointer.phoneEncode")
        contact_button.click()
        time.sleep(3)
        contact_element = driver.find_element(By.CSS_SELECTOR, "#tel-number > div.value.phoneDecode")
        every_link["contact"].append(contact_element.text.split(" ")[0])

    except:
        every_link["contact"].append("X")
#         # 연락처 저장 -> 모든 div 태그와 span 태그 모두 모음, 각자 텍스트마다 case가 있음.
#         # every_div = driver.find_elements(By.CSS_SELECTOR, "div")
#         # every_span = driver.find_elements(By.CSS_SELECTOR, "span")
#         # for div in every_div:
#         #     for case in contact_case:
#         #         if case in div.text:
#         #             print(div.text)
#         #
#         # for span in every_span:
#         #     for case in contact_case:
#         #         if case in span.text:
#         #             print(span.text)


inventors = pd.DataFrame(every_link)
inventors.to_excel("fromMember0407.xlsx", index=False)