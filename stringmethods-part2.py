# a='computer'
# print(a.upper())

# print('computer'.upper())
# print('COMPUTER'.lower())
# print('COMPUTER'.casefold())
# print('System'.isupper())
# print('SYSTEM'.isupper())
# print('system'.islower())
# print('sySteM'.islower())
# print('cOmPuTEr'.swapcase())
# print('heLLo WOrLd'.capitalize())
# print('heLLo wOrLd'.title())
# print('Hello World'.istitle())
# print('Hello world'.istitle())
# print('Note Book'.startswith('B'))
# print('Note Book'.startswith('n'))
# print('Note Book'.startswith('N'))
# print('Note Book'.startswith('No'))
# print('Note Book'.endswith('No'))
# print('Note Book'.endswith('k'))
# print('Note Book'.endswith('Book'))
# print(len('calendar'))
# print('calendar'.find('d'))
# print('calendar'.find('c'))
# print('calendar'.find('C'))

# print('hi'.isidentifier())
# print('_hi'.isidentifier())
# print('5hi'.isidentifier())

# a="programming"
# print(a.zfill(11))
# print(a.zfill(9))
# print(a.zfill(14))

# name="python programming"
# print(name.center(25))
# print(name.center(25,'^'))
# print(name.center(50,'*'))

# a="computer"
# print(type(a))
# n=a.encode()
# print(n)
# print(a.decode())

# s='hello world'
# print(s.endswith(''))
# print(s.endswith(' '))
# print(s.endswith('ld'))

# n='hello world'
# print(n.startswith(''))
# print(n.startswith(' '))
# print(n.startswith('h'))

# x=' hello world'
# print(x.startswith(''))
# print(x.startswith(' '))
# print(x.startswith('h'))

# a=''
# print(a.isspace())
# b='           '
# print(b.isspace())
# c='   .  '
# print(c.isspace())
# d='python'
# print(d.isspace())

q="methodology"
# print(q.index('l'))
# print(q.index('o',3))
# print(q.index('o',5))
# print(q.index('o'))
# print(q.index('o',4))
# print(q.rindex('g'))
# print(q.index('o'))
# print(q.rindex('o'))
# print(q.index('b'))

# r="hello world programming"
# print(r.index('u'))
# print(r.index('o'))
# print(len(r))
# print(r.rindex('g'))

# r='hello world programming'
# print(len(r))
# print(len('hello world programming'))

# g="python7 programming"
# print(g.find('m'))
# print(g.find('o'))
# print(g.find('s'))
# print(len(g))
# print(g.rfind('m'))

# v='hello python'
# print(v.count('o'))
# print(v.count('p'))
# print(v.count('g'))

# j="python programming"
# print(j.replace('programming','course'))

# w="course python programming course python"
# print(w.replace('python',str(678)))
# print(w.replace('python','678'))
# print(w.replace('o','s',3))
# print(w.replace('o','s',5))
# print(w.replace('o','s',(5)))

# d="             python course      "
# print(d.strip())
# print(d.lstrip())
# print(d.rstrip())
# print(len(d))
# e=d.strip()
# print(len(e))

# f="      hello everyone     ".strip()
# print(len(f))

# a="hi","hello","namaste"
# print(a,type(a))
# b='python'.join(a)
# print(b)
# c=' python '.join(a)
# print(c)
# print("hello","world",sep=" python ")
# d='hiii'
# e="&".join(d)
# print(e)
# f='hey',
# g='@'.join(f)
# print(g)
# h='hey',''
# i='*'.join(h)
# print(i)

# a="college campus"
# print(a.removeprefix('c'))
# print(a.removeprefix('C'))
# print(a.removeprefix('co'))
# print(a.removeprefix("college"))
# print(a.removesuffix('s'))
# print(a.removesuffix('us'))
# print(a.removesuffix('pus'))
# print(a.removesuffix('pous'))

# a="hello world"
# print(a.isalnum())   # space not allowed in isalnum
# a="helloworld"
# print(a.isalnum())   # returns True because no space
# a="hello.world"
# print(a.isalnum())   # returns False because .(point) or special symbols
# a="helloworld56"
# print(a.isalnum())   # returns True because contains only alphabets & numbers

# b="python programming"
# print(b.isalpha())
# b="pythonprogramming"
# print(b.isalpha())
# b="pythonprogramming789"
# print(b.isalpha())
# b='123'
# print(b.isalpha())
# b='hiy'
# print(b.isalpha())
# b=""
# print(b.isalpha())
# b="          "
# print(b.isalpha())

# v='python course'
# print(v.isascii())

# a=chr(0)
# print(a.isspace())
# b=chr(30)
# print(b.isspace())
# print('hello'+chr(32)+'world')
# print('hello'+' '+'world')
# print('hello','world',sep=' ')
# print('hello','world')
# print(chr(32)+"hi")
# print(chr(0)+"hi")

# print(ord('h'))
# print(ord('u'))
# print(ord('S'))
# print(ord('J'))
# print(ord('7'))
# print(ord('8'))
# print(ord(" "))
# print(ord('$'))

# print(chr(67))
# print(chr(66))