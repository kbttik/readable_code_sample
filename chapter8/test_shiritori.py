
import contextlib
import io
import sys
from kaito.shiritori import shiritori as kaito_shiritori

def test_しりとり成功(monkeypatch):
    word = ''
    next_head = ''
    words = []
    for w in ['りんごじゅーす', 'すりがらす', 'すずめのなみだ', 'だちょう', 'うんこ']:
        monkeypatch.setattr('sys.stdin', io.StringIO(w))
        print('ワードを入力:')
        word = input().strip()
        jadge, next_head = kaito_shiritori(word, next_head, words)
        if not jadge or word == 'quit':
            print('NG')
            assert False
            break
        print('OK')
        words.append(word)


def test_しりとり失敗_末尾と先頭の不一致(monkeypatch):
    word = ''
    next_head = ''
    words = []
    for w in ['りんご', 'すりがらす']:
        monkeypatch.setattr('sys.stdin', io.StringIO(w))
        print('ワードを入力:')
        word = input().strip()
        jadge, next_head = kaito_shiritori(word, next_head, words)
        if not jadge or word == 'quit':
            print('NG')
            assert True
            break
        print('OK')
        words.append(word)
    
    assert not jadge

