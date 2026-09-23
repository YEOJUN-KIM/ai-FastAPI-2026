from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 우리가 만든 database파일
from database import get_connect
from psycopg.rows import dict_row

app = FastAPI(title = 'FastAPI DB 연동')

# 학생 모델
class StudentModel(BaseModel) :
    name : str
    email : str | None = None   # DB에  null허용
    age : int | None = None
    major : str

# 전체학생 조회
@app.get('/students')
def get_student() :
    # 실제 DB 연결
    conn = get_connect()
    cursor = conn.cursor(row_factory=dict_row) # 마우스커서처럼 테이블 한행씩 가르키는 값

    try:    #실제 쿼리는 DBeaver 등에서 작성 확인하고 복사하는게 좋음
        cursor.execute("""
            select id, name, email, age, major, created_at
            from students
            order by id
        """)

        #위 쿼리를 실행 후 데이터를 가져와 students에 할당
        students = cursor.fetchall()
        if not students:
            raise HTTPException(status_code=404, detail='Students no found')
        
        return students
    
    #except Exception: #예외

    finally: #예외 여부 관계없이 마지막에 항상 실행
        cursor.close()
        conn.close()    #쿼리 실행 후 커서와 DB연결을 종료

# 특정조회
@app.get('/students/{id}')
def get_student(id:int) :
    conn = get_connect()
    cursor = conn.cursor(row_factory=dict_row) 
    
    try:
        # 쿼리 실행, 외부에서 받은 값은 %s로 변경, 값은 (id, ) 형식으로 작성
        cursor.execute("""
            select id, name, email, age, major, created_at
            from students
            where id = %s
        """,(id,))
    
        student = cursor.fetchone() # 커서에서 1건만 가져옴
        # 쿼리가 가져오지 못하면(특정 학생이 없다면)
        if not student:
            raise HTTPException(status_code=404, detail='Student no found')
        return student
        
    finally: 
        cursor.close()
        conn.close()  #위 연결과 반대의 순서로 close    ex) a.conn, b.conn -> b.close, a.close

# 학생등록
@app.post('/students')
def create_student(student : StudentModel):
    conn = get_connect()
    cursor = conn.cursor(row_factory=dict_row)
    try:
        cursor.execute("""
            insert into students (name, email, age, major)
            values (%s, %s, %s, %s)
        """,(student.name,student.email,student.age,student.major))

        #new_student = cursor.fetchone()  
        conn.commit()

        #return new_student
        return {"message": "학생 등록 완료"}
    
    except:
        conn.rollback()
        raise
    finally:
        cursor.close() 
        conn.close()    

# 학생수정
@app.put('/students/{id}')
def update_student(id:int, student: StudentModel):
    pass


# 학생삭제
@app.delete('/students/{id}')
def delete_student(id:int):
    pass


