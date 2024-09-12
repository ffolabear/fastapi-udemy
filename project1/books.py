from fastapi import FastAPI

app = FastAPI()

# 실행 : uvicorn books:app --reload
# --reload 옵션 줄시 코드 변화가 있을때 마다 자동 리로드
# 혹은 fastapi run books.py
# fastapi run dev books.py 로 실행시 개발모드

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


# 작거나 정적 api 를 앞에 둬야함
@app.get("/api-endpoint")
async def first_api():
    return "{'message': 'Hello fff'}"


@app.get("/books")
async def read_all_books():
    return BOOKS


# 위에서 부터 탐색하기 때문에 아래에 둘 경우 무시됨
# @app.get("/books/mybook")
# async def read_all_books():
#     return {'dynamic_param': 'My favorite book!'}


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    return {'dynamic_param': book_title}


@app.get("/book/{book_title}")
async def read_specific_book(book_title: str):
    for book in BOOKS:
        # casefold() : 소문자 변환
        if book.get('title').casefold() == book_title.casefold():
            return book
