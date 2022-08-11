def arithmetic_arranger(problems):
    # Test if the list has more than 5 problems

    if len(problems) > 5:
        return 'Error: Too many problems.'

    # I turn the elements of the list problem into list of string where each element of the sublist is a string.
    for problem in problems:
        split_problem = problem.split(' ')
        problems[problems.index(problem)] = split_problem

        # Test if the operators are only + or -
        if not split_problem[1] in ['+', '-']:
            return "Error: Operator must be \'+\' or \'-\'."

        # Test if the operands contain only digit
        if not (split_problem[0].isdigit() and split_problem[2].isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Test if the len of each operands' is more than 4

        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'


    final_first_line = ''
    final_second_line = ''
    final_third_line = ''


    for problem in problems:

        # put single space between the operator and the longest of the two operands
        if len(problem[0]) <= len(problem[2]):
            first_line = f'{problem[0]}'
            second_line = f'{problem[1]} {problem[2]}'
        else:
            first_line = f'{problem[0]}'
            second_line = f'{problem[1]}{" "*(len(problem[0])-len(problem[2])+1)}{problem[2]}'

        # Make the two line of the same len
        if len(first_line) < len(second_line):
            while len(first_line) < len(second_line):
                first_line = f' {first_line}'
        elif len(first_line) > len(second_line):
            while len(first_line) > len(second_line):
                second_line = f'{second_line[0]} {second_line[1:]}'

        third_line = ''
        while len(third_line) < len(second_line):
            third_line = f'{third_line}-'

        final_first_line += f'{first_line}    '
        final_second_line += f'{second_line}    '
        final_third_line += f'{third_line}    '

    arranged_problems = f'{final_first_line.rstrip()}\n{final_second_line.rstrip()}\n{final_third_line.rstrip()}'
    return arranged_problems