from mng_start_student import *


## Entry Point~
json_big_data = []

# 프로그램 시작 시 소스코드가 있는 경로에 'ITT_Student.JSon' 파일을 읽어 들인다
if os.path.isfile("ITT_Student.JSon"):
    path_number = 0
    with open("ITT_Student.JSon", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        start_student(path_number, json_big_data)

# 파일이 없을 시
elif not os.path.isfile("ITT_Student.JSon"):
    path_number = int(input("<<파일이 존재하지 않습니다.>>\n1. 경로 선택\n2. 신규 생성\n-> "))
    if path_number == 1:
        path_path = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.JSon" % path_path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            start_student(path_number, json_big_data)
    elif path_number == 2:
        start_student(path_number, json_big_data)
    else:
        print("입력을 잘못하셨습니다. 프로그램을 종료합니다:)\n")