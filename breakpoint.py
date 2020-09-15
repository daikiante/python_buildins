
"""
breakpoint()
Python3.7で新しく導入された機能。
Pythonのデバッガのブレイクポイントを簡単に置くことができる。
breakpointはsys.breakpointhook()を呼び出し、デフォルトではpdbモジュールが起動してデバッグモードになる。

Python3.7から起動すると、pdbの対話モードに入る。

pdbの使い方 : https://docs.python.org/ja/3/library/pdb.html

Qiita : https://qiita.com/patekawa/items/3e79fe58b3b2f14dbab5
"""
print('--- breakpoint ---')

def print_hello():
    # breakpointを設置する。これだけでOK
    breakpoint()
    for c in 'Hello, World!!!!!':
        print(c)

if __name__ == '__main__':
    print_hello()