# -*- coding: utf-8 -*-
"""Readable_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-9elUqK_o-Rb8tBpuKNRQvsONjK-Yc8L
"""

#20210417 松原 Cap. 8

def shiritori(word, next_head, words):
    """しりとりの勝敗を判定する関数

      Args:
        word (str): 入力ワード
        next_head (str): 前ワードの最後の文字
        words (list): １つ前までのワードが格納されているリスト

      Returns:
        bool: 負けTrue/満たしているFalseの論理値をnot any()でまとめて判定して「Falseなら負け」
        next_head (str): wordを引数に最後の文字を返す
      
      memo:
        勝敗条件を書き加える場合はany()内の更新を忘れない事！
    """
    ## debug用
    #print(word[-1]) 
    #print(len(word))

    is_lose_with_nn = word[-1] == "ん"
    if is_lose_with_nn:
      print("「ん」で終わったので負け！")

    # ５文字以下のワードが3回連続したら終了(ここの部分「リーダブル」かな？)
    is_lose_continue_short_words = len(word) <= 5 and \
                                 [ len(word) <= 5 for word in words[-2:] ] == [True, True]
    if is_lose_continue_short_words:
      print("5文字以下が３回連続したので負け！")
    
    is_lose_not_fit_head = not ((next_head == '') or (word[0] == next_head))
    if is_lose_not_fit_head:
      print("しりとりになってない！やり直し！")
    
    is_lose_already_used = word in words
    if is_lose_already_used:
      print("すでに使われてるので負け！")
    
    return not any([is_lose_with_nn, is_lose_continue_short_words, \
                    is_lose_not_fit_head, is_lose_already_used]), word[-1]


def main():
    word = ''
    next_head = ''
    words = []
    while(True):
        print('ワードを入力:')
        word = input().strip()
        jadge, next_head = shiritori(word, next_head, words)
        if not jadge or word == "quit":
            print("NG")
            break
        print("OK")
        words.append(word)

if __name__ == "__main__":
    main()