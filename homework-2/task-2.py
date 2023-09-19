def find_max_brace_seq(seq):
    checker, counter, result = 0, 0, 0
    for brace in seq:
        if brace == '(':
            checker = (checker << 1) | 1  # equal to "checker * 2 + 1"
        elif brace == ')':
            if checker >= 1:
                counter += 2
                if counter > result:
                    result = counter
            else:
                counter = 0
            checker >>= 1
        else:
            return False  # Wrong symbol
    return result


print(find_max_brace_seq("(()(()))"))
