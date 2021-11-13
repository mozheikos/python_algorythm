from collections import Counter

SEP = '-' * 14  # Разделитель для таблицы (чтоб красиво)


class Node:  # Объект "узел"
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def table(node):  # формирование шифровальной таблицы (в словарь)
    code_table = {}
    s = ''

    def walk(tab, node, s):  # Обход дерева для формирования адресов символов
        if len(node.value) == 1:
             tab[node.value] = s
        else:
            walk(tab, node.left, s=s + '0'), walk(tab, node.right, s=s + '1')
    walk(code_table, node, s)
    return code_table


def tree_build(data):  # Постороение дерева

    def building(data):
        if len(data[0]) == 1:
            return Node(data[0])
        else:
            if len(data[0]) % 2 == 0:
                n = len(data[0]) // 2
            else:
                n = len(data[0]) // 2 + 1
            return Node(data[0], building([data[0][:n]]), building([data[0][n:]]))
    root = Node(data[0][0] + data[1][0], building(data[0]), building(data[1]))
    return root


def haffman(s):  # Парсинг строки по алгоритму Хаффмана. В определенных случаях, когда много разных символов и все они
    # повторяются не часто, распределение получается не совсем оптимальным - один из редких символов цепляется вторым
    # листом к узлу с наиболее частым символом. Надеюсь, это не слишком критичная ошибка. но буду благодарен, если Вы
    # подскажете алгоритм более правильно разбивающий строку
    c = 0
    for item in range(len(s) - 1):
        if s[item][1] == s[item + 1][1]:
            c += 1
    if len(s) == 2:
        return s
    elif not c:  # Объединение символов в том случае, когда одинаковых частот больше нет, а элементов больше 2
        s = sorted(s, key=lambda x: -x[1])
        result = [*s[:-2], [s[-2][0] + s[-1][0], s[-2][1] + s[-1][1]]]
        return haffman(result)
    else:
        result = []
        i = 0
        while i < len(s):
            j = 0
            while j < len(s):
                if s[i][1] == s[j][1] and s[i][0] != s[j][0]:
                    a = s.pop(i)
                    b = s.pop(j - 1)
                    result.append([a[0] + b[0], a[1] + b[1]])
                    j = 1
                else:
                    j += 1
            else:
                i += 1
        result.extend(s)
        return haffman(result)


string = "good for you"
# string = "good morning"
# string = "big bang theory"
string_split = sorted(list(map(list, Counter(string).items())), key=lambda x: x[1])
haff = haffman(string_split)
tree = tree_build(haff)
coding_table = table(tree)
for key, value in coding_table.items():
    print(SEP)
    print(f'| "{key}" |{value.center(6, " ")}|')
print(SEP)
encoded_string = list(string)
for i in range(len(encoded_string)):
    encoded_string[i] = coding_table[encoded_string[i]]
print(f'\n{string}\n')
print(''.join(encoded_string))
