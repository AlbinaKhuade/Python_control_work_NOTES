import model as m
from os import path

def check_type_num(data):
    if data.isdigit():
        return int(data)
    return -1

# проверка существования id
def check_id_exist(file, m_id):
    list_all_person = m.read_file(file)
    temp = str(m_id)
    count = 0
    for i in range(1,len(list_all_person)):
        if list_all_person[i][0] == temp:
            count += 1
    if count > 0:
        return m_id
    else:
        return -1