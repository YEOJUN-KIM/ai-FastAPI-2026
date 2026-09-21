# FastAPI

- 실행 속도가 빠르다
- 테스트를 위한 UI를 자동으로 만들어 줌
- Pydantic을 사용, 요청과 응답 데이터를 검증할 수 있다
- PostgreSQL, MySQL, Oracle 등 DB와 연동이 쉽다

### API 서버

클라이언트 요청을 받아 필요한 작업을 수행, 그 결과를 클라이언트에게 돌려주는 프로그램

## 개발환경 설정

### FastAPI 패키지 설치

```bash
pip install fastapi uvicorn
```

- 현재 파이썬에 `fastapi`와 `uvicorn` 패키지를 설치
- C:\Users\User\AppData\Roaming\Python\Python314\Scripts
- sysdm.cpl을 실행 - 고급 - 환경변수
- Path에서 C:\Users\User\AppData\Roaming\Python\Python314\Scripts를 추가
- cmd, VS CODE 재시작

### Fast API 시작

프로젝트 루트(`ai_DB_2026`)에서 터미널을 열고 실행한다.

``` bash
cd FastAPI
python -m uvicorn Main:app --reload --port 8000
```
- 이미 `FastAPI` 폴더에 있다면 `cd FastAPI`는 생략
- `Main:app` : `Main.py` 파일의 `app` 객체를 실행
- `--reload` : 수정되면 곧바로 반영되어서 서버 재시작
- `--port 8000` : 서버를 시작할 포트 지정
- http://127.0.0.1:8000 로 접속

## FastAPI 기본 학습

### 웹 응답코드

- `200 : OK` : 요청이 정상적으로 처리됨
- `404 : Not Found` : 클라이언트가 요청한 페이지나 데이터가 없음
- `500 : Internal Server Error` : 내부 서버 오류

### Swagger UI 확인

- FastAPI에서 자동으로 제공하는 API 문서 및 테스트 페이지
- 위 명령으로 서버를 실행한 상태에서 브라우저로 http://127.0.0.1:8000/docs 에 접속
- `GET /`를 펼치고 `Try it out` → `Execute`를 누르면 API를 테스트할 수 있음
- 현재 코드에서는 응답코드 `200`과 `{"message": "Hello FastAPI"}` 응답을 확인할 수 있음
- 서버를 종료하려면 터미널에서 `Ctrl+C`

참고: [FastAPI 공식 문서 — 첫 단계](https://fastapi.tiangolo.com/tutorial/first-steps/)

### Swagger UI 화면 읽기

- `default` : 별도의 태그를 지정하지 않은 API가 표시되는 기본 그룹
- `GET` : 데이터를 조회할 때 사용하는 HTTP 요청 메서드
- `/` : 요청을 보낼 URL 경로(루트)
- `Read Root` : `read_root()` 함수 이름을 바탕으로 자동 생성된 API 설명 제목

### API 응답과 JSON

- 현재 API는 파이썬 딕셔너리를 반환하고, FastAPI가 이를 JSON 형식으로 변환해서 응답함
- JSON의 문자열과 객체 키는 큰따옴표(`"`)로 표현함
- 파이썬 딕셔너리에서는 문자열에 작은따옴표(`'`)와 큰따옴표(`"`)를 모두 사용할 수 있음

```python
# 파이썬 코드에서 반환하는 딕셔너리
return {'message': 'Hello FastAPI'}
```

```json
{"message": "Hello FastAPI"}
```

### URL 경로

- 기본 구조 : `http(s)://address:port/경로?key=value`
- `address` : `127.0.0.1`, `192.168.0.105` 등의 IP 주소 또는 `www.naver.com`, `google.com` 등의 도메인 주소
- `127.0.0.1` : 현재 사용 중인 내 컴퓨터를 가리키는 주소
- `port` : 포트 번호는 `0~65535` 범위이며, `0`은 예약된 값. 이 실습에서는 `8000` 사용
- `/` : 루트 경로, 기본 페이지
- `/students` : 학생 목록 등의 리소스를 나타내는 경로(REST API 경로 예시)
- `/students/1` : 특정 학생을 나타내는 경로. `/students/{student_id}`로 정의하면 `1`이 경로 파라미터가 됨
- `/?key=value` : `?` 뒤에 쿼리 파라미터를 전달. 여러 개는 `?key=value&name=test`처럼 `&`로 연결
- 위의 `/students` 경로는 설명용 예시이며, 사용하려면 해당 API를 코드에 추가해야 함

### HTTP(S) 메서드

FastAPI에서는 URL 주소와 HTTP 메서드를 함께 파악해야 함. 같은 URL이라도 메서드에 따라 다른 작업을 처리할 수 있음.

| 메서드 | 의미 | 예시 |
| --- | --- | --- |
| `GET` | 데이터 조회 | 학생 목록 조회, 특정 학생 조회 |
| `POST` | 데이터 생성 등 서버에 처리 요청 | 학생 등록 |
| `PATCH` | 데이터 일부 수정 | 학생 전공 수정 |
| `PUT` | 데이터 전체 교체 | 학생 정보 전체 수정 |
| `DELETE` | 데이터 삭제 | 학생 정보 삭제 |

- `POST`는 생성뿐 아니라 API 설계에 따라 수정·삭제 등의 처리에도 사용될 수 있음
- 브라우저 주소창에 URL을 입력해서 접속하면 `GET` 요청이 전송됨
- 이 실습에서는 `POST`, `PUT`, `PATCH`, `DELETE` 요청을 Swagger UI에서 테스트하면 편리함. Postman이나 curl 같은 도구로도 테스트 가능
- Swagger UI에서 해당 메서드를 펼치고 `Try it out` → 필요한 값 입력 → `Execute` 순서로 실행
- HTTPS에서도 HTTP와 동일한 메서드를 사용하며, HTTPS는 통신을 암호화함

### 요청 본문

- 이 실습에서 `POST`나 `PATCH` 요청 시 클라이언트는 등록하거나 수정할 데이터를 JSON 형식의 요청 본문(body)에 담아 서버에 전달함
- FastAPI에서는 Pydantic 패키지의 모델(`BaseModel`)을 사용해 요청 본문의 데이터 구조를 정의하고 값을 검증할 수 있음
- JSON에서는 파이썬의 `None` 대신 `null`을 사용함
- JSON의 객체 키와 문자열은 큰따옴표(`"`)로 작성함
- JSON에서는 마지막 항목 뒤에 쉼표(`,`)를 붙일 수 없음. `}` 또는 `]`를 닫기 전 마지막 쉼표를 제거해야 함(파이썬에서는 허용)

```json
{
  "name": "홍길동",
  "major": null
}
```

### HTTPException

- API 처리 중 오류가 발생하면 예외 처리를 통해 클라이언트에 오류 상태코드와 내용을 전달함
- FastAPI에서는 `raise HTTPException(status_code=..., detail=...)`으로 오류 응답을 보낼 수 있음
- 아래 표의 `200`, `201`은 예외가 아닌 정상 처리 상태코드임

| 상태코드 | 의미 |
| --- | --- |
| `200 OK` | 요청 성공 |
| `201 Created` | 데이터 생성 성공 |
| `403 Forbidden` | 접근 권한 없음 |
| `404 Not Found` | 요청한 데이터나 경로가 없음 |
| `500 Internal Server Error` | 서버 내부 오류 |
