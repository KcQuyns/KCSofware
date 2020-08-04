str_ = input("input: ")


morse_alp = ['.-', '-...', '-.-.', '-..', '.', '..-.',
             '--.', '....', '..', '.---', '-.-', '.-..',
             '--', '-.', '---', '.--.', '--.-', '.-.', '...',
             '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

morse_num = ['.....', '.----', '..---', '...--', '....-', '-----', '----.', '---..', '--...', '-....']

for ltt in str_:
    _ascii_ = ord(ltt)
    if 64 < _ascii_ < 91:
        print(morse_alp[_ascii_-ord('A')], sep='', end=' ')
    elif 96 < _ascii_ < 123:
        print(morse_alp[_ascii_-ord('a')], sep='', end=' ')
    elif 47 < _ascii_ < 58:
        print(morse_num[_ascii_ - ord('0')], sep='', end=' ')
    elif ltt == ' ':
        print('/', sep='', end=' ')