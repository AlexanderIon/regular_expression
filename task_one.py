from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from help_metods import create_list_doubles, create_common_list ,create_repeat_person

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

_list =[]
_str = " "

for e in range(1, len(contacts_list)):
  count_recording = len(contacts_list[e])

  person = contacts_list[e]
  for r in range(7):
    person[r] = f'${person[r]}$'

for i in range(1,len(contacts_list)):

  _list.append(contacts_list[i])


srt_q =""
# print(_list[3])
for i in range(len(_list)):
  srt_q+=(_str.join(_list[i]))+"\n"


"""ГРУПИРУЕМ Ф,И,О,РАБОТА"""
pattern_FIO_ = r'^(\$(\w+)\s(\w+)\s(\w+)\$)\s\$+\s\$+\s\$(\w+)\$'
res = re.sub(pattern_FIO_, r'\2,\3,\4,\5,', srt_q,0, re.MULTILINE)


pattern_F_IO_ = r'^\$(\w+)\$\s\$(\w+)\s(\w+)\$\s\$+\s\$(\w+)\$'
res = re.sub(pattern_F_IO_, r'\1,\2,\3,\4,', res, 0, re.MULTILINE)

pattern_FI_not_ = r'^\$(\w+)\s(\w+)\$\s\$+\s(\$+)\s(\$+)'
res = re.sub(pattern_FI_not_, r'\1,\2,Not,Not,', res, 0, re.MULTILINE)

pattern_F_I_O =  r'^\$(\w+)\$\s\$(\w+)\$\s\$(\w+)\$\s\$(\w+)\$'
res = re.sub(pattern_F_I_O, r'\1,\2,\3,\4,', res, 0, re.MULTILINE)

"""ОТМЕЧАЕМ где нет ДАННЫХ  """
pattern__ =  r'(\s\$\$)'
res = re.sub(pattern__, r',Not', res, 0, re.MULTILINE)
pattern = r'(\,\,)'
res = re.sub(pattern, r',', res, 0, re.MULTILINE)


"""ФОРМАТИРУЕМ ТЕЛ"""
pattern = r"(\$8\s)|(\$\+7\s)|(\$8)|(\$\+7)"
res = re.sub(pattern, r',+7', res, 0, re.MULTILINE)

pattern = r"(\+7\((\d+)\)\s)"
res = re.sub(pattern, r'+7(\2)', res, 0, re.MULTILINE)

pattern = r'(\+7(\d{3})\-)'
res = re.sub(pattern, r'+7(\2)', res, 0, re.MULTILINE)

pattern = r"\+7(\d{3})(\d{3})(\d\d)(\d\d)"
res = re.sub(pattern, r'+7(\1)\2-\3-\4', res, 0, re.MULTILINE)

pattern = r"((\+7\(\d+\)\d+\-)(\d{2})(\d+))"
res = re.sub(pattern, r'\2\3-\4', res, 0, re.MULTILINE)

pattern = r"(\+7\(\d+\)\d+\-\d+\-\d+)\s\((\w+\.\s+\d+)\)"
res = re.sub(pattern, r'\1 \2', res, 0, re.MULTILINE)

"""формируем данные для CVR"""

pattern = r"(\$\s\$)"
res = re.sub(pattern, r',', res, 0, re.MULTILINE)

pattern = r"\s\$(\w)"
res = re.sub(pattern, r',\1', res, 0, re.MULTILINE)
pattern = r'\$\,'
res = re.sub(pattern, r',', res, 0, re.MULTILINE)

pattern = r"\$"
res = re.sub(pattern, r'', res, 0, re.MULTILINE)

pattern = r"\,,"
res = re.sub(pattern, r',', res, 0, re.MULTILINE)

"""ОПРЕДЕЛЕНИЕ совпадений Ф И """
pattern = r"^(\w+\,\w+)"
finder = re.findall(pattern, res, re.MULTILINE)

"""list_repeat_name список имен для обьединения"""
list_repeat_name = create_list_doubles(finder)


"""ФОРМИРОВАНИЕ СПИСКА ДЛЯ CSV формата"""
res = res.split('\n')
del res[-1]
res_cvs = []
for i in range(len(res)):
    res_cvs.append(res[i].split(','))

"""ОбЬЕДИНЕНИЕ повторений (сделано только для двух повторений в основном списке.Надо доделать) """
for q in range(len(list_repeat_name)):
    element = list_repeat_name[q]
    surname, name = element.split(',')
    list_repeating = create_repeat_person(surname, name, res_cvs)
    common = create_common_list(list_repeating)
    res_cvs.append(common)

"""после ОБЬЕДИНЕНИЯ появились пустные элементы.
   УДАЛЯЕМ пустоту."""
while "" in res_cvs:
    res_cvs.remove("")
# pprint(res_cvs)

res_cvs.insert(0, contacts_list[0])
pprint(res_cvs)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(res_cvs)