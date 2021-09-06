'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

Make a program that has a notes() function that can receive multiple grades from students and will return a dictionary with
The following information:
- Number of notes
- The highest grade
- The lowest grade
- The class average
- The situation (optional)
Also add the docstrings of this function for developer query.
'''
def notas(*n, sit=False):
    info = dict()
    info['Quantidade de notas: '] = len(n)
    info['Maior nota: '] = max(n)
    info['Menor nota: '] = min(n)
    info['Média da turma: '] = round(sum(n)/len(n),2)

    if sit:
      if sum(n)/len(n) >= 7:
          info['Situação da turma'] = 'BOA'
      elif sum(n)/len(n) >= 5:
          info['Situação da turma'] = 'RAZOÁVEL'
      else:
          info['Situação da turma'] = 'RUIM'

    for i, j in info.items():
        print(f'{i}: {j}')


# MAIN
notas(5.5, 2.5, 1.5)
print()
notas(10, 8, 7.5,sit=True)