# 경로 상에 파일이 존재하는지 확인하기 위한 테스트 코드
import os

fileName = "All_site_info.py"
isExisting = os.path.isfile(f"{fileName}")

if isExisting:
    print("Exist")
else:
    print("No exist")


# home directory를 뜻하는 ~/는 isfile()안에 사용불가