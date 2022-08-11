def arithmetic_arranger(problems):
    # I turn the elements of the list problem into list of string where each element of the sublist is a string.
    for problem in problems:
        problems[problems.index(problem)] = problem.split(' ')

    first_line = ''
    second_line = ''
    third_line = ''
    for problem in problems:
        temp_third_line = ''
        first_line += f'{problem[0]}\t'
        second_line += f'{problem[1]} {problem[2]}\t'

        while len(temp_third_line) < max(len(problem[0]), len(second_line.strip())):
            temp_third_line += '-'

        third_line += temp_third_line + '\t'

    print(first_line)
    print(second_line)
    print(third_line)

    arranged_problems = ''
    return arranged_problems