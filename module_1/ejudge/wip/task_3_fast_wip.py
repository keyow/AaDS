import sys


def find_chains(current_lib, parents, own_libs, chain=None, chain_set=None,chains=None):
    if chain is None:
        chain = [current_lib]
        chain_set = {current_lib}
    if chains is None:
        chains = []
    if current_lib in own_libs:
        chains.append(list(reversed(chain)))
    if current_lib in parents:
        for parent in parents[current_lib]:
            if parent in chain_set:
                continue
            chain.append(parent)
            chain_set.add(parent)
            find_chains(parent, parents, own_libs, chain=chain, chain_set=chain_set, chains=chains)
            chain.pop()
            chain_set.remove(parent)
    return chains


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


if __name__ == '__main__':
    vulnerable_targets = set(input().split())
    own_libraries = set(input().split())

    libs_parents = find_parents(sys.stdin.readlines())
    for target in vulnerable_targets:
        for c in find_chains(target, libs_parents, own_libraries):
            print(' '.join(c))
