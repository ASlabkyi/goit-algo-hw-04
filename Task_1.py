# Fist variant

# def total_salary(path):
#     total = 0
#     count = 0
#
#     try:
#         with open(path, 'r', encoding='utf-8') as fh:
#             for line in fh:
#                 name, salary = line.strip().split(',')
#                 total += int(salary)
#                 count +=1
#             average = total / count
#             return total, average
#     except FileNotFoundError:
#         print('File not found')
#         return 0, 0

# Second variant

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            salaries = [int(line.strip().split(',')[1]) for line in fh]
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    except FileNotFoundError:
        print('File not found')
        return 0, 0
