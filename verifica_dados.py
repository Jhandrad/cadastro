# imports da lib padrão
import time

# imports de terceiros

# imports de módulos próprios

def verifica_faixa_etaria(data: str) -> bool:
    ''' Verifica se pela idade do usuário, ele se enquadra no grupo de risco '''

    ano_atual = time.localtime()[0]
    mes_atual = time.localtime()[1]
    dia_atual = time.localtime()[2]
    ano_nascimento = int(data.split("/")[2])
    mes_nascimento = int(data.split("/")[1])
    dia_nascimento = int(data.split("/")[0])
    idade = ano_atual - ano_nascimento

    if idade > 60:
        return True
    elif idade == 60:
        if (mes_atual - mes_nascimento) > 0:
            return True
        elif (mes_atual - mes_nascimento) == 0:
            if (dia_atual - dia_nascimento) >= 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
