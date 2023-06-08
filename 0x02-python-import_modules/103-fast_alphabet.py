#!/usr/bin/python3
print(str(list(map(chr, range(65, 91)))).replace(
    chr(39), chr(0)).replace(chr(32), chr(0)).replace(chr(44), chr(0))
    .replace(chr(91), chr(0)).replace(chr(93), chr(0)))
