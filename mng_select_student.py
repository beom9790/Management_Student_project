## 학생 정보 조회 함수
def select_student(json_big_data):
    personal_select_name = ['이름', '나이', '주소', '과거 수강 횟수', '강의 코드', '강의명', '강사명']

    print("<<학생 정보 조회를 진행하겠습니다.>>".center(30))
    select_number = int(input("===원하는 조회 서비스의 번호를 눌러주세요~ 찡긋;)===\n"
                                  "1. 전체 학생 조회\n2. 개별 학생 조회\n0. 돌아가기\n-> "))
    if select_number == 1:
        total_student(json_big_data)
    elif select_number == 2:
        print("<<개별 학생 정보 조회합니다.>>".center(30))
        personal_select_number = int(input("===원하는 개별 학생 조회 서비스의 번호를 눌러주세요~ 찡긋;)===\n"
                                           "1. ID\n2. 이름\n3. 나이\n4. 주소\n5. 과거 수강 횟수\n"
                                           "6. 강의 코드\n7. 강의명\n8. 강사명\n0. 돌아가기\n-> "))
        if  personal_select_number == 1:
            personal_select_number = 'student_ID'
            print("<<ID를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 ID를 입력해 주세요 : ")
            personal_student(key_name, personal_select_number, json_big_data)
        elif 2 <= personal_select_number and personal_select_number <= 4:
            # personal_select_number와 personal_select_name 인덱스 차이가 2라서 2를 빼줌
            print_select(personal_select_name[personal_select_number - 2], json_big_data)
        elif 5 <= personal_select_number and personal_select_number <= 8:
            print_select_low(personal_select_name[personal_select_number - 2], json_big_data)
        elif personal_select_number == 0: return None
        else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

    elif select_number == 0:
        return None
    else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

## 전체 학생 정보 조회하는 함수
def total_student(json_big_data):
    print("<<전체 학생 정보 조회합니다.>>".center(30))
    for total_print in json_big_data:
        personal_student_print(total_print)    ## 각각의 학생들 정보 출력을 위해 personal_student_print(total_print) 함수로

## depth 1_ 개별 학생 정보 조회 함수(이름, 나이, 주소를 통한 조회)
def personal_student(key_name, personal_select_number, json_big_data):
    search_index = []
    index_number = 0
    for search in json_big_data:
        if key_name in str(search.get(personal_select_number)):
            search_index.append(index_number)
        index_number += 1
    if len(search_index) == 1:
        personal_student_index(personal_select_number, search_index, key_name, json_big_data)
    elif len(search_index) > 1:
        print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
        mul_id_print(search_index, key_name, json_big_data)
    else:
        print("일치하는 정보가 없습니다. 다시 확인해 주세요!!\n")

## depth 2_ 개별 학생 정보 조회 함수
def low_persoanl_student(key_name, personal_select_number, json_big_data):
    search_index = []
    index_number = 0
    if personal_select_number == '과거 수강 횟수':    ## 과거 수강 횟수를 통한 조회
        for search in json_big_data:
            if key_name in str(search.get('수강 정보').get(personal_select_number)):
                search_index.append(index_number)
            index_number += 1
        if len(search_index) == 1:
            personal_student_index(personal_select_number, search_index, key_name, json_big_data)
        elif len(search_index) > 1:
            print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
            mul_id_print(search_index, key_name, json_big_data)
        else:
            print("일치하는 정보가 없습니다. 다시 확인해 주세요!!\n")

    ## depth 3_ 현재 수강 과목(강의 코드, 강의명, 강사명을 통한) 조회
    else:
        for search in json_big_data:
            for now_course in search.get('수강 정보').get('현재 수강 과목'):
                if key_name in now_course.get(personal_select_number):
                    search_index.append(index_number)
                    break
            index_number += 1
        if len(search_index) == 1:
            personal_student_index(personal_select_number, search_index, key_name, json_big_data)
        elif len(search_index) > 1:
            print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
            mul_id_print(search_index, key_name, json_big_data)
        else:
            print("일치하는 정보가 없습니다. 다시 확인해 주세요!!\n")

## 학생 정보 조회 -> ID가 하나일 경우 출력 전 함수
def personal_student_index(personal_select_number, search_index, key_name, json_big_data):
    total_print = json_big_data[search_index[0]]
    print("'%s'에 '%s'이/가 포함된 학생의 정보는 다음과 같습니다." % (personal_select_number, key_name))
    personal_student_print(total_print)    # 학생 정보 출력 함수(personal_student_print)로

## 학생 정보 조회 -> ID 중복일 경우, ID와 이름만 출력하는 함수
def mul_id_print(search_index, key_name, json_big_data):
    for idx in search_index:
        print("ID : %s      이름 : %s" % (json_big_data[idx].get('student_ID'), json_big_data[idx].get('이름')))
    print("")

## 학생 정보 출력 함수
def personal_student_print(total_print):
    print("학생 ID : %s" % total_print.get('student_ID'))
    print("이름 : %s" % total_print.get('이름'))
    print("나이 : %s" % total_print.get('나이'))
    print("주소 : %s" % total_print.get('주소'))
    print("수강 정보")
    print("  >> 과거 수강 횟수 : %s" % total_print.get('수강 정보').get('과거 수강 횟수'))
    if total_print.get('수강 정보').get('현재 수강 과목'):
        print("  >> 현재 수강 과목")
        for now_course in total_print.get('수강 정보').get('현재 수강 과목'):
            print("    +강의 코드 : %s" % now_course.get('강의 코드'))
            print("    +강의명 : %s" % now_course.get('강의명'))
            print("    +강사명 : %s" % now_course.get('강사명'))
            print("    +개강일 : %s" % now_course.get('개강일'))
            print("    +종강일 : %s \n" % now_course.get('종강일'))
    print("")

def print_select(personal_select_number, json_big_data):
    print("<<%s을/를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30) % personal_select_number)
    key_name = input("조회를 원하는 %s을/를 입력해 주세요 : " % personal_select_number)
    personal_student(key_name, personal_select_number, json_big_data)

def print_select_low(personal_select_number, json_big_data):
    print("<<%s을/를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30) % personal_select_number)
    key_name = input("조회를 원하는 %s을/를 입력해 주세요 : " % personal_select_number)
    low_persoanl_student(key_name, personal_select_number, json_big_data)