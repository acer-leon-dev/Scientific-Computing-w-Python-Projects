def arithmetic_arranger(problems, show_answers=False):
    ## Error if len(problems > 5)   
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Declare the current operation, pair of operands and
    # the result of the operation for each iteration.
    current_operation = None
    operand_pair = []
    result = None
    longer_operand = None

    ## For returning the equations
    operand1_line = []
    operand2_line = []
    dash_line = []
    result_line = []

    lines = [operand1_line, operand2_line, dash_line]
    if show_answers:
        lines.append(result_line)

    for i in range(len(problems)):
        # Reformat the problem with no whitespace, ex: "98+342"
        problem = problems[i].translate(
            str.maketrans({' ': ''}))

        # Determine the current operation and find the result
        try:
            if problem.find('+') >= 0:
                current_operation_symbol = '+'
                operand_pair = problem.split('+')
                result = str(int(operand_pair[0]) 
                + int(operand_pair[1]))
            elif problem.find('-') >= 0:
                current_operation_symbol = '-'
                operand_pair = problem.split('-')
                result = str(int(operand_pair[0]) 
                - int(operand_pair[1]))
            else:
                # Error if operation is not addition or subtract
                return "Error: Operator must be '+' or '-'."
        except ValueError: 
            ## Error if any operand contains non-digit characters   
            for num in operand_pair:
                if not num.isdigit():
                    return 'Error: Numbers must only contain digits.'
        ## Error if len(operand_pair) > 4             
        for num in operand_pair:
                if len(num) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
        
        # Determine the alignment/justify length
        longer_operand = None
        if len(operand_pair[0]) >= len(operand_pair[1]):
            longer_operand = operand_pair[0]
        else: 
            longer_operand = operand_pair[1]
        
        operand_max_len = len(longer_operand)
        justify_length = 2 + operand_max_len

        # Align and add each line to its respective variable 
        # 1
        operand1_line.append(operand_pair[0].rjust(justify_length))
        # 2
        operand2_line.append(f'{current_operation_symbol} {operand_pair[1].rjust(operand_max_len)}')
        # 3
        dash_line.append('-' * justify_length)
        # 4; only if show_answers == True
        if show_answers:
            result_line.append(result.rjust(justify_length))

    # Combine each line
    problems = '\n'.join(list(map(lambda l: '    '.join(l), lines)))
    return problems

# Test various sequences
print(f'1. \n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
print(f'2. \n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'3. \n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'4. \n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'5. \n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'6. \n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'7. \n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'8. \n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'9. \n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'10. \n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
