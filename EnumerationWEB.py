import requests

while True:
    ex = str(input('\33[1;30mDeseja ver Exemplos de uso ? [y/n] ')).upper()
    if ex == 'Y':
        print('\33[1;35mFormato de arquivo:')
        print('(\33[1;30mWindows\33[m): \33[1;36mC:/Users/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('(\33[1;30mLinux\33[m): \33[1;36m/home/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('\33[1;30mFormato da URL: https://target/')
        print('\33[1;30mExemplo de uso: https://google.com/ \33[1;33mC:/Users/Myuser/Desktop/Wordlist.txt\n')

    url = str(input('\33[1;31mInsira a URL: '))
    path2file = str(input('\33[1;31mInsira o caminho para sua wordlist: '))
    show404 = str(input('\33[1;31mEsconder código 404? [y/n] \33[m')).upper()
    print()
    file = open(path2file, 'r', encoding="utf-8")
    with open(path2file) as wordList:
        numberoflines = sum(1 for n in wordList)

    print(f'\033[1;35m{"=":=<50}')
    print('\033[1;36m{:>28}   {:>19}\33[m'.format('Request', 'Response'))
    print(f'\033[1;35m{"=":=<50}\33[m')
    for a in range(0, numberoflines):
        wordlistread = file.readline()
        request = requests.get(url+wordlistread.rstrip())
        output = [wordlistread.strip(), request.status_code]
        if 100 <= request.status_code <= 199:
            print('\33[1;30m{:>28}   \33[1;30m{:>19}\33[m'.format(*output))
        elif 200 <= request.status_code <= 299:
            print('\33[1;30m{:>28}   \33[1;32m{:>19}\33[m'.format(*output))
        elif 300 <= request.status_code <= 399:
            print('\33[1;30m{:>28}   \33[1;35m{:>19}\33[m'.format(*output))
        elif 400 <= request.status_code <= 403 or 405 <= request.status_code <= 499:
            print('\33[1;30m{:>28}   \33[1;31m{:>19}\33[m'.format(*output))
        elif 500 <= request.status_code <= 599:
            print('\33[1;30m{:>28}   \33[1;33m{:>19}\33[m'.format(*output))
        elif request.status_code == 404 and show404 == 'N':
            print('\33[1;30m{:>28}   \33[1;31m{:>19}\33[m'.format(*output))

    print(f'\033[1;35m{"=":=<50}')
    break
