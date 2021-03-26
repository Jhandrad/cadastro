CADASTRO DE USUÁRIOS

O script recebe do usuário as seguintes entradas: CPF, NOME COMPLETO, DATA DE NASCIMENTO
e PROFISSÃO, durante esse período o usuário pode digitar -1 para sair do programa. Após
receber essas quatro primeiras entradas o programa faz uma validação, caso alguma entrada
não antenda aos padrões estabelecidos, será pedido que sejam inseridos novos dados.

Após essa primeira fase o usuário não poderá sair do programa até que seja inserida a última
entrada exigida. Então o script pede que seja respondido com (s/n) a pergunta: "Você faz parte
de algum grupo de risco?", a resposta pode ser em maiúscula ou minúscula e caso não seja
(s/n), será exibida uma mensagem de erro e a pergunta será feita novamente. Caso a resposta
seja s, será exibida nos mesmos moldes as perguntas sobre: faixa etária, pessoa institucionali-
zada, indígena vivendo em terras indígenas, trabalhador da saúde e doença preexistente. Todas
para serem respondidas com (s/n). Independente da escolha do usuário, a faixa etária será
calculada por meio de sua data de nascimento. Após isso, será solicitado ao usuário que insira
uma senha e logo após confirme-a. Caso a resposta para a pergunta "Você faz parte
de algum grupo de risco?" seja n, o script pula direto para a parte da senha.

Depois do usuário inserir a senha e confirmá-la o script verifica se são iguais e atendem ao
padrão, caso não sejam iguais será solicitado ao usuário que repita o processo, caso não
atendam ao padrão o script iniciará do zero. Se nada disso acontecer será exibida a pergunta:
"Declaro que as informações são verdadeiras, de acordo com o art. 219 do Código Civil (s/n)".
Se inserido s, é feita uma verificação se aquele usuário não foi cadastrado anteriormente,
o cadastro é concluido se for um usuário único (CPF), os dados do usuário cadastrado são exibi-
dos e o script volta ao estado inicial. Se inserido n, o cadastro não é realizado e retorna-se
ao estado inicial. Todas as perguntas com * são obrigatórias.

PADRÕES ACEITOS

CPF: deve ser no seguinte formato NNN.NNN.NNN-NN. Três blocos de três números separados por
pontos, seguido de um traço e um bloco de dois números.

NOME COMPLETO: o nome completo deve conter entre 10 e 2 nomes simples, cada nome simples deve
conter entre 2 e 30 caracteres que podem ser apenas letras maiúsculas ou minúsculas, não pode
conter caracteres especiais nem síbolos.

DATA DE NASCIMENTO: deve ser no seguinte formato DD/MM/AAAA (dia, mês, ano) e conter apenas 
números. O dia deve ficar entre [1,31], o mês entre [1,12] e o ano entre 
[(ano corrente)-130, (ano corrente)]

PROFISSÃO: deve conter entre 1 e 10 nomes simples, cada um entre 1 e 30 caracteres. Pode conter
caracteres especiais e símbolos. Não pode conter números, nem ser vazio ou apenas espaços em 
branco.

SENHA: deve conter entre 8 e 20 caracteres, podem conter números, letras maiúsculas e
minúsculas, símbolos e espaços em branco, porém não pode ser composta apenas por espaços em
branco.

ORGANIZAÇÃO DE ARQUIVOS

O arquivo menu.py é o arquivo principal.
O arquivo valida_dados.py contém as funções para validar as entradas.
O arquivo verifica_dados.py contém a função para calcular a idade do usuário.
O arquivo usuarios_cadastrados é responsável por armazenar e exibir dados dos usuários.
O arquivo test_cadastro.py contém os testes unitários. (executar para realizar os testes)
O arquivo dados_para_teste.py contém todos os dados usados nos testes unitários de forma a
facilitar a adição de novos dados.


