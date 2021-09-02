
# script para tratar alguns entraves para a etapa de validação

with open('ocorrencia.csv', 'r') as f:
    arquivo = f.readlines()
    with open('ocorrencia2.csv', 'w') as f:
        for linha in arquivo:
            if linha.split(';')[9].startswith('*'):
                print(linha.index('***'))
                arquivo = f.writelines(linha.replace('***', ''))
            else:
                arquivo = f.writelines(linha)
with open('ocorrencia2.csv', 'r') as f:
    arquivo = f.readlines()
    for linhas in arquivo:
        if linha.split(';')[9].startswith('*'):
                print(linha.index('***'))
