
def students_credits(*args):
    collection = {}
    total_credits = 0
    result_to_print = ''


    for arg in args:
        line = arg.split('-')
        diyan_points = int(line[-1])
        max_points = int(line[2])
        credits = int(line[1])
        result = diyan_points / max_points
        final_credits = credits * result
        total_credits += final_credits
        collection[line[0]] = final_credits

    if total_credits >= 240:
        result_to_print += f'Diyan gets a diploma with {total_credits:.1f} credits.'
    else:
        credits_needed = 240 - total_credits
        result_to_print += f'Diyan needs {credits_needed:.1f} credits more for a diploma.'

    ordered_collection = sorted(collection.items(), key=lambda x: -x[1])

    for course, credit in ordered_collection:
        result_to_print += f'\n{course} - {credit:.1f}'

    return result_to_print


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
