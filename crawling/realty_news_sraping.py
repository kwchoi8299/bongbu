# 다음 부동산 뉴스 스크래핑 하기 
from datetime import datetime
import requests
from bs4 import BeautifulSoup
# import a_auto_posting_tistory
import pymysql

url = "https://realestate.daum.net/news"
res = requests.get(url, verify=False)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml") # beautifulsoup 객체로 만든것이다. 
news_list = soup.find("div", attrs={"class":"section_allnews"}).find_all("li")

# 타이틀과 링크 데이터 담기
news_title_link_list = []


#뉴스 출력
def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (link : {})".format(link))

#다음 뉴스 스크래핑
def scrape_realestate_new():
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        news_title_link_list.append(str(index+1) + ". "+ a_tag.get_text().strip())
        url_link = "\"https:"+a_tag["href"]+'\"'
        news_title_link_list.append("(link : "+ '<a href='+url_link + ' target="_blank">' + url_link +"</a>"+")".strip())

    news_contents = ""
    for i in range(0, len(news_title_link_list), 2):
        news_contents += f"{news_title_link_list[i]}\n{news_title_link_list[i+1]}\n\n"

    return news_contents

# Django 데이터베이스 설정을 사용하여 연결 정보 로드
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'kwchoi8299',
        'PASSWORD': 'rldnjs23!',
        'HOST': '132.226.21.110',
        'PORT': '3306'
    }
}

database_config = DATABASES['default']

def insert_to_db(news_contents):
    # MySQL 데이터베이스 연결 설정
    conn = pymysql.connect(
        host=database_config['HOST'],
        user=database_config['USER'],
        password=database_config['PASSWORD'],
        db=database_config['NAME'],
        port=int(database_config['PORT']),
        charset='utf8'
    )

    # 오늘 날짜를 yyyy-mm-dd 형태로 가져온다.
    today_date = datetime.now().strftime('%Y-%m-%d')
    print(today_date)

    try:
        with conn.cursor() as cursor:

            # 제목에 오늘 날짜 포함해서 문자열 생성
            news_title = f"{today_date} 부동산 주요뉴스"

            # 오늘 날짜와 시간을 datetime(6) 형태로 가져온다.
            now_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print(now_datetime)

            # 뉴스 데이터를 삽입하기 위한 쿼리
            insert_query = "INSERT INTO bongbu_realty_news (title, content, create_date) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (news_title, news_contents, now_datetime))
            conn.commit()
    finally:
        # 데이터베이스 연결 종료
        conn.close()

if __name__ == "__main__":
    # today = datetime.today().strftime('%Y-%m-%d')
    # print("[",today, "부동산 주요뉴스","]")
    
    # 오늘의 부동산 뉴스 스크래핑
    news_contents = scrape_realestate_new()
    print('총 %d건의 뉴스를 수집했습니다.\n' % (len(news_contents) // 2))
    insert_to_db(news_contents)

    # 오토 포스팅 함수 호출 - 타이틀과 링크주소를 함께 넘김
    # a_auto_posting_tistory.writeContent(news_titles, news_links)
    # a_auto_posting_tistory.postContent()