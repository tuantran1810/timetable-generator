import json
import xt_types

def fetch_json(path) -> any:
    data = None
    with open(path) as fd:
        data = json.load(fd)
    return data

def parse_teachers(filepath: str) -> xt_types.XTAllTeachers:
    data = fetch_json(filepath)
    lst = list()
    for t in data:
        teacher = xt_types.teacher_from_json(t)
        lst.append(teacher)
    all_teachers = xt_types.XTAllTeachers(lst)
    return all_teachers

def parse_classrooms(filepath: str) -> xt_types.XTAllClassrooms:
    data = fetch_json(filepath)
    lst = list()
    for t in data:
        croom = xt_types.classroom_from_json(t)
        lst.append(croom)
    all_classrooms = xt_types.XTAllClassrooms(lst)
    return all_classrooms

def parse_classes(
    filepath: str, 
    all_teachers: xt_types.XTAllTeachers, 
    all_classrooms: xt_types.XTAllClassrooms,
) -> xt_types.XTAllClasses:
    data = fetch_json(filepath)
    lst = list()
    for t in data:
        cl = xt_types.class_from_json(t, all_teachers, all_classrooms)
        lst.append(cl)
    classes = xt_types.XTAllClasses(lst)
    return classes

def parse_subjects(filepath: str) -> xt_types.XTAllSubjects:
    data = fetch_json(filepath)
    lst = list()
    for g in data:
        grade = g['grade']
        n_classes = g['n_classes']
        for s in g['subjects']:
            cl = xt_types.subject_from_json(grade, n_classes, s)
            lst.append(cl)
    classes = xt_types.XTAllSubjects(lst)
    return classes

# def process_teacher_class_assigment(
#     j_grades: list,
# ) -> dict:
#     lesson_count = dict()
#     for grade in j_grades:
#         n_classes = grade['n_classes']
#         subjects = grade['subjects']
#         for subject in subjects:
#             subject_id = subject['id']
#             lessons_per_week = subject['lessons_per_week']
#             total_lessons = lessons_per_week * n_classes
#             lesson_count[subject_id] = total_lessons
#     return lesson_count

# def class_teacher_assignment(
        
# ) -> None:
#     return

if __name__ == '__main__':
    subjects_filepath = './problem_modeling/subjects.json'
    classes_filepath = './problem_modeling/classes.json'
    classrooms_filepath = './problem_modeling/classrooms.json'
    teachers_filepath = './problem_modeling/teachers.json'

    all_teachers = parse_teachers(teachers_filepath)
    all_classrooms = parse_classrooms(classrooms_filepath)
    all_classes = parse_classes(classes_filepath, all_teachers, all_classrooms)
    all_subjects = parse_subjects(subjects_filepath)

    print(all_subjects)
