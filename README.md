# 설치 방법
1. 터미널에 입력: 
    - cd weerobot
    - alembic init migrations
    - alembic.ini 파일에서 sqlalchemy.url = sqlite:///./weerobot.db 로 수정
    - /migrations.env 파일에서 
        - import models 추가
        - target_metadata = models.Base.metadata 수정
    - alembic revision --autogenerate
    - alembic upgrade head
2. 서버 실행
    - fastapi dev --port 1221 main.py
    - http://127.0.0.1:1221/docs 로 접속
    - station, cctv, robot 순서로 하나씩 만들기