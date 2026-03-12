# First variant

def get_cats_info(path):
    final_list = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                id, name, age = line.strip().split(',')
                cat = {'id': id, 'name': name, 'age': age}
                final_list.append(cat)
            return final_list
    except FileNotFoundError:
        print('File not found')
        return final_list

# Second variant

# def get_cats_info(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as fh:
#             return [{'id': id, 'name': name, 'age': age}
#                     for line in fh
#                     for id, name, age in [line.strip().split(',')]]
#     except FileNotFoundError:
#         print('File not found')
#         return []