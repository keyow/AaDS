def valid_braces_complicated(seq):
    stk = []

    for brace in seq:
        if brace == '(' or brace == '[':
            stk.append(brace)
        else:
            prev = stk.pop()
            if prev == '(' and brace == ']':
                return False
            if prev == '[' and brace == ')':
                return False
    if stk:
        return False
    return True


print(valid_braces_complicated("[()[][](())[]]"))