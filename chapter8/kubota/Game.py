class Game:
    """しりとりゲームクラス
    """

    def __init__(self, min_word_len:int):
        """ゲームの負け条件を入れる

        Args:
            min_word_len ([type], optional): これ以上の長さの文字でしりとりをしないといけない. Defaults to 5:int.
        """
        self.min_word_len = min_word_len
        self.words = []
        self.last_key = ''

    def is_lose_by_len(self, word:str) -> bool:
        """ワードの長さがゲームの基準を満たしていなくて負けているか

        Args:
            word (str): 入力ワード
            lose_len ([type]): この長さ未満の文字だと負け

        Returns:
            bool: 負けTrue/満たしているFalseの論理値
        """
        return len(word) < self.min_word_len
    
    def is_lose_by_tail(self, word:str) -> bool:
        """ワードの最後が「ん」で負けているか

        Args:
            word (str): 入力ワード

        Returns:
            bool: 負けTrue
        """
        return word[-1] == 'ん'

    def is_lose_by_match(self, word:str, last_key:str) -> bool:
        """前回のワードの最後とマッチしていないで負けているか。

        Args:
            word (str): [description]
            last_key (str): [description]

        Returns:
            bool: [description]
        """
        if last_key == '':
            return False

        return word[0] != last_key

    def is_lose_by_already(self, word:str) -> bool:
        """すでに使っている単語なので負け

        Args:
            word (str): [description]

        Returns:
            bool: 単語が含まれているから負け
        """
        return word in self.words

    def judge_is_lose(self, word:str) -> bool:
        """全部の負けを評価する

        Args:
            word (str): [description]
            last_key (str): [description]

        Returns:
            bool: [description]
        """
        return any([self.is_lose_by_len(word), self.is_lose_by_tail(word), self.is_lose_by_match(word, self.last_key), self.is_lose_by_already(word)])

    def exec_game(self):
        while(True):
            print('ワードを入力:')
            word = input().strip()
            if self.judge_is_lose(word):
                print('NG')
                break
            print('OK')
            # 最後の文字を更新
            self.last_key = word[-1]
            # 使ったワードリストに追加
            self.words.append(word)

def main():
    game = Game(5)
    game.exec_game()

if __name__ == '__main__':
    main()