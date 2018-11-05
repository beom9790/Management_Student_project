from mng_create_student import *
from mng_update_student import *
from mng_delete_student import *

def start_student(path_number, json_big_data):

    ## str or 공백으로 인한 오류를 잡아주기 위해
    try:
        while True:
            print("<<json기반 학생 정보 관리 프로그램>>".center(33))
            initial_number = int(input("===원하는 서비스의 번호를 눌러주세요~ 찡긋;)===\n1. 학생 정보 입력\n2. 학생 정보 조회\n"
                                       "3. 학생 정보 수정\n4. 학생 정보 삭제\n5. 프로그램 종료\n-> "))
            if initial_number == 1:         ## 학생 정보 입력
                create_student(path_number, json_big_data)
                path_number = 0             ## 처음부터 신규 생성할 때와, 신규 생성할 때 이미 txt 파일이 존재할 때 아이디 고유번호 선정을 위해
            elif initial_number == 2:       ## 학생 정보 조회
                select_student(json_big_data)
            elif initial_number == 3:       ## 학생 정보 수정
                find_id(json_big_data)      ## 학생 정보 수정 전, ID 조회 함수
            elif initial_number == 4:       ## 학생 정보 삭제
                delete_number = int(input("===삭제를 원하는 서비스의 번호를 눌러주세요~ 찡긋;)===\n"
                                          "1. 학생 정보 삭제\n2. 과목 삭제\n0. 돌아가기\n-> "))
                if delete_number == 1:      ## 학생 정보 삭제
                    delete_info = input("정보 삭제를 원하는 학생의 ID를 입력해 주세요 : ")
                    delete_student(json_big_data, delete_info)
                elif delete_number == 2:    ## 과목 삭제
                    delete_info = input("삭제를 원하는 과목의 강의 코드를 입력해 주세요 : ")
                    delete_class(json_big_data, delete_info)
                elif delete_number == 0:
                    print("정보 삭제 서비스를 취소하셨습니다.\n")
                    continue
                else:
                    print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                    continue

            elif initial_number == 5:       ## 프로그램 종료
                print("이용해 주셔서 감사합니다!! 찡긋;)")
                break
            else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

    ## str or 공백으로 인한 오류를 잡아주기 위해
    except:
        print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
        start_student(path_number, json_big_data)