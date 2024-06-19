def softuni_students(*args, **kwargs):
    students_courses = {}
    invalid_courses = []
    result = ''

    for id, student in args:
        if id in kwargs:
            students_courses[student] = kwargs[id]
        else:
            invalid_courses.append(student)

    sorted_students_courses = sorted(students_courses.items(), key=lambda x: (x[0]))
    for student, courses in sorted_students_courses:
        result += (f'*** A student with the username {student} '
                   f'has successfully finished the course {courses}!\n')

    if invalid_courses:
        invalid_courses = sorted(invalid_courses)
        result += f'!!! Invalid course students: {", ".join(invalid_courses)}\n'
    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
