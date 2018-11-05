import json

## ID_info txt에서 ID를 읽어, ID를 부여하는 함수
def read_json(create_student, json_big_data):
    with open('Student_ID_info.txt', 'r') as student_id_info:
        student_id = student_id_info.readline()
        create_student['student_ID'] = student_id
        json_big_data.append(create_student)

## JSon 파일 생성하는 함수
def make_json(json_big_data):
    with open('ITT_Student.JSon', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)


