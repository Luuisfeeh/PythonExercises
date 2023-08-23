def notas(*nota,sit=False):
    dic = dict()
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['média'] = sum(nota)/len(nota)
    if sit:
        if 8 >= dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 9:
            dic['situação'] = 'EXCELENTE'
        elif 5 <= dic['média'] < 7:
            dic['situação'] = 'RUIM'
        else:
            dic['situação'] = 'PÉSSIMO'
    return dic


resp = notas(5.5,2.5,1.5, sit= True)
print(resp)