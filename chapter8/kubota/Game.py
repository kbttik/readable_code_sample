class Game:
    """しりとりゲームクラス
    """

    def __init__(self, min_word_len:int, max_count:int):
        """ゲームの負け条件を入れる

        Args:
            min_word_len ([type], optional): これ以上の長さの文字でしりとりをしないといけない. Defaults to 5:int.
        """
        self.min_word_len = min_word_len
        self.words = []
        self.last_key = ''
        self.now_count = 0
        self.max_count = max_count
        self.is_lose = False

    def is_lose_by_len(self, word:str) -> bool:
        """ワードの長さがゲームの基準を満たしていなくて負けているか

        Args:
            word (str): 入力ワード
            lose_len ([type]): この長さ未満の文字だと負け

        Returns:
            bool: 負けTrue/満たしているFalseの論理値
        """

        # X文字列以下のcountを足していく
        if len(word) >= self.min_word_len:
            self.now_count = 0
        else:
            self.now_count += 1

        #if len(word) < self.min_word_len:
        if self.now_count >= self.max_count:
            print('長さが%s以下のワードが%s回連続したので負け！' % (self.min_word_len, self.max_count))
            return True
        else:
            return False
    
    def is_lose_by_tail(self, word:str) -> bool:
        """ワードの最後が「ん」で負けているか

        Args:
            word (str): 入力ワード

        Returns:
            bool: 負けTrue
        """
        if word[-1] == 'ん':
            print('ん がついた！負け')
            return True
        else:
            return False

    def is_lose_by_match(self, word:str) -> bool:
        """前回のワードの最後とマッチしていないで負けているか。

        Args:
            word (str): [description]
            last_key (str): [description]

        Returns:
            bool: [description]
        """
        if (word[0] != self.last_key):
            # しりとりの開始のときは、一致しなくても負けない
            # 毎回評価させないために位置をここにした
            if self.last_key == '':
                return False
            print('前のワードとしりとりになってない！最後のワード%s' % self.last_key)
            return True
        else:
            return False

    def is_lose_by_already(self, word:str) -> bool:
        """すでに使っている単語なので負け

        Args:
            word (str): [description]

        Returns:
            bool: 単語が含まれているから負け
        """
        if word in self.words:
            print('もう使ってるよ！%s' % word)
            return True
        else:
            return False

    def judge_lose(self, word:str) -> bool:
        """全部の負けを評価して保持する

        Args:
            word (str): [description]
        """
        self.is_lose = any([self.is_lose_by_len(word), self.is_lose_by_tail(word), self.is_lose_by_match(word), self.is_lose_by_already(word)])
        return self.is_lose

    def set_word(self, word:str):
        """wordリストに追加と、次の先頭文字の設定

        Args:
            word (str): [description]
        """
        self.words.append(word)
        self.last_key = word[-1]

    def exec_game(self):
        while(True):
            print('ワードを入力:')
            word = input().strip()
            if self.judge_lose(word):
                print('NG')
                break
            print('OK')
            # 最後の文字を更新
            # 使ったワードリストに追加
            self.set_word(word)

def main():
    game = Game(6, 2)
    #game.exec_game()
    while(True):
        print('ワードを入力')
        word = input().strip()
        if game.judge_lose(word):
                print('NG')
                break
        print('OK')
        # 最後の文字を更新
        # 使ったワードリストに追加
        game.set_word(word)

if __name__ == '__main__':
    main()