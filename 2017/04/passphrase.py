#!/usr/bin/env python3

def valid(passphrase):
    d = set()
    for i in passphrase.split():
        if PART2:
            i = "".join(sorted(i))
        if i in d:
            return False
        else:
            d.add(i)
    return True

def check_passphrases(f):
    for line in f:
        yield valid(line)

PART2 = False
# print(valid("aa bb cc dd ee "))
# print(valid("aa bb cc dd aa "))
# print(valid("aa bb cc dd aaa"))

with open("input", 'r') as f:
    print(sum(check_passphrases(f)))

PART2 = True
# print(valid("abcde fghij"))
# print(valid("abcde xyz ecdab"))
# print(valid("a ab abc abd abf abj"))
# print(valid("iiii oiii ooii oooi oooo"))
# print(valid("oiii ioii iioi iiio"))

with open("input", 'r') as f:
    print(sum(check_passphrases(f)))
