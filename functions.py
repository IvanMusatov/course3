import json


def load_data():
    '''Загружаем новый файл'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sorted_state_executed(data):
    '''Сортировка по статусу операции'''
    executed = []
    for part in data:
        for k, v in part.items():
            if v == 'EXECUTED':
                executed.append(part)
    executed = sorted(executed, key=lambda item: item['date'], reverse=True)
    return executed[:5]


def format_date(date):
    '''Форматирование даты по т.з.'''
    format = date[:10].split('-')
    return '.'.join(reversed(format))


def format_check(data):
    '''Форматирование счета по т.з.'''
    check = data.split(' ')
    return f'{"".join(check[0])} **{check[-1][-4:]}'


def format_card(data):
    '''Форматирование номера карты'''
    card = data.split(' ')
    return f'{"".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'


def manipulation(data):
    '''Формируем вывод по т.з.'''
    for item in data:
        if item.get("from") == None:
            print(format_date(item.get("date")), item.get("description"))
            print(format_check(item.get("to")))
            print(item.get("operationAmount")["amount"], item.get("operationAmount")["currency"]["name"])
        elif item.get("description") == 'Перевод со счета на счет':
            print(format_date(item.get("date")), item.get("description"))
            print(format_check(item.get("from")), '->', format_check(item.get("to")))
            print(item.get("operationAmount")["amount"], item.get("operationAmount")["currency"]["name"])
        else:
            print(format_date(item.get("date")), item.get("description"))
            print(format_card(item.get("from")), '->', format_check(item.get("to")))
            print(item.get("operationAmount")["amount"], item.get("operationAmount")["currency"]["name"])
