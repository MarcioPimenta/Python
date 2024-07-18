import urllib
import urllib.request

# import requests não consegui fazer funcionar com essa biblioteca

try:
    site = input('Insira o link do site: ')
    check = urllib.request.urlopen(site)  # não deu certo o site pudim, testei com outros
except:
    print("\033[31mDeu erro.\033[m")
else:
    print("\033[32mTudo OK!\033[m")

'''try:
    site = input('Insira o link do site: ')
    check = requests.get(site)
except:
    print('Site indisponível')
else:
    print('Site está acessível')'''
