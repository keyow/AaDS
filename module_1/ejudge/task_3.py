import sys


def find_chains(current_lib, chain=None, chain_set=None):
    if chain is None:
        chain = [current_lib]
        chain_set = {current_lib}
    if current_lib in own_libraries:
        print(' '.join(reversed(chain)))
    if current_lib in libs_parents:
        for parent in libs_parents[current_lib]:
            if parent in chain_set:
                continue
            chain.append(parent)
            chain_set.add(parent)
            find_chains(parent, chain=chain, chain_set=chain_set)
            chain.pop()
            chain_set.remove(parent)


def find_parents(raw_data):
    result = {}
    for line in raw_data:
        deps = line.split()
        for dep in set(deps[1:]):
            if dep not in result:
                result[dep] = {deps[0]}
            else:
                result[dep].add(deps[0])
    return result


vulnerable_targets = set(input().split())
own_libraries = set(input().split())

libs_parents = find_parents(sys.stdin.readlines())
for target in vulnerable_targets:
    find_chains(target)
