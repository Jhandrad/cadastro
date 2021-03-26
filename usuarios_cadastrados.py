class UsuariosCadastrados():
    ''' Classe que contém as funcionalidades para armazenar e 
        exibir usuários '''

    def __init__(self) -> None:
        self.lista_de_usuarios = []
    
    def cadastrar_usuario(self, values: dict) -> bool:

        if len(self.lista_de_usuarios) > 0:
            for usuario in self.lista_de_usuarios:
                if usuario["cpf"] == values["cpf"]:
                    return False
            self.lista_de_usuarios.append(values)
            return True 
        else:
            self.lista_de_usuarios.append(values)
            return True 
    
    def lista_usuarios(self) -> None:

        if len(self.lista_de_usuarios) > 0:
            for usuario in self.lista_de_usuarios:
                self.printa_usuario(usuario)
        else:
            print("\n\t\tNENHUM USUÁRIO CADASTRADO AINDA\n")
    
    def printa_usuario(self, usuario: dict) -> None:

        print("\n"+"="*30 + " DADOS DO USUÁRIO " + "="*30 + "\n")
        print("NOME: {0:35}\t DATA DE NASCIMENTO: {1}".format(
            str(usuario["nome_usuario"]).upper(), usuario["data_nascimento"]
        ))
        print("CPF: {0:35}\t PROFISSÃO: {1}".format(
            str(usuario["cpf"]).upper(), str(usuario["profissao"]).upper()
        ))
        if True in usuario["lista_comorbidades"]:
            cont = 0
            lista = ["FAIXA ETÁRIA: ", "PESSOA INSTITUCIONALIZADA: ",
                     "INDÍGENA VIVENDO EM TERRAS INDÍGENAS: ",
                     "TRABALHADOR(A) DA SAÚDE: ", "DOENÇAS: "]
            print("\nGRUPO DE RISCO: {0}".format("SIM"))
            for i in usuario["lista_comorbidades"]:
                print("\t{0}{1}".format(lista[cont], i))
                cont += 1
        else:
            print("\nGRUPO DE RISCO: {0}".format("NÃO"))
      