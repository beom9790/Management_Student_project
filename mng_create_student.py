import os
from mng_create_course import *
from mng_control_json import *

## 학생 정보 입력 함수
def create_student(path_number, json_big_data):
    print("<<학생 정보 입력을 진행하겠습니다. (돌아가기 : Enter)>>".center(50))
    total_student_list = []

    ## depth 1
    create_student = {}
    create_student['이름'] = input("이름을 입력해 주세요(예, 홍길동) : ")
    if create_student['이름'] == "": return None     ## 엔터시 '돌아가기' 기능
    create_student['나이'] = input("나이를 입력해 주세요(예, 22) : ")
    if create_student['나이'] == "": return None
    create_student['주소'] = input("주소를 입력해 주세요(예, 대구광역시 달서구 성지로 177) : ")
    if create_student['주소'] == "": return None

    ## depth 2
    create_student['수강 정보'] = create_student_course_info = {}
    create_student_course_info['과거 수강 횟수'] = input("과거 수강 횟수를 입력해 주세요(예, 0) : ")
    if create_student_course_info['과거 수강 횟수'] == "": return None
    print("현재 수강 정보를 입력하시겠습니까? (y/n)")

    ## depth 3
    create_student_course_info_now = {}
    create_student_course_info['현재 수강 과목'] = create_student_course_info_now_list = []
    while True:
        now_course_exist = input(" : ")
        if now_course_exist == 'Y' or now_course_exist == 'y':
            create_course(create_student_course_info_now_list, create_student)
            print("추가 수강 정보를 입력하시겠습니까? (y/n)")
        elif now_course_exist == 'N' or now_course_exist == 'n':
            if os.path.isfile("Student_ID_info.txt"):  ## 고유 아이디 생성 후 배정 - 아이디 배정 txt 파일이 있을 경우
                if path_number == 2:                   ## JSon 파일을 신규 생성하는데, 아이디 배정 txt 파일이 있으면 001부터가 아닌
                    with open('Student_ID_info.txt', 'w') as student_id_info:   ## 파일에 있는 아이디 고유번호 +1 증가된 것을 부여하므로,
                        student_id_info.write("ITT" + "001")                    ##  ↳ 001부터 부여하도록!
                else:
                    with open('Student_ID_info.txt', 'r') as numbering:
                        id_number = numbering.readline()
                        split_numbering = id_number[3:]
                        int_split_numbering = int(split_numbering) + 1
                    with open('Student_ID_info.txt', 'w') as student_id_info:
                        student_id_info.write("ITT" + "{0:0>3}".format(str(int_split_numbering)))

            elif not os.path.isfile("Student_ID_info.txt"):     ## 아이디 배정 txt 파일이 없을 경우
                if len(json_big_data) > 0:                      ## 입력값이 이미 있고, 추가로 작성할 경우
                    search_id_index = []                        ## json_big_data에서 ID만 뽑아서 리스트로 저장
                    for id_idx in json_big_data:
                        search_id_index.append(id_idx.get('student_ID'))
                    last_id_number = search_id_index[-1][3:]
                    last_id_number = int(last_id_number) + 1    ## 마지막 아이디 고유번호 + 1 해서 아이디 배정

                    with open('Student_ID_info.txt', 'w') as student_id_info:
                        student_id_info.write("ITT" + "{0:0>3}".format(str(last_id_number)))

                else:       ## 처음부터 입력할 경우
                    with open('Student_ID_info.txt', 'w') as student_id_info:
                        student_id_info.write("ITT" + "001")


            read_json(create_student, json_big_data)  ## JSon 파일 읽는 함수로
            make_json(json_big_data)                  ## JSon 파일 생성하는 함수로
            print("학생 정보 입력이 완료되었습니다!!\n")

            break
        elif now_course_exist == "": return None
        else:
            print("입력을 잘못하셨습니다. y 또는 n을 입력해 주세요:)")