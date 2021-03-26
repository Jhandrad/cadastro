'''
        Para adicionar novos dados de teste basta criar a variável
        e adicionar na lista correspondente à classe de dados em questão.

                                                                            '''



'''======================================================================='''
'''                  DADOS PARA A PRIMEIRA CLASSE DE TESTE                '''

''' CPFs que devem passar na validação '''
cpf_ok_1 = "385.779.964-05"
cpf_ok_2 = "000.000.000-00"
cpf_ok_3 = "123.456.789-01"
# cpf_ok_4 = 
# cpf_ok_5 = 
# cpf_ok_6 = 
# cpf_ok_7 = 

lista_de_cpfs_que_passam = [
                            cpf_ok_1,
                            cpf_ok_2,
                            cpf_ok_3]


''' CPFs que não devem passar na validação '''
cpf_nao_ok_1 = "74185296336"
cpf_nao_ok_2 = "000-000-000-00"
cpf_nao_ok_3 = "1235.46.789-01"
cpf_nao_ok_4 = "987.367.149.02"
# cpf_nao_ok_5 =  
# cpf_nao_ok_6 = 
# cpf_nao_ok_7 = 

lista_de_cpfs_que_nao_passam = [
                            cpf_nao_ok_1,
                            cpf_nao_ok_2,
                            cpf_nao_ok_3,
                            cpf_nao_ok_4]


''' Nomes que devem passar na validação '''
nome_ok_1 = "Joao Henrique Andrade da Silva"
nome_ok_2 = "Aristoteles de Almeida Santos"
nome_ok_3 = "joao silva"
nome_ok_4 = "ana    souza"
nome_ok_5 = "JOSE MARIA"
nome_ok_6 = ("ARISTIDIS BELQUIOR COUTINHO DE ALMEIDA SILVA PAULO" +
             " DE ANDARDE LIMA")
        
lista_de_nomes_que_passam = [
                            nome_ok_1,
                            nome_ok_2,
                            nome_ok_3,
                            nome_ok_4,
                            nome_ok_5,
                            nome_ok_6]


''' Nomes que não devem passar na validação '''
nome_nao_ok_1 = "João"
nome_nao_ok_2 = "maria34 pereira"
nome_nao_ok_3 = "@josé"
nome_nao_ok_4 = " "
nome_nao_ok_5 = ""
nome_nao_ok_6 = "      "
nome_nao_ok_7 = ("ARISTIDIS BELQUIOR COUTINHO DE ALMEIDA SILVA "+
                 "PAULO DE ANDARDE LIMA BARRETO")
        
lista_de_nomes_que_nao_passam = [
                                nome_nao_ok_1,
                                nome_nao_ok_2,
                                nome_nao_ok_3,
                                nome_nao_ok_4,
                                nome_nao_ok_5,
                                nome_nao_ok_6,
                                nome_nao_ok_7]


''' Datas que devem passar na validação '''
data_ok_1 = "01/01/1985"
data_ok_2 = "05/09/1990"
data_ok_3 = "31/12/1930"
data_ok_4 = "  25/10/2000  "
data_ok_5 = "13/05/2021  "
data_ok_6 = "02/11/2014"
# data_ok_7 = 
        
lista_de_datas_que_passam = [
                            data_ok_1,
                            data_ok_2,
                            data_ok_3,
                            data_ok_4,
                            data_ok_5,
                            data_ok_6]


''' Datas que não devem passar na validação '''
data_nao_ok_1 = "00/03/1975"
data_nao_ok_2 = "05/13/1980"
data_nao_ok_3 = "31/10/3930"
data_nao_ok_4 = "31/12/1889"
# data_nao_ok_5 = 
# data_nao_ok_6 = 
# data_nao_ok_7 = 
        
lista_de_datas_que_nao_passam = [
                                data_nao_ok_1,
                                data_nao_ok_2,
                                data_nao_ok_3,
                                data_nao_ok_4]


