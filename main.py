import csv
#основной файл
MAIN_FILE = 'C:\\Users\\Для учебы\\rcit\\Основной лист.csv'
#категории 
CAT_FILE = 'C:\\Users\\Для учебы\\rcit\\Список категорий.csv'
#подкатегории
CLASS_FILE = 'C:\\Users\\Для учебы\\rcit\\Классификатор.csv'

def func(id:int,f_name:str):
    '''
    id- id категории
    f_name - название csv файла
    '''
    try:   
        file = open(f_name, "r", encoding='utf-8')
        #to list
        data = list(csv.reader(file, delimiter=","))
        #list -> dict
        x = {i[0].split(';')[0]:i[0].split(';')[1] for i in data}
        file.close()
        return x[id]
    except:
        return ""

# Открыть основной файл
with open(MAIN_FILE,'r',encoding='utf-8') as f:
    # Открыть файл для результата
    result_file = open("C:\\Users\\Для учебы\\rcit\\result.txt", "w", encoding='utf-8-sig')
    # Итерация файла с индексом
    for enum, i in enumerate(f.readlines()):
        # Пропуск 1 строки
        if enum != 0:
            r = i.split(';')   
            # результат итерации
            result = r[0],';',func(r[1],CAT_FILE),';',func(r[2],CLASS_FILE),';', r[3]
            #tuple -> str
            result = ''.join(result)
            result_file.writelines(result)
        else:
            # Добавить название столбцов
            result_file.writelines('id;category;class;value\n')
    result_file.close()
