def arithmetic_arranger(problems):
    # Check for error

    if len(problems) > 5:
        return 'Error: Too many problems.'


    # I turn the elements of the list problem into list of string where each element of the sublist is a string.
    for problem in problems:
        problems[problems.index(problem)] = problem.split(' ')

    final_first_line = ''
    final_second_line = ''
    final_third_line = ''


    for problem in problems:

        first_line = f'{problem[0]}'
        second_line = f'{problem[1]} {problem[2]}'

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

        final_first_line += f'{first_line}\t'
        final_second_line += f'{second_line}\t'
        final_third_line += f'{third_line}\t'

    arranged_problems = f'{final_first_line.rstrip()}\n{final_second_line.rstrip()}\n{final_third_line.rstrip()}'
    return arranged_problems