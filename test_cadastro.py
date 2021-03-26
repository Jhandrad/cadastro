# imports da lib padrão
import unittest

#imports de terceiros

# imports de módulos próprios
import valida_dados
import dados_para_teste
import usuarios_cadastrados
import verifica_dados


class TesteValidaDados(unittest.TestCase):
    ''' Testa as funções de integridade e validação 
        dos dados inseridos pelo usuário '''

    def setUp(self) -> None:
        self.CPFS_OK = dados_para_teste.lista_de_cpfs_que_passam
        self.CPFS_NAO_OK = dados_para_teste.lista_de_cpfs_que_nao_passam
        self.NOMES_OK = dados_para_teste.lista_de_nomes_que_passam
        self.NOMES_NAO_OK = dados_para_teste.lista_de_nomes_que_nao_passam
        self.DATAS_OK = dados_para_teste.lista_de_datas_que_passam
        self.DATAS_NAO_OK = dados_para_teste.lista_de_datas_que_nao_passam
        self.SENHAS_OK = dados_para_teste.lista_de_senhas_que_passam
        self.SENHAS_NAO_OK = dados_para_teste.lista_de_senhas_que_nao_passam
        self.PROFISSOES_OK = dados_para_teste.lista_de_profissoes_que_passam
        self.PROFISSOES_NAO_OK = dados_para_teste.lista_de_profissoes_nao_que_passam

        self.VALOR_ESPERADO_TRUE = True
        self.VALOR_ESPERADO_FALSE = False

    def teste_true_valida_cpf(self):
        ''' Teste com cpfs válidos '''

        for cpf in self.CPFS_OK:
            self.assertEqual(valida_dados.valida_cpf(cpf), 
                            self.VALOR_ESPERADO_TRUE)
            
    def teste_false_valida_cpf(self):
        ''' Teste com cpfs inválidos '''

        for cpf in self.CPFS_NAO_OK:
            self.assertEqual(valida_dados.valida_cpf(cpf), 
                            self.VALOR_ESPERADO_FALSE)

    def teste_true_valida_nome_usuario(self):
        ''' Teste com nomes válidos '''

        for nome in self.NOMES_OK:
            self.assertEqual(valida_dados.valida_nome_usuario(nome),
                             self.VALOR_ESPERADO_TRUE)

    def teste_false_valida_nome_usuario(self):
        ''' Teste com nomes inválidos '''

        for nome in self.NOMES_NAO_OK:
            self.assertEqual(valida_dados.valida_nome_usuario(nome),
                             self.VALOR_ESPERADO_FALSE)

    def teste_true_valida_data_nascimento(self):
        ''' Teste com datas válidas'''

        for data in self.DATAS_OK:
            self.assertEqual(valida_dados.valida_data_nascimento(data),
                             self.VALOR_ESPERADO_TRUE)

    def teste_false_valida_data_nascimento(self):
        ''' Teste com datas inválidas'''

        for data in self.DATAS_NAO_OK:
            self.assertEqual(valida_dados.valida_data_nascimento(data),
                             self.VALOR_ESPERADO_FALSE)

    def teste_true_valida_senha(self):
        ''' Teste com senhas válidas '''

        for senha in self.SENHAS_OK:
            self.assertEqual(valida_dados.valida_senha(senha),
                             self.VALOR_ESPERADO_TRUE)
    
    def teste_false_valida_senha(self):
        ''' Teste com senhas inválidas '''

        for senha in self.SENHAS_NAO_OK:
            self.assertEqual(valida_dados.valida_senha(senha),
                             self.VALOR_ESPERADO_FALSE)

    def teste_true_valida_profissao(self):
        ''' Teste com profições válidas '''

        for profissao in self.PROFISSOES_OK:
            self.assertEqual(valida_dados.valida_profissao(profissao), 
                            self.VALOR_ESPERADO_TRUE)
    
    def teste_false_valida_profissao(self):
        ''' Teste com profições inválidas '''

        for profissao in self.PROFISSOES_NAO_OK:
            self.assertEqual(valida_dados.valida_profissao(profissao), 
                            self.VALOR_ESPERADO_FALSE)


class TesteCadastroUsuario(unittest.TestCase):
    ''' Testa as funções de CadastroUsuario '''

    def setUp(self) -> None:
        self.VALUES_OK_1 = dados_para_teste.values_ok_1
        self.VALUES_OK_2 = dados_para_teste.values_ok_2
        self.cadastro = usuarios_cadastrados.UsuariosCadastrados()

        self.VALOR_ESPERADO_TRUE = True
        self.VALOR_ESPERADO_FALSE = False

    def teste_true_cadastrar_usuario(self):
        ''' Cadastro de usuário que ainda não foi cadastrado '''

        self.assertEqual(self.cadastro.cadastrar_usuario(self.VALUES_OK_1),
                         self.VALOR_ESPERADO_TRUE)
    
    def teste_false_cadastrar_usuario(self):
        ''' Cadastro de usuário que já foi cadastrado '''

        self.cadastro.cadastrar_usuario(self.VALUES_OK_2)
        self.assertEqual(self.cadastro.cadastrar_usuario(self.VALUES_OK_2),
                         self.VALOR_ESPERADO_FALSE)


class TesteVerificaDados(unittest.TestCase):
    ''' Testa as funções responsáveis por verificar dados '''

    def setUp(self) -> None:
        self.DATAS_OK = dados_para_teste.lista_de_datas_com_mais_60
        self.DATAS_NAO_OK = dados_para_teste.lista_de_datas_com_menos_60

        self.VALOR_ESPERADO_TRUE = True
        self.VALOR_ESPERADO_FALSE = False

    def teste_true_verifica_faixa_etaria(self):
        ''' Datas de pessoas com mais de 60 anos de idade '''

        for data in self.DATAS_OK:
            self.assertEqual(verifica_dados.verifica_faixa_etaria(data), 
                            self.VALOR_ESPERADO_TRUE)

    def teste_false_verifica_faixa_etaria(self):
        ''' Datas de pessoas com menos de 60 anos de idade '''
        
        for data in self.DATAS_NAO_OK:
            self.assertEqual(verifica_dados.verifica_faixa_etaria(data), 
                            self.VALOR_ESPERADO_FALSE)


unittest.main()