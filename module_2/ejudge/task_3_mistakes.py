import sys


class CompactTrieNode:
    """
    Узел сжатого префиксного дерева

    self.label - подстрока
    self.children - словарь, где ключ - первый символ подстроки, значение - узел с данной подстрокой
    self.full_word - если подстрока в узле завершает слово, то содержит всё слово. Иначе None.
    """
    def __init__(self, label=None, word=None):
        self.label = label
        self.children = {}
        self.full_word = word


class CompactTrie:
    """
    Сжатое (компактное) префиксное дерево.
    В интерфейсе реализована лишь функция вставки, так как иных функций для реализцаии
    алгоритма не требуется.
    """

    def __init__(self):
        self.root = CompactTrieNode()

    def insert(self, word):
        """
        Вставляет слово в сжатое префиксное дерево.

        1. Если слово пустое - сразу выходим из функции
        2. Если первый символ слова не является началом всех подстрок, являющимися детьми корня префиксного
           дерева, то такого слова в дереве нет -> добавить новый узел с данным словом
        3. Если i-ый символ слова и j-ый подстроки не равны то необходимо:
              1. Расщепить узел:
                  - создать новый узел, содержащий подстроку текущей подстроки, начинающуюся с j-го символа.
                  - в текущем узле обрезать подстроку до j-го символа.
                  - сделать новый узел дочерним к текущему.
              2. Добавить новый узел с остатком слова
                  - создать ещё один узел, содержащий подстроку слова, начинающуюся с i-го символа.
                  - сделать новый узел дочерним к текущему.
                  - выйти из цикла
           Таким образом, мы расщепляем узел, выделяя общий префикс для нового слова и подстроки в данном узле.
        4. Если нет различия в символах, но слово длиннее подстроки - добавить узел с остатком слова
        5. Если нет различия в символах, но подстрока длиннее слова - расщепить узел.
        6. Если нет различия в символах и длины слова и подстроки равны - то пометить узел, как слово.

        ----------------------------------
        Сложность добавления: O(len(word))
        Гарантированно выйдем из цикла в момент, когда индекс i равен длине слова
        ----------------------------------

        :param word: вставляемое слово
        """
        if not word:
            return

        if word[0] not in self.root.children:
            node = CompactTrieNode(word, word=word)
            self.root.children[word[0]] = node
            return

        cur_node = self.root.children[word[0]]

        i = 0
        j = 0
        while True:
            if word[i] != cur_node.label[j]:
                # Tearing the prefix piece off
                node = CompactTrieNode(cur_node.label[j:])
                if cur_node.full_word:
                    node.full_word = cur_node.full_word
                    cur_node.full_word = None
                node.children = cur_node.children
                cur_node.label = cur_node.label[:j]
                cur_node.children = {node.label[0]: node}

                # Adding a new child
                node = CompactTrieNode(word[i:], word=word)
                cur_node.children[word[i]] = node
                return

            i += 1  # stands for inserted word
            j += 1  # stands for node label

            if j == len(cur_node.label) and i < len(word):
                if word[i] not in cur_node.children:
                    # Adding a new child
                    node = CompactTrieNode(word[i:], word=word)
                    cur_node.children[word[i]] = node
                    return
                cur_node = cur_node.children[word[i]]
                j = 0
            elif i == len(word) and j < len(cur_node.label):
                # Tearing the prefix piece off
                node = CompactTrieNode(cur_node.label[j:], word=cur_node.full_word)
                node.children = cur_node.children
                cur_node.label = cur_node.label[:j]
                cur_node.children = {node.label[0]: node}
                cur_node.full_word = word
                j = 0
                return
            elif i == len(word) and j == len(cur_node.label):
                cur_node.full_word = word
                return


