import json

class XTTeacher:
    def __init__(self, teacher_id: str, name: str, permanent: bool, lesson_per_week_limit: int, subjects: list[str]):
        self.teacher_id = teacher_id
        self.name = name
        self.permanent = permanent
        self.lesson_per_week_limit = lesson_per_week_limit
        self.homeroom_teacher = subjects is None
        self.subjects = subjects

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return str(self)

def teacher_from_json(data: any) -> XTTeacher:
    return XTTeacher(data['id'], data['name'], data['permanent'], data['lesson_per_week_limit'], data.get("subjects", None))

class XTAllTeachers:
    def __init__(self, lst: list[XTTeacher]):
        self.lst = lst
        self.__dict = dict()
        for t in lst:
            self.__dict[t.teacher_id] = t

    def get_by_id(self, teacher_id: str) -> XTTeacher:
        return self.__dict.get(teacher_id, None)
    
    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self)


class XTClassroom:
    def __init__(self, room_id: str, name: str):
        self.room_id = room_id
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)

def classroom_from_json(data: any) -> XTClassroom:
    return XTClassroom(data['id'], data['name'])

class XTAllClassrooms:
    def __init__(self, lst: list[XTClassroom]):
        self.lst = lst
        self.__dict = dict()
        for t in lst:
            self.__dict[t.room_id] = t

    def get_by_id(self, room_id: str) -> XTTeacher:
        return self.__dict.get(room_id, None)
    
    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self)
    

class XTClass:
    def __init__(self, class_id: str, homeroom_teacher: XTTeacher, classroom: XTClassroom):
        self.class_id = class_id
        if homeroom_teacher is None:
            raise RuntimeException(f"homeroom teacher not exists for class {class_id}")
        self.homeroom_teacher = homeroom_teacher
        if classroom is None:
            raise RuntimeException(f"classroom not exists for class {class_id}")
        self.classroom = classroom

    def __str__(self):
        return str(f'({self.class_id};{self.homeroom_teacher.teacher_id};{self.classroom.room_id})')

    def __repr__(self):
        return str(self)

def class_from_json(data: any, all_teachers: XTAllTeachers, all_classrooms: XTAllClassrooms) -> XTClass:
    homeroom_teacher_id = data['homeroom_teacher_id']
    classroom_id = data['classroom_id']
    homeroom_teacher = all_teachers.get_by_id(homeroom_teacher_id)
    classroom = all_classrooms.get_by_id(classroom_id)
    return XTClass(data['id'], homeroom_teacher, classroom)

class XTAllClasses:
    def __init__(self, lst: list[XTClass]):
        self.lst = lst
        self.__dict = dict()
        for t in lst:
            self.__dict[t.class_id] = t

    def get_by_id(self, class_id: str) -> XTTeacher:
        return self.__dict.get(class_id, None)
    
    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self)
