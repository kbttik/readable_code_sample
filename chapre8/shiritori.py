def shiritori(word, next_head):
    # TODO: 実装してください
    return True, 'aaa'

def main():
    word = ''
    next_head = ''
    while(True):
        print('ワードを入力:')
        word = input().strip()
        jadge, next_head = shiritori(word, next_head)
        if not jadge or word == "quit":
            print("NG")
            break
        print("OK")

if __name__ == "__main__":
    main()
