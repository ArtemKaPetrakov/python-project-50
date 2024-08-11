# import json
from gendiff.parser import parser




def generate_diff(file_path1, file_path2):
    diff_list = ''
    # first_file = dict(json.load(open('tests/fixtures/' + file_path1)))
    # second_file = dict(json.load(open('tests/fixtures/' + file_path2)))

    first_file, second_file = parser(file_path1, file_path2)

    all_files_keys = set(list(first_file.keys()) + list(second_file.keys()))
    sorted_keys = sorted(all_files_keys)

    for key in sorted_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                diff_list += f'    {key}: {first_file[key]}\n'
            else:
                diff_list += f'  - {key}: {first_file[key]}\n'
                diff_list += f'  + {key}: {second_file[key]}\n'
        if key in first_file and key not in second_file:
            diff_list += f'  - {key}: {first_file[key]}\n'
        if key in second_file and key not in first_file:
            diff_list += f'  + {key}: {second_file[key]}\n'

    return '{\n' + diff_list.lower() + '}'
