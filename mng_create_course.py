def create_course(create_student_course_info_now_list, create_student):
    create_student_course_info_now = {}        ## depth 3
    create_student_course_info_now['강의 코드'] = input("강의 코드를 입력해 주세요(예, PY180712) : ")
    if create_student_course_info_now['강의 코드'] == "": return None       ## 엔터시 '돌아가기' 기능
    create_student_course_info_now['강의명'] = input("강의명을 입력해 주세요(예, 점프투 파이썬) : ")
    if create_student_course_info_now['강의명'] == "": return None
    create_student_course_info_now['강사명'] = input("강사명을 입력해 주세요(예, 박철수) : ")
    if create_student_course_info_now['강사명'] == "": return None
    create_student_course_info_now['개강일'] = input("개강일을 입력해 주세요(예, 2018-07-12) : ")
    if create_student_course_info_now['개강일'] == "": return None
    create_student_course_info_now['종강일'] = input("종강일을 입력해 주세요(예, 2019-02-12) : ")
    if create_student_course_info_now['종강일'] == "": return None
    create_student_course_info_now_list.append(create_student_course_info_now)
    create_student.get('수강 정보')['현재 수강 과목'] = create_student_course_info_now_list