# 파이썬에서 다른 패키지를 사용하려면
# from * import **
# import *

from fastapi import FastAPI
from pydantic import BaseModel

import Day1.fnc_test as fnc_test

app = FastAPI()

# 클래스 : 함수의 변형. 현재는 데이터 구조만
# 데이터 제대로 입력 검증
class StudentModel(BaseModel):
    name : str
    email : str
    age : int
    major : str | None = None

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

@app.get('/search')
def search_student(major: str | None = None) :
    return{"major" : major}

@app.post('/students/{id}')
def create_students(student : StudentModel):
    return{'message': '학생등록',
           'data' : student
           }

@app.patch('/students/{id}')
def update_student(id:int):
    return { 'message' : f'{id}번 학생 수정'}

@app.delete('/students/{id}')
def delete_student(id:int):
    return { 'message' : f'{id}번 학생 삭제'}