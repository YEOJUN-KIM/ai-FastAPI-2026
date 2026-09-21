# 파이썬에서 다른 패키지를 사용하려면
# from * import **
# import *

from fastapi import FastAPI
import fnc_test
app = FastAPI()

@app.get('/')
def read_root() :
    fnc_test.sayHello("홍길동")
    return {'message' : 'Hello FastAPI'}

@app.get('/students')
def get_students() :
    return [
        {'id' : 1, "name" : "김철수", "major" : "인공지능"},
        {'id' : 2, "name" : "이영희", "major" : "데이터분석"},
        {'id' : 3, "name" : "성유고", "major" : "컴퓨터공학"},
        ]

@app.get('/stduents/{id}')
def get_students(id : int) :
    return{'student_id' : id}