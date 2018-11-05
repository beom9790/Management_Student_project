from mng_select_student import *
from mng_control_json import *

## 학생 정보 삭제 함수
def delete_student(json_big_data, delete_info):
    del_index = -1
    for del_info in json_big_data:
        del_index += 1
        if del_info.get('student_ID') == delete_info:
            print("입력하신 ID의 학생 정보는 다음과 같습니다.")
            for total_print in json_big_data:               ## ID 조회
                if total_print.get('student_ID') == delete_info:
                    personal_student_print(total_print)     ## 입력한 ID의 학생 정보 출력
            del_number = int(input("'%s' 학생의 삭제 내용을 선택해 주세요\n1. 모든 정보 삭제\n"
                                   "2. 수강 강의 정보만 삭제\n0. 돌아가기\n-> " % delete_info))
            if del_number == 1:
                recheck_que = input("정말 '%s' 학생의 모든 정보를 삭제하시겠습니까? (y/n) : " % delete_info)
                if recheck_que == 'Y' or recheck_que == 'y':
                    del json_big_data[del_index]
                    make_json(json_big_data)                ## JSon 파일 생성하는 함수로
                    print("ID '%s' 학생 정보가 모두 삭제 되었습니다!!\n" % delete_info)
                    return None
                elif recheck_que == 'N' or recheck_que == 'n':
                    print("모든 정보 삭제가 취소되었습니다.\n")
                    return None
                else:
                    print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                    return None

            elif del_number == 2:
                del_class_code = input("삭제를 원하시는 수강 강의 코드를 입력해 주세요 : ")
                class_code_list = del_info.get('수강 정보').get('현재 수강 과목')
                code_list_index = -1
                for del_code in class_code_list:
                    code_list_index += 1
                    if del_code['강의 코드'] == del_class_code:
                        recheck_que = input("'%s' 학생의 수강 강의 중 '%s' 강의를 정말 삭제하시겠습니까? (y/n) : "
                                                                            % (delete_info, del_class_code))
                        if recheck_que == 'Y' or recheck_que == 'y':
                            del class_code_list[code_list_index]
                            make_json(json_big_data)        ## JSon 파일 생성하는 함수로
                            print("ID '%s' 학생의 수강 강의 중 '%s' 강의가 삭제되었습니다!!\n"
                                                        % (delete_info, del_class_code))
                            return None
                        elif recheck_que == 'N' or recheck_que == 'n':
                            print("강의 정보 삭제가 취소되었습니다.\n")
                            return None
                        else:
                            print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                            return None

                    else:
                        print("일치하는 강의 코드가 없습니다. 강의 코드를 확인해 주세요!!\n")
                        return None

            elif del_number == 0:
                return None

    else:
        print("일치하는 ID가 없습니다. ID를 확인해 주세요!!\n")
        return None

## 과목 삭제 함수
def delete_class(json_big_data, delete_class):
    for exist_del in json_big_data:
        dl_exist = exist_del.get('수강 정보').get('현재 수강 과목')
        for fnd in dl_exist:
            if fnd.get('강의 코드') == delete_class:
                for del_cl in json_big_data:
                    class_list = del_cl.get('수강 정보').get('현재 수강 과목')
                    del_index = 0
                    for find_del_cl in class_list:
                        if find_del_cl.get('강의 코드') == delete_class:
                                del class_list[del_index]
                        del_index += 1

                recheck_del = input("정말 강의 코드 '%s' 과목을 삭제하시겠습니까? (y/n) : " % delete_class)
                if recheck_del == 'Y' or recheck_del == 'y':
                    make_json(json_big_data)        ## JSon 파일 생성하는 함수로
                    print("강의 코드 '%s' 과목이 삭제되었습니다!!\n" % delete_class)
                    return None
                elif recheck_del == 'N' or recheck_del == 'n':
                    print("과목 삭제가 취소되었습니다.\n")
                    return None
                else:
                    print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                    return None

    else:
        print("일치하는 강의 코드가 없습니다. 강의 코드를 확인해 주세요!!\n")
        return None