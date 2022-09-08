import re


def arithmetic_arranger(problems):
    n = 0
    check = False
    if type(problems[-1]) == bool:
        if problems[-1]:
            check = True
        problems.pop(-1)
    max = list(problems)

    if len(problems) > 5:
        return 'Error: Too many problems.\n'
    for problem in problems:
        i = problem.index(' ')
        # error check block
        if problem[i+1] != '+' and problem[i+1] != '-':
            return "Error: Operator must be '+' or '-'.\n"
            return
        if bool(re.search('[a-zA-Z]', problem)):
            return "Error: Numbers must contain digits.\n"
            return
        if len(problem[:i]) > 4 or len(problem[i+3:]) > 4:
            return 'Error: Numbers cannot be more than four digits.\n'
            return

        max[n] = len(problem[:i])
        if len(problem[i + 3:]) > max[n]:
            max[n] = len(problem[i + 3:])
        n += 1
    arranged_problems = ''
    for k in range(n):
        problem = problems[k]
        i = problem.index(' ')
        quant = max[k] - len(problem[:i]) + 2
        space = ' '*quant
        arranged_problems += space + problem[:i] + '    '
    arranged_problems += '\n'
    for k in range(n):
        problem = problems[k]
        i = problem.index(' ')
        quant = max[k] - len(problem[i + 2:]) + 1
        space = ' ' * quant
        arranged_problems += problem[i + 1] + space + problem[i + 2:] + '    '
    arranged_problems += '\n'
    for k in range(n):
        quant = max[k] + 2
        dash = '-'*quant
        arranged_problems += dash + '    '
    if check:
        arranged_problems += '\n'
        for k in range(n):
            problem = problems[k]
            i = problem.index(' ')
            if problem[i + 1] == '+':
                a = int(problem[:i])
                b = int(problem[i + 2:])
                ans = str(a + b)
            else:
                a = int(problem[:i])
                b = int(problem[i+2:])
                ans = str(a - b)
            quant = max[k] - len(ans) + 2
            space = ' ' * quant
            arranged_problems += space + ans
            arranged_problems += '    '
    arranged_problems += '\n'
    return arranged_problems


print(arithmetic_arranger(["32 + 6982", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print(arithmetic_arranger(["32 + 6982", "3801 - 2", "45 + 43", "123 + 49", False]))

