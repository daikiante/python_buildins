"""
abs()
数値の絶対値を返却する関数
引数には整数か浮動小数を渡す。また複素数も渡すことが可能。
"""
print('--- abs ---')

# int型 : 整数型
print(abs(1))
print(abs(-1))

# float型 : 浮動小数型
print(abs(-3.4))

# complex : 複素数型
print(abs(3+2j))


"""
all()
引数に渡した要素がすべて真であればTrueを返す。それ以外はFalseを返す。
引数はiterableになる。つまり、ループできるものなら渡せると考えればよい。
"""
print('--- all ---')

# 空ならばTrue
print(all([]))

# list
print(all([1, 2, 3]))

# list : 0が偽になるのでFalse
print(all([0, 1, 2]))

# strも渡せる
print(all('ラーメン'))

# mapオブジェクトも渡せる
print(all(map(lambda x:x==42, [3, 5, 1, 42])))

print(all([True, True, True]))


"""
any()
all()と同じく引数にはiterableを渡すが、評価の仕方が異なる。
any()はOR条件で、引数のiterableのどれか一要素でも真ならTrue, すべて偽の場合にFalseになる。
all()は全て真のときにTrueを返すというAND条件の関数なので違いに注意して使う。
"""
print('--- any ---')

# 空のときはFalse
print(any([]))

# list
print(any([1, 2, 3]))

# list : 0が偽になるのでFalse
print(any([0, 1, 2]))

# strも渡せる
print(any('ラーメン'))

# mapオブジェクトも渡せる
print(any(map(lambda x:x==42, [3, 5, 1, 42])))


"""
ascii()
一つの引数を取る。repr()と同じように可能であればeval()で評価すると引数と同様のオブジェクトになる文字列を、そうでない場合は、<>で囲まれたオブジェクトの情報を返却する。

ASCIIとは、アルファベットや数字、記号などを収録した文字コードの一つ。最も基本的な文字コードとして世界的に普及しており、他の多くの文字コードがASCIIの拡張になるよう実装されている。文字を7ビットの値（0～127）で表し、128文字が収録されている。
"""
# repr()との違いは非ASCII文字が \x \u \U を使ってユニコードのコードポイントとしてエスケープされるということです。例を見るとわかりやすいかもしれません。

print('--- ascii ---')

print(ascii(1))

print(eval(ascii(1)))

# str
print(ascii('Ascii Characters'))

print(eval(ascii('Ascii Characters')))

# 非アスキーな文字列ではエスケープされる
print(ascii('アスキーじゃないお'))

# 結果 : '\u30a2\u30b9\u30ad\u30fc\u3058\u3083\u306a\u3044\u304a'
print(eval(ascii('アスキーじゃないお')))

# ↑をrepr()で評価すると
print(repr('アスキーじゃないお'))

print(eval(repr('アスキーじゃないお')))

# eval()に渡す表現を持たない場合
print(ascii(object()))


"""
bin()
引数に整数を渡すと、頭に"0b"のついた２進数表現の文字列として変換してくる。整数型ではなく、文字列を返すので注意。結果はPythonの式としてeval()で評価可能。
"""
print('--- bin ---')

print(bin(0))

print(bin(1))

print(bin(1023))

print(bin(-1023))

print(eval(bin(1023)))


"""
bool()
引数の値を評価して真ならTrue、偽ならFalseを返却する。
真偽の判定方法は公式ドキュメントの真理値判定を参照。

偽になる値の例
False, None, ,''(空文字列), 0, 0.0, [], {} など。

オブジェクトの真偽値のデフォルトは真なので、__bool__()や__len__()を実装していないクラスのインスタンスをbool()に渡すと、返り値はTrueになる。


ちなみに、Python3.6まではbool()の引数はx=1というように名前付き引数の形式を使えたが、Python3.7からは位置引数のみとなっている。

Python3.6
>>> bool(x=1)
True

Python3.7
>>> bool(x=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bool() takes no keyword arguments
"""
print('--- bool ---')

print(bool())

print(bool(0))

print(bool(1))

print(bool(''))

print(bool('シン'))

print(bool([]))

print(bool({'The Answer': 'Echigo Seika'}))


# __bool__()を実装しないクラス
class MyClass(object):
    pass

# True
print(bool(MyClass()))


# __bool__()を実装するクラス
class MyFalseClass(object):
    def __bool__(self):
        return False

# False
print(bool(MyFalseClass()))

