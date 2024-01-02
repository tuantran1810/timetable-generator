import json

def class_summary_to_subjects(
        grades_filepath: str,
        classrooms_filepath: str,
        classes_filepath: str,
        teachers_filepath: str,
    ) -> any:
    classrooms = dict()
    with open(classrooms_filepath) as fp:
        lst = json.load(fp)
        for room in lst:
            classrooms[room['id']] = room['name']

    classes = dict()
    with open(classes_filepath) as fp:
        lst = json.load(fp)
        for cl in lst:
            classes[cl['id']] = cl

    teachers = dict()
    supplement_subjects = set()
    supplement_subjects_to_teachers = dict()
    with open(teachers_filepath) as fp:
        lst = json.load(fp)
        for t in lst:
            teacher_id = t['id']
            teachers[teacher_id] = t
            if 'subjects' in t:
                for s in t['subjects']:
                    supplement_subjects.add(s)
                    if s not in supplement_subjects_to_teachers:
                        supplement_subjects_to_teachers[s] = [teacher_id]
                    else:
                        supplement_subjects_to_teachers[s].append(teacher_id)

    out = list()
    with open(grades_filepath) as fp:
        grades = json.load(fp)
        for grade in grades:
            grade_num = grade['grade']
            n_classes = grade['n_classes']
            subjects = grade['subjects']
            for i in range(1, n_classes+1, 1):
                for subject in subjects:
                    subject_id = subject['id']
                    name = subject['name']
                    class_id = f'class_{grade_num}_{i}'
                    length = subject['length']
                    classes_per_week = subject['classes_per_week']
                    possible_teachers = None
                    if subject_id not in supplement_subjects:
                        c = classes[class_id]
                        host_teacher_id = c['host_teacher_id']
                        possible_teachers = [host_teacher_id]
                    else:
                        possible_teachers = supplement_subjects_to_teachers[subject_id]
                    item = {
                        "id": f'{subject_id}__{grade_num}_{i}',
                        "name": name,
                        "class_id": class_id,
                        "subject_id": subject_id,
                        "length": length,
                        "classes_per_week": classes_per_week,
                        "possible_teachers": possible_teachers,
                    }
                    out.append(item)
    return out

def main():
    grade_input_filepath = './problem_modeling/grades.json'
    classrooms_input_filepath = './problem_modeling/classrooms.json'
    classes_input_filepath = './problem_modeling/classes.json'
    teachers_input_filepath = './problem_modeling/teachers.json'
    output_filepath = './problem_modeling/generated/generated_subjects.json'
    
    subjects = class_summary_to_subjects(
        grade_input_filepath,
        classrooms_input_filepath,
        classes_input_filepath,
        teachers_input_filepath,
    )
    with open(output_filepath, 'w') as fp:
        json.dump(subjects, fp, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()
