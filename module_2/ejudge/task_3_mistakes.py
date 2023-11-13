import sys


class CompactTrieNode:
    def __init__(self, label=None, word=None):
        self.label = label
        self.children = {}
        self.full_word = word


class CompactTrie:
    def __init__(self):
        self.root = CompactTrieNode()

    def insert(self, word):
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
    def __init__(self, wordlist):
        self.wordlist = set()
        self.__trie = CompactTrie()

        for word in wordlist:
            lower_case_word = word.lower()
            self.wordlist.add(lower_case_word)
            self.__trie.insert(lower_case_word)

    def candidates(self, word, max_distance=1):
        current_row = range(len(word) + 1)
        lower_case_word = word.lower()
        if lower_case_word in self.wordlist:
            return [lower_case_word]

        results = []
        for first_letter in self.__trie.root.children:
            # print('\n-------------------------')
            # print('WORD:', word, 'NEXT PREFIX:', self.__trie.root.children[first_letter].label)
            self.__search(self.__trie.root.children[first_letter], lower_case_word, results, max_distance,
                          prev_row=current_row)
        return results

    def __search(self, node, word, results, max_distance, prev_row, prev_prev_row=None):
        current_trie_prefix = node.label

        current_row = [prev_row[0] + 1]  # adding a new row
        # print('PREV_PREV_ROW: ', prev_prev_row)
        # print('PREV_ROW', prev_row)
        # print('CURRENT_ROW', current_row)
        for row in range(1, len(current_trie_prefix) + 1):
            for col in range(1, len(word) + 1):
                insert_cost = current_row[col - 1] + 1
                delete_cost = prev_row[col] + 1
                replace_cost = prev_row[col - 1]
                if word[col - 1] != current_trie_prefix[row - 1]:
                    replace_cost += 1

                if prev_prev_row and col > 1:
                    if word[col - 1] == current_trie_prefix[row - 2] and word[col - 2] == current_trie_prefix[row - 1]:
                        transpose_cost = prev_prev_row[col - 2] + 1
                        current_row.append(min(insert_cost, delete_cost, replace_cost, transpose_cost))
                        continue
                current_row.append(min(insert_cost, delete_cost, replace_cost))

            if row < len(current_trie_prefix):
                prev_prev_row = prev_row
                prev_row = current_row
                current_row = [prev_row[0] + 1]  # adding a new row
                # print('AFTER:')
                # print('PREV_PREV_ROW: ', prev_prev_row)
                # print('PREV_ROW', prev_row)
                # print('CURRENT_ROW', current_row)

        if node.full_word:
            if 0 < current_row[-1] <= max_distance:
                # print('COST:', current_row[-1])
                results.append(node.full_word)
        if min(current_row) <= max_distance:  # Иначе нет смысла продолжать вычисления
            for next_first_letter in node.children:
                # print('-------------------------')
                # print('WORD:', word, 'NEXT PREFIX:', node.children[next_first_letter].label)
                self.__search(node.children[next_first_letter], word, results, max_distance,
                              prev_row=current_row,
                              prev_prev_row=prev_row)

    # def __search(self, node, word, results, max_distance, prev_row, prev_prev_row=None, prev_letter=None):
    #     current_row = [prev_row[0] + 1]
    #
    #     for col in range(1, len(word) + 1):
    #         insert_cost = current_row[col - 1] + 1
    #         delete_cost = prev_row[col] + 1
    #         replace_cost = prev_row[col - 1]
    #         if word[col - 1] != letter:
    #             replace_cost += 1
    #
    #         if prev_prev_row and col > 1:
    #             if word[col - 1] == prev_letter and word[col - 2] == letter:
    #                 transpose_cost = prev_prev_row[col - 2] + 1
    #                 current_row.append(min(insert_cost, delete_cost, replace_cost, transpose_cost))
    #                 continue
    #         current_row.append(min(insert_cost, delete_cost, replace_cost))
    #
    #     if node.word:
    #         if 0 < current_row[-1] <= max_distance:
    #             results.append(node.word)
    #     if min(current_row) <= max_distance:
    #         prev_letter = letter
    #         for letter in node.children:
    #             self.__search(node.children[letter], letter, word, results, max_distance,
    #                           prev_row=current_row, prev_prev_row=prev_row, prev_letter=prev_letter)


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
