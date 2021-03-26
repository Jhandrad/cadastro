# imports da lib padrão
import re
import time

# imports de terceiros

# imports de módulos próprios


def valida_cpf(cpf: str) -> bool:
    ''' Função que apenas retorna True caso a string cpf seja compativel 
        com o padrão: NNN.NNN.NNN-NN '''

    padrao_aceito = re.compile('[0-9]{3,3}\.[0-9]{3,3}\.[0-9]{3,3}-[0-9]{2,2}')
    cpf_valido = True
    
    if padrao_aceito.fullmatch(cpf.strip()) == None:
        cpf_valido = False
    return cpf_valido


def valida_nome_usuario(nome_completo: str) -> bool:
    ''' Função que apenas retorna True caso a string nome_completo
        tenha entre 10 e 2 nomes, e cada nome tenha entre 2 e 30
        caracteres compostos somente por letras maiúsculas e/ou minúsculas '''

    padrao_aceito = re.compile('[A-Za-z]{2,30}')
    nome_valido = True
    contador = 0
    nome_usuario = filter(None, nome_completo.split(" "))
    
    for nome in nome_usuario:
        contador += 1
        if padrao_aceito.fullmatch(nome) == None:
            nome_valido = False
    return ((10 >= contador >= 2) and nome_valido)


def valida_data_nascimento(data: str) -> bool:
    ''' Função que apenas retorna True caso a string data
        siga o padrão: DD/MM/AAAA (dia, mês, ano). E seja composta somente
        por números '''

    ano_atual = time.localtime()[0]
    data_nascimento = data.strip()
    padrao_aceito = re.compile('[0-9]{2,2}\/[0-9]{2,2}\/[0-9]{4,4}') 
    data_valida = False

    if padrao_aceito.fullmatch(data_nascimento) == None:
        return data_valida

    dia_mes_ano = data_nascimento.split("/")
    dia = int(dia_mes_ano[0])
    mes = int(dia_mes_ano[1])
    ano = int(dia_mes_ano[2])

    if (0 < dia <= 31) and (0 < mes <= 12) and ((ano_atual-130) <= ano <= ano_atual):
        data_valida = True
    return data_valida


def valida_senha(senha: str) -> bool:
    ''' Função que apenas retorna True caso a string senha
        siga o padrão: tenha entre 8 e 20 caracteres, podem
        conter números letras maiúsculas e minúsculas, símbolos
        e espaços em branco, porém não pode ser composta
        apenas por espaços em branco '''

    padrao_aceito = re.compile('[a-zA-Z0-9!-/:-@\[-`´\{-~].{7,19}')
    senha_valida = True

    if padrao_aceito.fullmatch(senha) == None:
        senha_valida = False
    return senha_valida


def valida_profissao(profissao: str) -> bool:
    ''' Função que apenas retorna True caso a string profissão
        tenha entre 10 e 1 nome(s), e cada nome tenha entre 1 e 30
        caracteres. Pode conter letras maiúsculas e/ou minúsculas,
        caracteres especiais, símbolos e espaços em branco. Não
        podem conter número, não podem ser vazias ou conter apenas
        espaços em branco. '''

    padrao_aceito = re.compile('[a-zA-Záàâãéèêíïóôõöúçñ!-/:-@\[-`´\{-~]{1,30}')
    profissao_valida = True
    profissao_usuario = filter(None, profissao.split(" "))
    contador = 0

    for prof in profissao_usuario:
        contador += 1
        if padrao_aceito.fullmatch(prof.lower()) == None:
            profissao_valida = False
    return ((10 >= contador >= 1) and profissao_valida)