# imports da lib padrão

# imports de terceiros

# imports de módulos próprios
import valida_dados
import verifica_dados
import usuarios_cadastrados

class Menu():

    def __init__(self) -> None:
        self.values = {}
        self.usuarios = usuarios_cadastrados.UsuariosCadastrados()

    def verifica_entradas(self, values: dict) -> int:

        codigo_erro = 0
        if not valida_dados.valida_cpf(values["cpf"]):
            codigo_erro = 1
            return codigo_erro
        if not valida_dados.valida_nome_usuario(values["nome_usuario"]):
            codigo_erro = 2
            return codigo_erro
        if not valida_dados.valida_data_nascimento(values["data_nascimento"]):
            codigo_erro = 3
            return codigo_erro
        if not valida_dados.valida_profissao(values["profissao"]):
            codigo_erro = 4
            return codigo_erro
        return codigo_erro

    def faz_validacao(self, values: dict) -> bool:
        resultado = self.verifica_entradas(values)
        if resultado == 1:
            print("\n\t\t" + " "*7 + "CPF EM FORMATO NÃO ACEITO\n")
            return False
        if resultado == 2:
            print("\n\t\t" + " "*7 + "NOME EM FORMATO NÃO ACEITO\n")
            return False
        if resultado == 3:
            print("\n\t\t" + " "*7 + "DATA DE NASCIMENTO EM FORMATO NÃO ACEITO\n")
            return False
        if resultado == 4:
            print("\n\t\t" + " "*7 + "PROFISSÃO EM FORMATO NÃO ACEITO\n")
            return False
        return True

    def grupo_risco(self) -> list:
        lista_comorbidades = []  
        while True:
            resposta_grupo_risco = input("Você faz parte de algum grupo" +
                                        " de risco? (s/n) ").lower()
            if resposta_grupo_risco == "n":
                faixa_etaria = (verifica_dados.verifica_faixa_etaria
                                        (self.values["data_nascimento"]))
                lista_comorbidades.append(faixa_etaria)
                for i in range(4):
                    lista_comorbidades.append(False)
                return lista_comorbidades
            elif resposta_grupo_risco == "s":
                
                while True:
                    faixa_etaria = input("Faixa etária? (s/n) ").lower()
                    if faixa_etaria == "s":
                        pass
                    elif faixa_etaria == "n":
                        pass
                    else:
                        print("Entrada inválida,"
                            + " responda com (s/n)")
                        continue
                    pessoa_inst = input("Pessoa institucionalizada? (s/n) ").lower()
                    if pessoa_inst == "s":
                        pessoa_inst = True
                    elif pessoa_inst == "n":
                        pessoa_inst = False
                    else:
                        print("Entrada inválida,"
                            + " responda com (s/n)")
                        continue
                    indig_v_t_indg = input("Indígena vivendo em terras indígenas? (s/n) ").lower()
                    if indig_v_t_indg == "s":
                        indig_v_t_indg = True
                    elif indig_v_t_indg == "n":
                        indig_v_t_indg = False
                    else:
                        print("Entrada inválida,"
                            + " responda com (s/n)")
                        continue
                    trabal_saude = input("Trabalhador da saúde? (s/n) ").lower()
                    if trabal_saude == "s":
                        trabal_saude = True
                    elif trabal_saude == "n":
                        trabal_saude = False
                    else:
                        print("Entrada inválida,"
                            + " responda com (s/n)")
                        continue
                    doencas = input("Doença preexistente? (s/n) ").lower()
                    if doencas == "s":
                        doencas = True
                    elif doencas == "n":
                        doencas = False
                    else:
                        print("Entrada inválida,"
                            + " responda com (s/n)")
                        continue
                    break
                faixa_etaria = (verifica_dados.verifica_faixa_etaria
                                        (self.values["data_nascimento"]))
                lista_comorbidades.append(faixa_etaria)
                lista_comorbidades.append(pessoa_inst)
                lista_comorbidades.append(indig_v_t_indg)
                lista_comorbidades.append(trabal_saude)
                lista_comorbidades.append(doencas)
                return lista_comorbidades
            else:
                print("Entrada inválida, responda com s/n")
                continue
    
    def pede_senha(self) -> tuple[bool, str]:
        while True:
            senha = input("Insira uma senha* ")
            senha1 = input("Confirme a senha* ")
            if senha == senha1:
                return (valida_dados.valida_senha(senha), senha)
            else:
                print("\n\t\t" + " "*7 + "AS SENHAS NÃO SÃO IGUAIS\n")
                continue

    def exibir(self) -> None:  
        while True:
            print("\n"+"="*25 + " CADASTRO DE USUÁRIO " + "="*25 + "\n")
            print("\t\tDigite -1 para sair a qualquer momento\n" +
                  "\n\t\t\t"+"    *OBRIGATÓRIO\n")
            cpf = input("Digite seu CPF na forma: NNN.NNN.NNN-NN* ")
            if cpf == "-1":
                break
            nome_usuario = input("Digite o nome completo " + 
                                "(sem caracteres especiais)* ")
            if nome_usuario == "-1":
                break
            data_nascimento = input("Digite a data de nascimento na forma: " +
                                    "DD/MM/AAAA* ")
            if data_nascimento == "-1":
                break
            profissao = input("Digite a sua profissão* ")
            if profissao == "-1":
                break
            self.values = {"cpf" : cpf,
                      "nome_usuario" : nome_usuario,
                      "data_nascimento" : data_nascimento,
                      "profissao" : profissao
                             }
            if not self.faz_validacao(self.values):
                continue
            lista_comorbidades = self.grupo_risco()
            self.values["lista_comorbidades"] = lista_comorbidades
            ok_senha = self.pede_senha()
            if ok_senha[0]:
                self.values["senha"] = ok_senha[1]
            else:
                print("\n\t\t" + " "*7 + "SENHA EM FORMATO NÃO ACEITO\n")
                continue
            while True:
                aceito = input("Declaro que as informações são verdadeiras, " +
                        "de acordo com o art. 219 do Código Civil* (s/n)").lower()
                if aceito == "s":
                    if not self.usuarios.cadastrar_usuario(self.values):
                        print("\n\t\t" + " "*7 + "USUÁRIO JÁ FOI CADASTRADO\n")
                        break
                    else:
                        print("\n\t\t" + " "*7 + "CADASTRO CONCLUÍDO COM SUCESSO\n")
                        self.usuarios.lista_usuarios()
                        break
                elif aceito == "n":
                    print("\n\t\t" + " "*7 + "CADASTRO NÃO CONCLUÍDO\n")
                    break
                else:
                    print("Entrada inválida,"
                        + " responda com (s/n)")
                    continue
            
            


menu = Menu()
menu.exibir()