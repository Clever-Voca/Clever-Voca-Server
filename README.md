# Clever-Voca-Server

### 모듈 설치
pip install -r requirements.txt

### 서버 실행
1. 파일을 클론이나 다운 후 파일에다가 넣어놓는다.
2. 해당 경로로 찾아가 src/config.ini를 만들어준다.
    - MySQL DB_URL을 넣어주면 된다.
    % 유의사항 %
    (1. MySQL이 깔려있어야한다.
     2. DB이름을 CV로 해서 생성해주어야한다.
     3. mysql://root:[DB비번]@localhost:3306/[DB이름]?charset=utf8
        이런식으로 mysql DB_URL을 작성해주어야한다.
        utf-8 필수)
    ```ini
        [default]
        DB_URL = "your MYSQL DB URL"
        PORT = "you will write youn want port number"
    ```
3. 실행을 해준다.
    - python src/main.py -R(Reload option) -P (Port number)
        - 이때 -R이나 -P는 옵션이니 안넣어줘도 된다.    

## API명세서

1. `POST /api/module`
    module을 생성합니다.
    - request
    ```json
    {
        "module_name": "string",
        "publisher": "string",
        "word": [
            {
            "word": "string",
            "mean": "문장"
            }
        ]
    }
    ```
    - response
    ```json
    {
        "module": {
            "module_name": "string",
            "publisher": "string",
            "module_id": 39,
            "created_at": "2020-12-22T15:52:18"
        },
        "word": [
            {
                "word": "string",
                "module_id": 39,
                "mean": "문장",
                "word_id": 25
            },
            {
                "word": "word",
                "module_id": 39,
                "mean": "단어",
                "word_id": 2
            }
        ]
    }
    ```

2. `GET /api/module/search?search={search}`
    모듈을 검색합니다, search에 아무것도 안넣으면 기본적으로 `""`
    - request
    ```json
    search : 검색할 값
    ```

    - response
    ```json
    [
        {
            "created_at": "2020-12-22T16:00:12",
            "module_name": "string",
            "publisher": "string",
            "module_id": 1
        }
    ]
    ```

3. `GET /api/module/{id}`
    모듈을 가져옵니다.
    - request
    ```json
    id : module_id
    ```

    - response
    ```json
    {
        "module": [
            {
                "created_at": "2020-12-22T16:00:12",
                "module_name": "string",
                "publisher": "string",
                "module_id": 1
            }
        ],
        "word": [
            {
                "word": "string",
                "module_id": 1,
                "mean": "문장",
                "word_id": 1
            },
            {
                "word": "word",
                "module_id": 1,
                "mean": "단어",
                "word_id": 2
            }
        ]
    }
    ```
