class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    if(word != word[::-1]) :
        # print(word, word[::-1]) 
        # -> interval이 -1이면,
        # 자동적으로 시작인덱스는 -1, 
        # 종료인덱스는 (여기서는) -5가 됨.
        
        raise NotPalindromeError
    else:
        print(word)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)