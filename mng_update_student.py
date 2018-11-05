from mng_select_student import *
from mng_control_json import *

## 학생 정보 수정 전, ID 조회 함수
def find_id(json_big_data):
    search_id = input("정보 수정을 원하는 학생의 ID를 입력해 주세요(예, ITT001) (돌아가기 : Enter)\n"
                      "-> ")
    if search_id == "":          ## 엔터시 '돌아가기' 기능
        return None
    else:
        for total_print in json_big_data:                       ## ID 조회
            if total_print.get('student_ID') == search_id:
                update_student(search_id, total_print, json_big_data)
                return None
        print("일치하는 ID가 없습니다. ID를 확인해 주세요!!\n")      ## ID 조회 -> 일치하는 ID가 없을 경우

## 학생 정보 수정 함수
def update_student(search_id, total_print, json_big_data):
    print("입력하신 ID의 학생 정보는 다음과 같습니다.")
    personal_student_print(total_print)
    update_code = int(input("수정을 원하는 서비스의 번호를 입력해 주세요\n"
                            "1. 이름\n2. 나이\n3. 주소\n4. 수강 정보 수정\n5. 수강 정보 추가\n0. 돌아가기\n-> "))
    if update_code == 1 or update_code == 2 or update_code == 3:
        if update_code == 1:
            update_content = input("현재 이름은 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['이름'])
            total_print['이름'] = update_content
        elif update_code == 2:
            update_content = input("현재 나이는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['나이'])
            total_print['나이'] = int(update_content)
        elif update_code == 3:
            update_content = input("현재 주소는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['주소'])
            total_print['주소'] = update_content
    elif update_code == 4:
            update_class_info = int(input("수정을 원하는 수강 정보의 번호를 입력해 주세요\n"
                                      "1. 과거 수강 횟수\n2. 현재 수강 과목\n0. 돌아가기\n-> "))
            if update_class_info == 1:
                update_content = int(input("현재 과거 수강 횟수는 '%s'입니다. 무엇으로 바꾸시겠습니까? : "
                                           % total_print.get('수강 정보').get('과거 수강 횟수')))
                total_print.get('수강 정보')['과거 수강 횟수'] = int(update_content)
            elif update_class_info == 2:
                update_class_code = input("수정을 원하는 수강 과목의 강의 코드를 입력해 주세요 : ")
                class_index = -1
                for idx_class in total_print.get('수강 정보').get('현재 수강 과목'):
                    class_index += 1
                    if idx_class.get('강의 코드') == update_class_code:
                        print("입력하신 강의 코드의 과목 내용은 다음과 같습니다.")
                        print("강의 코드 : %s" % idx_class.get('강의 코드'))
                        print("강의명 : %s" % idx_class.get('강의명'))
                        print("강사명 : %s" % idx_class.get('강사명'))
                        print("개강일 : %s" % idx_class.get('개강일'))
                        print("종강일 : %s \n" % idx_class.get('종강일'))
                        update_class_content_number = int(input("수정을 원하는 과목 내용의 번호를 입력해 주세요\n"
                                                     "1. 강의 코드\n2. 강의명\n3. 강사명\n0. 돌아가기\n-> "))
                        if update_class_content_number == 1:
                            update_class_content = input("현재 강의 코드는 '%s'입니다. 무엇으로 바꾸시겠습니까? : "
                                                         % idx_class.get('강의 코드'))
                            idx_class['강의 코드'] = update_class_content
                        elif update_class_content_number == 2:
                            update_class_content = input("현재 강의명은 '%s'입니다. 무엇으로 바꾸시겠습니까? : "
                                                         % idx_class.get('강의명'))
                            idx_class['강의명'] = update_class_content
                        elif update_class_content_number == 3:
                            update_class_content = input("현재 강사명은 '%s'입니다. 무엇으로 바꾸시겠습니까? : "
                                                         % idx_class.get('강사명'))
                            idx_class['강사명'] = update_class_content
                        elif update_class_content_number == 0:
                            return None
                        else:
                            print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                            return None
                        break
            elif update_class_info == 0:
                return None
            else:
                print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                return None
    elif update_code == 5:
        yes_no = input("현재 수강 과목을 추가하시겠습니까? (y/n)")
        if yes_no == 'Y' or yes_no =='y':
            print("\n<<'%s'의 현재 수강 과목을 추가하겠습니다.>>".center(40) % search_id)
            while True:
                if yes_no == 'Y' or yes_no == 'y':
                    add_course_info = {}
                    add_course_info['강의 코드'] = input("강의 코드를 입력해 주세요(예, PY180712) : ")
                    if add_course_info['강의 코드'] == "": return None  ## 엔터시 '돌아가기' 기능
                    add_course_info['강의명'] = input("강의명을 입력해 주세요(예, 점프투 파이썬) : ")
                    if add_course_info['강의명'] == "": return None
                    add_course_info['강사명'] = input("강사명을 입력해 주세요(예, 박철수) : ")
                    if add_course_info['강사명'] == "": return None
                    add_course_info['개강일'] = input("개강일을 입력해 주세요(예, 2018-07-12) : ")
                    if add_course_info['개강일'] == "": return None
                    add_course_info['종강일'] = input("종강일을 입력해 주세요(예, 2019-02-12) : ")
                    if add_course_info['종강일'] == "": return None
                    total_print.get('수강 정보').get('현재 수강 과목').append(add_course_info)
                    print("추가 수강 과목 정보 입력을 완료했습니다!!\n")
                    add_cancel = input("수강 과목 추가를 계속하시겠습니까? (y/n)")
                    if add_cancel == 'Y' or add_cancel =='y':
                        break
                    elif add_cancel == 'N' or add_cancel == 'n':
                        print("수강 과목 추가를 완료했습니다!!")
                        break
                    else:
                        print("입력을 잘못하셨습니다. 다시 확인해 주세요:)")
                        break
                else:
                    print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                    return None
        elif yes_no == 'N' or yes_no == 'n':
            print("수강 과목 추가를 취소하셨습니다.\n")
            return None
        else:
            print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
            return None

    elif update_code == 0:
        return None
    else:
        print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
        return None

    make_json(json_big_data)   ## JSon 파일 생성하는 함수로
    print("학생 정보 입력이 수정되었습니다!!\n")