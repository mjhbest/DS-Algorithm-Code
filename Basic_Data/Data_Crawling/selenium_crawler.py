from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')  # Headless 모드로 실행할 경우 추가


webdriver_service = Service(
    '/Users/owen/Downloads/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=options)
# driver = webdriver.Chrome(
#     '/Users/owen/Downloads/chromedriver_mac_arm64', options=options)

# Google 검색 페이지 열기


driver.get('https://www.google.com')

# 검색어 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Hello, World!')

# 검색 버튼 클릭
search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()

# 결과 출력
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for result in results:
    print(result.text)

# 브라우저 종료
driver.quit()
