def gather_credits(number, *args):
    courses = set()
    credis_from_courses = 0

    for cours, credits in args:
        if credis_from_courses >= number:
            break
        courses.add(cours)
        credis_from_courses += credits


    result = ''

    orderd_courses = sorted(courses)
    if credis_from_courses >= number:
        result += (f'Enrollment finished! Maximum credits: {credis_from_courses}.\n'
                   f'Courses: {", ".join(orderd_courses)}')

    else:
        result += (f'You need to enroll in more courses! You have to gather '
                   f'{number - credis_from_courses} credits more.')
    return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
