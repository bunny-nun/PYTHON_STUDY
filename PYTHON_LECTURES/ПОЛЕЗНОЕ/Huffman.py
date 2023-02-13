# Подготовить таблицу частотности каждого символа
def symbols_frequency(txt):
    result = dict()
    for i in txt:
        if i in result:
            result[i] += 1
        else:
            result.update({i: 1})
    return result


# Создать класс узла
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left_child = None
        self.right_child = None


# Создать дерево Хаффмана
class HuffmanTree(object):
    # По идее дерева Хаффмана: на основе узла построить
    # дерево Хаффмана в обратном порядке
    def __init__(self, char_weight):
        self.leaf = [Node(a, b) for a, b in char_weight.items()]
        while len(self.leaf) != 1:
            self.leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.leaf[-1].value + self.leaf[-2].value))
            n.left_child = self.leaf.pop(-1)
            n.right_child = self.leaf.pop(-1)
            self.leaf.append(n)
        self.root = self.leaf[0]
        self.buffer = list(range(10))

    # Создать коды с рекурсивным подходом
    def generate_huffman(self, tree, length):
        new_node = tree
        if not new_node:
            return
        elif new_node.name:
            print(f'Кодировка Хаффмана для "{new_node.name}": ', end='')
            for i in range(length):
                print(self.buffer[i], end='')
            print('\n')
            return
        self.buffer[length] = 0
        self.generate_huffman(new_node.left_child, length + 1)
        self.buffer[length] = 1
        self.generate_huffman(new_node.right_child, length + 1)

    # Вывод кодировки Хаффмана
    def get_code(self):
        self.generate_huffman(self.root, 0)


if __name__ == '__main__':
    text = 'hello world!'
    frequency_dict = symbols_frequency(text)
    print(frequency_dict)
    new_tree = HuffmanTree(frequency_dict)
    new_tree.get_code()
