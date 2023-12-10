"""The dashboard page."""
from reflex_python.templates import template

import reflex as rx
import requests


# NEWS API: https://newsapi.org/s/new-zealand-news-api
# pip3 install requests
response = requests.get("https://newsapi.org/v2/top-headlines?country=nz&apiKey=113b00adf8724c22a70cb6c95b61e44e")
print(response)
data = response.json()
print(data)

"""
대부분의 Web API 는 Web URL 모양으로 "설계"가 되어있다.
"링크URL" 을 조금 분석해보자. 참고: https://blog.hubspot.com/marketing/parts-url


GET: https://newsapi.org/v2/top-headlines?country=nz&apiKey=113b00adf8724c22a70cb6c95b61e44e
➡️ Path: v2/top-headlines
➡️ Query: ?country=nz&apiKey=113b00adf8724c22a70cb6c95b61e44e
"규칙" 이기 때문에, API 마다 다르다.
하지만, 일반적으로, RESTful API 는 규칙을 공유하고 있다.
우리가 사용하고 있는 공식문서: https://newsapi.org/docs


[CRUD - CREATE / READ / UPDATE / DELETE: 모든 프로그램이 갖고있는 성질]
GET: 은 데이터를 요청하고 response 를 "받기만 한다!" 
POST: 는 데이터를 보내서 (서버 안에 있는 DB 에) "새 데이터를 생성한다"
PUT: 는 데이터를 보내서 (서버 안에 있는 DB 에) 기존 데이터를 요청한 데이터로 "수정"한다.
DELETE: 요청한 대상을 (서버에서) 지운다.
"""



@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Alvin's website", font_size="3em"),
        rx.text("Welcome to News Page!"),
        rx.text("You can edit this page in ",rx.code("{your_app}/pages/dashboard.py"),),
    )
