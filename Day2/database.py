# PostgreSQL 데이터베이스 연동 파이썬
import psycopg
from psycopg.rows import dict_row

# 우리가 만드는 함수 정의
def get_connect():
    return psycopg.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'ai_db',
        user = 'postgres',
        password= '123456'
        )