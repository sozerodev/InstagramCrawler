# 인스타그램 본문 수집하기
from selenium import webdriver
import time

# 사용자에게 어떤 해시태그를 검색할지 입력어 받기
SearchKey = input("어떤 검색어에 대해 알고싶은가요?: ")
    # 한글로 하면 에러가 남... 왜일까.
    # 영어로 검색할때보다 한글로 검색할때 로딩시간이 더 길어지기 떄문.
HowMany = int(input("몇 개의 포스팅을 수집하고싶은가요? : "))
print("\n"+ SearchKey+"에 대해 알아보겠습니다.", end="\n"+"-"*50+"\n\n")

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

# 2. 인스타그램 사이트 접속
driver.get("https://www.instagram.com/explore/tags/"+SearchKey+"/")

# SearchKey가 영어일때보다 한글일때 로딩되는 시간이 더 길다.
# 또, 수집하는 포스팅의 갯수가 많을수록 기다리는 시간을 조금 늘려야 한다.
time.sleep(5) # 따라서 이게 없거나 너무 짧을 경우에는 에러가 발생할 수 있다.

login_close = driver.find_element_by_css_selector("button.dCJp8")
login_close.click()

# 3. 사이트 결과 확인
# 컨테이너 : div.v1Nh3
instagrams = driver.find_elements_by_css_selector("div.v1Nh3")

instagrams = instagrams[:HowMany]
time.sleep(5)

nth = 1
for instagram in instagrams:
    # url = album.attrs["href"]
    # driver.get("https://www.instagram.com/"+url)  로 시도하려 하였으나.. driver에는 attrs요소가 없어서 이렇게 이동 못함
    # 위의 주석처리된 방법은 뷰티풀솦에서만.

    instagram.click()

    # 사이트 접속 후 로딩 시간 기다리기
    time.sleep(2)

    # 본문 내용 수집
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(nth,"번째 포스트","="*30)
    nth += 1
    print(post, end="\n\n")

    close_button = driver.find_element_by_css_selector("button.ckWGn")
    close_button.click()

print("\n\n"+"-"*40)
print(SearchKey+"에 대한 수집을 마쳤습니다. ^--^")