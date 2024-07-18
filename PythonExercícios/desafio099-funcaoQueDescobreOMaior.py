import time


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    mai = 0
    for n in num:
        print(f'{n} ', end='', flush=True)
        time.sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    for n in num:
        if n > mai:
            mai = n
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
