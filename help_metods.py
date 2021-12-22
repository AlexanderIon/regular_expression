"""Функция на вход принимает список всех Фалимий И Имен cws файла.
   НА выходе будет список из повторяющихся имен и фамилий """


def create_list_doubles(_list_finder):
    _list_finder.sort()
    doubles = []
    for i, element in enumerate(_list_finder):
        if i != 0:
            if element == old:
                doubles.append(element)
                old = None
                continue
        old = element

    return doubles


"""Функция принимает на вход фамилию и имя.После чего 
   в списке _list_cws ищет повторяющиеся данные (Фамилию Имя.)
   На выходе получается список repeat_element , в котором будут данные дублированных (Фамилий и Имен.)
    РАБОТАЕТ ТОЛЬКО ПРИ ДВУХ ПОВТОРЕНИЯХ.Надо доделать чтобы работало при любом количестве совпадений.(в д.з.не входит) """


def create_repeat_person(_surname, _name, _list_cws):
    repeat_element = []
    for i in range(len(_list_cws)):
        element = _list_cws[i]
        if _surname and _name in _list_cws[i]:
            repeat_element.append(_list_cws[i])
            _list_cws[i] = ''
    return repeat_element


"""Функция из двух элементов списка с повторениями 
   делает один общий БЕЗ повторений. """


def create_common_list(list_element):
    log_1 = list_element[0]
    log_2 = list_element[1]

    common = [log_1[0], log_1[1]]
    for i in range(2, len(log_2)):

        if (log_1[i] == 'Not') or (log_1[i] == 'Not '):
            common.append(log_2[i])
        elif (log_2[i] == 'Not') or (log_2[i] == 'Not '):
            common.append(log_1[i])
        elif log_1[i] == log_2[i]:
            common.append(log_2[i])
    return common