class MistakeResolver:
    """
    Обработчик ошибок в слове.
    Предлагает список слов, служащих заменой данному.
    По умолчанию количество возможных ошибок (расстояние Дамерау-Левенштейна, далее ДВ) равно 1.

    К ошибке относятся:
    1. Лишний символ
    2. Отсутствие символа.
    3. Неправильный символ.
    4. Перестановка символов.

    Для оптимизации хранится set со всем словарём. Позволяет за O(1) определять, есть ли такое слово в словаре.
    Также хранит сжатое префиксное дерево (__trie) для быстрого вычисления строк матрицы ДВ.
    Получая подстроку в дереве, мы можем сразу вычислить все строки матрицы ДВ для данной подстроки.
    Далее перебираем дочерние узлы для данной подстроки в __trie и рекурсивно вычисляем следующие строки матрицы ДВ.

    Если в какой-то момент последний элемент строки содержит расстояние, большее заданной стоимости - вычисления
    можно не продолжать (мы знаем, что следующие слова нам точно не подойдут).
    """
    def __init__(self, wordlist):
        self.wordlist = set()
        self.__trie = CompactTrie()

        for word in wordlist:
            lower_case_word = word.lower()
            self.wordlist.add(lower_case_word)
            if word not in wordlist:
                self.__trie.insert(lower_case_word)

    def candidates(self, word, max_distance=1):
        """
        Для заданного расстояния ДВ находит список "кадидатов" для данного слова, в котором, возможно, допущена ошибка.
        Использует рекурсивную функцию __search для последовательного вычисления строк матрицы ДВ для входного слова
        и текущей подстроки.

        ----------------------------------
        Сложность поиска кандидатов: O(N * M^2)
        Пусть N - мощность словаря, M - длина входного слова

        Заполнение словаря - O(N)
        Ширина тиекущей подматрицы ДВ равна длине входного слова, высота - длине текущей подстроки.

        Для каждого слова в СПД количество подсчитанных столбцов гарантированно не превышает длину входного слова
        (M) + 1, так как в противном случае имеем две ошибки и останавливаем рекурсивный проход вершинам СПД.
        Таким образом, для каждого слова в исходном словаре сложность вычисления строк матрицы ДВ составляет O(M ^ 2)
        (M + 1 строка и M столбец, O(M(M + 1)) = O(M ^ 2))

        Всего слов в словаре N, значит имеем O(N * M^2)
        ----------------------------------

        :param word: входное слово
        :param max_distance: максимальное расстояние ДВ
        :return: список со всеми "кандидатами" на замену данного слова
        """
        current_row = range(len(word) + 1)
        lower_case_word = word.lower()
        if lower_case_word in self.wordlist:
            return [lower_case_word]

        results = []
        for first_letter in self.__trie.root.children:
            self.__search(self.__trie.root.children[first_letter], lower_case_word, results, max_distance,
                          prev_row=current_row)
        return results

    def __search(self, node, word, results, max_distance, prev_row, prev_prev_row=None, prev_letter=None):
        current_trie_prefix = node.label

        current_row = [prev_row[0] + 1]
        for row in range(1, len(current_trie_prefix) + 1):
            for col in range(1, len(word) + 1):
                insert_cost = current_row[col - 1] + 1
                delete_cost = prev_row[col] + 1
                replace_cost = prev_row[col - 1]
                if word[col - 1] != current_trie_prefix[row - 1]:
                    replace_cost += 1

                if prev_prev_row and col > 1:
                    if row > 1:
                        prev_letter = current_trie_prefix[row - 2]
                    if word[col - 1] == prev_letter and word[col - 2] == current_trie_prefix[row - 1]:
                        transpose_cost = prev_prev_row[col - 2] + 1
                        current_row.append(min(insert_cost, delete_cost, replace_cost, transpose_cost))
                        continue
                current_row.append(min(insert_cost, delete_cost, replace_cost))

            if row < len(current_trie_prefix):
                prev_prev_row = prev_row
                prev_row = current_row
                current_row = [prev_row[0] + 1]  # adding a new row

        if node.full_word:
            if 0 < current_row[-1] <= max_distance:
                results.append(node.full_word)
        if min(current_row) <= max_distance:  # Иначе нет смысла продолжать вычисления
            for next_first_letter in node.children:
                self.__search(node.children[next_first_letter], word, results, max_distance,
                              prev_row=current_row,
                              prev_prev_row=prev_row,
                              prev_letter=current_trie_prefix[-1])


if __name__ == '__main__':
    words = [str(input()) for i in range(int(input()))]
    resolver = MistakeResolver(words)

    for line in sys.stdin.readlines():
        if line == '\n':
            continue
        target = line.rstrip('\n')
        result = sorted(resolver.candidates(target))
        if result:
            print(f'{target} -'
                  f'{" ok" if len(result) == 1 and result[0] == target.lower() else "> " + ", ".join(result)}',
                  end='\n')
        else:
            print(f'{target} -?', end='\n')
