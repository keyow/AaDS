def decode_serialized(enc):
    counter = 0
    counters, fragments = [], ['']
    for symbol in enc:
        if symbol.isnumeric():
            counter = counter * 10 + int(symbol)
        else:
            if symbol == '[':
                counters.append(counter)
                counter = 0
                fragments.append('')
            elif symbol == ']':
                inner = (counters.pop() * fragments.pop())
                fragments[-1] += inner
            else:
                fragments[-1] += symbol
    return fragments.pop()


print(decode_serialized("aaaaaaaaaa"))
print(decode_serialized("aa5[B]cdef4[O]"))
print(decode_serialized("5[4[3[2[1[A]]]]eu]"))
print(decode_serialized("ab3[wow4[Ld2[POP]]okay]lol3[M]ENDHERE2[double]"))
print(decode_serialized("10[]"))