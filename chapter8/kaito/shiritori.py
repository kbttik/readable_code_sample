def shiritori(word, next_head, words):
    is_game_end_word = word[-1] == 'ん'
    if is_game_end_word:
        print('ん')
        return False, ''

    is_user_same_word = word in words
    if is_user_same_word:
        print('同じワードを使った')
        return False, ''

    if len(word) <= 5:
        is_continue_short_words = [ len(word) <= 5 for word in words[-2:] ] == [True, True]
        if is_continue_short_words:
            print('短いワードが連続した')
            return False, ''


    is_correct_head = not ((next_head == '') or (word[0] == next_head))
    if is_correct_head:
        return False, ''

    return True, word[-1]

def main():
    word = ''
    next_head = ''
    words = []
    while(True):
        print('ワードを入力:')
        word = input().strip()
        jadge, next_head = shiritori(word, next_head, words)
        if not jadge or word == 'quit':
            print('NG')
            break
        print('OK')
        words.append(word)

if __name__ == '__main__':
    main()
