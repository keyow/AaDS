import sys


class CompactTrieNode:
    def __init__(self, word=None, parent=None):
        self.word = word
        self.parent = parent
        self.children = {}
        self.is_word = False


class CompactTrie:
    def __init__(self):
        self.root = CompactTrieNode()

    def insert(self, word):
        cur_node = self.root



class MistakeResolver:
    def __init__(self, wordlist):
        self.wordlist = set()
        self.__trie = CompactTrie()
        for word in wordlist:
            lower_case_word = word.lower()
            self.wordlist.add(lower_case_word)
            # adding to trie here

    def candidates(self, word, max_distance=1):
        current_row = range(len(word) + 1)
        lower_case_word = word.lower()
        if lower_case_word in self.wordlist:
            return [lower_case_word]

        results = []
        for letter in self.__trie.children:
            self.__search(self.__trie.children[letter], letter, lower_case_word, results, max_distance,
                          prev_row=current_row)
        return results

    def __search(self, node, letter, word, results, max_distance, prev_row, prev_prev_row=None, prev_letter=None):
        current_row = [prev_row[0] + 1]

        for col in range(1, len(word) + 1):
            insert_cost = current_row[col - 1] + 1
            delete_cost = prev_row[col] + 1
            replace_cost = prev_row[col - 1]
            if word[col - 1] != letter:
                replace_cost += 1

            if prev_prev_row and col > 1:
                if word[col - 1] == prev_letter and word[col - 2] == letter:
                    transpose_cost = prev_prev_row[col - 2] + 1
                    current_row.append(min(insert_cost, delete_cost, replace_cost, transpose_cost))
                    continue
            current_row.append(min(insert_cost, delete_cost, replace_cost))

        if node.word:
            if 0 < current_row[-1] <= max_distance:
                results.append(node.word)
        if min(current_row) <= max_distance:
            prev_letter = letter
            for letter in node.children:
                self.__search(node.children[letter], letter, word, results, max_distance,
                              prev_row=current_row, prev_prev_row=prev_row, prev_letter=prev_letter)


if __name__ == '__main__':
    words = [str(input()) for i in range(int(input()))]
    resolver = MistakeResolver(words)

    for line in sys.stdin.readlines():
        if line == '\n':
            continue
        target = line.rstrip('\n')
        result = sorted(resolver.candidates(target))
        if result:
            print(f'{target} -{" ok" if len(result) == 1 and result[0] == target.lower() else "> " + ", ".join(result)}',
                  end='\n')
        else:
            print(f'{target} -?', end='\n')