''' Senhas que devem passar na validação '''
senha_ok_1 = "a4qj8nzo"
senha_ok_2 = "9fem!@ns"
senha_ok_3 = "jW@0B^e$"
senha_ok_4 = "edR9TxH jos#Y"
senha_ok_5 = "avOs3fFWq5iVY@"
senha_ok_6 = "MNDlk&d&SP1wQo'%'x"
senha_ok_7 = "$SfSU5D@#GF&lvRkZ8sA"
        
lista_de_senhas_que_passam = [
                            senha_ok_1,
                            senha_ok_2,
                            senha_ok_3,
                            senha_ok_4,
                            senha_ok_5,
                            senha_ok_6,
                            senha_ok_7]


''' Senhas que não devem passar na validação '''
senha_nao_ok_1 = "2376"
senha_nao_ok_2 = "seisdg"
senha_nao_ok_3 = "jW@0B^e"
senha_nao_ok_4 = "a"
senha_nao_ok_5 = "          "
senha_nao_ok_6 = "45"
senha_nao_ok_7 = "senhacommaisdevintedigitos"
        
lista_de_senhas_que_nao_passam = [
                                senha_nao_ok_1,
                                senha_nao_ok_2,
                                senha_nao_ok_3,
                                senha_nao_ok_4,
                                senha_nao_ok_5,
                                senha_nao_ok_6,
                                senha_nao_ok_7]


''' Strings que passam na validação (profissão) '''
profissao_ok_1 = "Professor(a)"
profissao_ok_2 = "Médico(a)"
profissao_ok_3 = "Auxiliar de enfermagem"
# profissao_ok_4 = 
# profissao_ok_5 = 
# profissao_ok_6 = 
# profissao_ok_7 = 

lista_de_profissoes_que_passam = [
                                profissao_ok_1,
                                profissao_ok_2,
                                profissao_ok_3]


''' Strings que não passam na validação (profissão) '''
profissao_nao_ok_1 = ""
profissao_nao_ok_2 = "comnumero56"
profissao_nao_ok_3 = "           "
# profissao_ok_4 = 
# profissao_ok_5 = 
# profissao_ok_6 = 
# profissao_ok_7 = 

lista_de_profissoes_nao_que_passam = [
                                profissao_nao_ok_1,
                                profissao_nao_ok_2,
                                profissao_nao_ok_3]



'''======================================================================='''
'''                   DADOS PARA A SEGUNDA CLASSE DE TESTE                '''

values_ok_1 = {"cpf": "385.779.964-05", 
               "nome_usuario": "Aristoteles de Almeida Santos",
               "data_nascimento": "01/01/1985",
               "senha": "jW@0B^e$",
               "profissao": "Professor(a)"} 

values_ok_2 = {"cpf": "123.456.789-01", 
               "nome_usuario": "joao silva",
               "data_nascimento": "08/06/1995",
               "senha": "jW@0B^e$fse",
               "profissao": "Médico(a)"} 



'''======================================================================='''
'''                  DADOS PARA A TERCEIRA CLASSE DE TESTE                '''

''' Datas de nascimento de pessoas com mais de 60 anos '''
data_com_mais_1 = "05/03/1961"
data_com_mais_2 = "30/11/1960"
data_com_mais_3 = "15/03/1959"
data_com_mais_4 = "03/02/1925"

lista_de_datas_com_mais_60 = [
                            data_com_mais_1,
                            data_com_mais_2,
                            data_com_mais_3,
                            data_com_mais_4
                              ]


''' Datas de nascimento de pessoas com menos de 60 anos '''
data_com_menos_1 = "05/07/1961"
data_com_menos_2 = "31/12/1962"
data_com_menos_3 = "25/01/1983"
data_com_menos_4 = "03/02/2000"

lista_de_datas_com_menos_60 = [
                            data_com_menos_1,
                            data_com_menos_2,
                            data_com_menos_3,
                            data_com_menos_4
                              ]