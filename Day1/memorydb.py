# 메모리기반 학생관리 API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 데이터 형식 지정
class StudentModel(BaseModel) :
    name : str
    age : int
    major : str

#더미 데이터(DB 사용 X)
students =[
    {'id' : 1, "name" : "김철수",'age' : 21, "major" : "인공지능"},
    {'id' : 2, "name" : "이영희",'age' : 22,  "major" : "데이터분석"},
    {'id' : 3, "name" : "성유고",'age' : 25,  "major" : "컴퓨터공학"},
]
@app.get('/')
def read_root():
    return {'message' : 'Hello FastAPI!'}

@app.get('/health')
def get_status():
    return{'message': 'Server is OK!'}

@app.get('/students')
def get_students() :
    return students #위에 선언한 배열을 그대로 출력(돌려줌)

@app.get('/students/{student_id}')
def get_student(student_id : int) :
    for student in students :
        if student['id'] == student_id :
            return student
    # 404 페이지 에러 처리(예외처리)
    raise HTTPException(status_code=404, detail='Student not found')

@app.post('/students')
def create_student(student : StudentModel) :
    new_id = max(item['id'] for item in students) + 1

    new_student = {
        'id' : new_id,
        'name' : student.name,
        'age' : student.age,
        'major' : student.major
        }
    students.append(new_student)
    return students

# 기존 데이터 전체 수정
@app.put('/students/{id}')
def update_student(id: int, student: StudentModel) :
    # update students set ... where id = ~~ ; 와 동일
    for item in students :
        if item['id'] == id :
            item['name'] = student.name
            item['age'] = student.age
            item['major'] = student.major

            return item
    raise HTTPException(status_code=404, detail='Student not found')

# 기존 데이터 일부 수정(잘 사용안함)
@app.patch('/students/{id}')
def patch_student(id: int, student: StudentModel) :
    for item in students :
        if item['id'] == id :
            if student.name is not None :
                item['name'] = student.name
            if student.age is not None :
                item['age'] = student.age
            if student.major is not None :
                item['major'] = student.major

            return item
    raise HTTPException(status_code=404, detail='Student not found')

@app.delete('/students/{id}')
def delete_student(id:int):
    for index, item in enumerate(students):
        if item['id'] == id:
            # students 배열에서 현재 index 의 값만 뽑아냄
            delete_student = students.pop(index)

            return {
                "Message" : 'Student delete',
                'student' : delete_student
            }
    raise HTTPException(status_code=404, detail='Student not found')