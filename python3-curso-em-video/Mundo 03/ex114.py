'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

Create Python code that tests whether the pudding site is accessible by the computer being used.
'''
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('Site não está acessível')
else:
    print('Site está acessível')
