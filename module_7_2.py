import os


def custom_write(file_name, strings):
    string_num = 0
    key_ = ()
    dict_ = {}
    file = open(file_name, 'w', encoding='utf-8')
    file.close()
    for i in strings:
        file = open(file_name, 'r', encoding='utf-8')
        file.read()
        string_num += 1
        key_ = (string_num, file.tell())
        file.close()
        file = open(file_name, 'a', encoding='utf-8')
        file.write(f'{i}\n')
        file.close()
        dict_[key_] = i
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
