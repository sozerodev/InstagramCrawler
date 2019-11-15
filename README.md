# Instagram Crawler
crawler.py를 실행시키기 전에 같은 로컬의 폴더에 자신의 chrome버전과 맞는 `chromedriver`를 다운받아야 한다. 

- 여기서 [다운로드](http://chromedriver.chromium.org/downloads)

### screenshot
![screenshot](./img/screen.png)

### Issue
1.
    - URL을 통한 태그 검색을 할때, SearchKey(검색어)가 영어일때보다 한글일때 로딩되는 시간이 더 길다.
    - 또, 수집하는 포스팅의 갯수가 많을수록 기다리는 시간을 조금 늘려야 한다.
    > 따라서 `time.sleep()`함수를 통해 기다리는 시간을 늘려야 한다. 


