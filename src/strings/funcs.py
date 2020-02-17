#String properties
"123".isdigit()
"ad3a".isalnum()
"\t \n".isspace()

#Регистр
"function".capitalize()
"function".title()
"function".lower()
"function".upper()
"function".title().swapcase()
#Выравнивание
"function".rjust(16, "*")
"function".ljust(16)
"function".center(16)
"function".center(2)
#Разбиение
"function foo\n".split() # --> "function", "foo"
" function foo\n".split(" ") #--> " ", "function", "foo\n"
"function\nfoo\n".splitlines() #--> "function", "foo"
"function\nfoo\n".splitlines(keepends=True) #--> "function\n", "foo\n"
first, rest = "foo bar baz".split(maxsplit=1) #--> rest --> "bar", "baz"
"foo bar baz".rsplit(maxsplit=1) #--> "foo", "bar", "baz"
#Подстроки
"foo" in "function" #--> False
"foo" not in "function" #--> True
"foobar".startswith("foo") #--> True
"foobar".endswith(("boo", "bar")) #--> True
#Поиск подстрок
"integer".find("i")
"integer".find("te", 2, 4) #-> not found
"integer".index("te", 2, 4) #-> not found

#Изменение
"string".replace("str", "int")
"1 / 2 / 3 / 6".replace("/", "*", 2)
"]>>foo bar<<]".lstrip("]>")
"]>>foo bar<<]".strip("[]<>")
"\t foo bar \r\n".strip()
#Байты
hello = b'hello'
h = bytearray(b'hello')
[print(x) for x in "hello".encode()]
if __name__ == "__main__":
    print(repr("92"))
