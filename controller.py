from model import Categoria, Produto, Cliente, Fornecedor, Funcionario, Movimento
from dal   import DalCategoria, DalProduto, DalCliente, DalFornecedor, DalFuncionario, DalMovimento
from termcolor import colored
from datetime import datetime
from collections import OrderedDict
from operator import itemgetter

class ConfirmacaoControler:

    @classmethod     
    def confirmacao(cls, msg):
        conf=''
        while conf.upper() not in ('S','N'):
            conf=input(colored(f'{msg}  [S/N]' ,'cyan', attrs=['bold']))
        
        return conf.upper()

    @classmethod     
    def deseja_alterar_excluir(cls,msg):
        conf=''
        while conf.upper() not in ('A','E','S'):
          conf=input(colored(f'Deseja Alterar/Excluir/Sair [A/E/S] { msg }: ','cyan', attrs=['bold']))
        return conf.upper()

    @classmethod
    def numero_valido(cls, campo):
         
        while not campo.isnumeric():
            campo = input(colored('Digite um número válido: ','yellow'))

        campo2=int(campo)
        return campo2    
    
    @classmethod
    def valor_valido(cls, campo):
        while True:
            try: 
              float(campo)
              break
            except:
              campo = input(colored('Digite um número válido: ','yellow'))

        campo2=float(campo)

        return campo2        
    
    @classmethod
    def valida_data(cls, datmov,n):
       
        conf = False
        data = datmov

        while True: 

            if n==1 and (data=='0000' or data=='0' ):
                data_valida=data
                break
            else:
                try:
                    data_valida = str(datetime.strptime(data, '%d/%m/%Y'))
                    break
                except ValueError:
                    data = input("Digite uma data no formato dd/mm/aaaa: ")

        return data_valida
    
    @classmethod
    def tipodoc_valido(cls, tipo_doc):
        while True:
            try: 
              if tipo_doc in ('CC','VV','DC','DV'):
                 break
              else:
                print(colored('Digite um tipo Valido','red'))
                tipo_doc = input(colored(' [cc]-Entrada [vv]-Saida [dc]-Devolução da compra [dv}-Devoluçao da venda: ','yellow')).upper()                   
            except:
              print(colored('Digite um tipo Valido','red'))
              tipo_doc = input(colored(' [cc]-Compra [vv]-Venta [dc]-Devolução da compra [dv}-Devoluçao da venda: ','yellow')).upper()  

        return tipo_doc       
    
class CategoriaControler:
    
    @classmethod
    def pega_todas_categoria(cls):

        dic_categoria=DalCategoria.ler()
        return dic_categoria
          
    @classmethod   
    def alterar_categoria(cls, dic_categoria, categoria, descricao):
        dic_categoria[categoria]['descricao']=descricao
        DalCategoria.esvaziar()

        for x,y in dic_categoria.items():        
            res =DalCategoria.gravar(Categoria(x, y['descricao']))
    
    @classmethod  
    def inclui_categoria(cls, categoria, descricao):
        return DalCategoria.gravar(Categoria(categoria, descricao))

    @classmethod    
    def lista_categoria(cls, dic_categoria):
        for x,y in dic_categoria.items():           
            print(colored(f'CATEGORIA : {x}  {y["descricao"]} ','light_green'))

    @classmethod  
    def valida_categoria(cls, dic_categoria, codigo):
        while True:
            if  codigo==9999:                        
                if (len(dic_categoria))==0:
                    print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                else:
                    CategoriaControler.lista_categoria(dic_categoria)
                codigo =input('Codigo da Categoria : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
            if codigo !=9999:
                return int(codigo)
                        
    @classmethod            
    def exclui_categoria(cls, dic_categoria, categoria,):
        
        dic_categoria.pop(categoria)
        DalCategoria.esvaziar()
        for x,y in dic_categoria.items():    
            res =DalCategoria.gravar(Categoria(x, y['descricao']))

class ProdutoControler:
    
    @classmethod
    def pega_todos_produtos(cls):

        dic_produtos=DalProduto.ler()
        return dic_produtos
          
    @classmethod   
    def alterar_produto(cls, dic_produto, produto, descricao, categoria,unidade, quantidade, valor ):

        if descricao != '': dic_produto[produto]['descricao' ]=descricao
        if categoria != '': dic_produto[produto]['categoria' ]=str(categoria)
        if categoria != '': dic_produto[produto]['unidade'   ]=unidade
        dic_produto[produto]['quantidade']=str(quantidade)
        dic_produto[produto]['valor'     ]=str(valor)
        DalProduto.esvaziar()

        for x,y in dic_produto.items():        
            res =DalProduto.gravar(Produto(x, y['descricao'], y['categoria'], y['unidade'], y['quantidade'], y['valor']))
    
    @classmethod  
    def inclui_produto(cls, produto, descricao, categoria, unidade, quantidade, valor):
        return DalProduto.gravar(Produto(produto, descricao, categoria, unidade, quantidade, valor))

    @classmethod    
    def lista_produto(cls, dic_produto):
        for x,y in dic_produto.items():           
            print(colored(f'PRODUTO : {x}  {y["descricao"]} Unidade : {y["unidade"]} Quantidade : {y["quantidade"]} Valor Unitario : {y["valor"]}' ,'light_green'))

    @classmethod  
    def valida_produto(cls, dic_produto, codigo,tipo):

        while True:
            if  codigo==9999:                        
                if len(dic_produto)==0:
                   print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                elif tipo in ('','C'):
                      ProdutoControler.lista_produto(dic_produto)
                elif tipo=='L': return int(codigo)
                codigo =input('Codigo do Produto : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
            if codigo !=9999:
                try:
                    desc = dic_produto[int(codigo)]['descricao']
                    break
                except:
                    if tipo !='C':
                        print(colored('Produto não Cadastrado', 'red'))
                        codigo =input('Codigo do Produto : ')
                        codigo = ConfirmacaoControler.numero_valido(codigo)
                    else: break

        return int(codigo)
                        
    @classmethod            
    def exclui_produto(cls, dic_produto, produto):
        
        dic_produto.pop(produto)
        DalCategoria.esvaziar()
        for x,y in dic_produto.items():    
            res =DalProduto.gravar(Produto(x, y['descricao'], y['categoria'], y['unidade'], y['quantidade'], y['valor']))

class ClienteControler:
    
    @classmethod
    def pega_todos_clientes(cls):

        dic_clientes=DalCliente.ler()
        return dic_clientes
          
    @classmethod   
    def alterar_clientes(cls, dic_clientes, clientes, nome, cidade, bairro, endereco, 
                                            complemento, numero, telefone , whatsapp):
        
        dic_clientes[clientes]['nome']       =nome       
        dic_clientes[clientes]['cidade']     =cidade     
        dic_clientes[clientes]['bairro']     =bairro     
        dic_clientes[clientes]['endereco']   =endereco   
        dic_clientes[clientes]['complemento']=complemento
        dic_clientes[clientes]['numero']     =numero     
        dic_clientes[clientes]['telefone']   =telefone   
        dic_clientes[clientes]['whatsapp']   =whatsapp   
        DalCliente.esvaziar()

        for x,y in dic_clientes.items():        
            res =DalCliente.gravar(Cliente(x, y['nome'],y['cidade'], y['bairro'], y['endereco'],
                                              y['complemento'],y['numero'],y['telefone'],
                                              y['whatsapp'] ))
    
    @classmethod  
    def inclui_clientes(cls, cliente, nome , cidade, bairro ,endereco ,complemento ,numero     
                           , telefone ,whatsapp):
     
        return DalCliente.gravar(Cliente(cliente ,nome ,cidade ,bairro ,endereco ,complemento ,numero,telefone ,whatsapp))

    @classmethod    
    def lista_clientes(cls, dic_clientes):
            
        for x,y in dic_clientes.items():        
            print(colored(f'CLIENTE : {x}  {y["nome"] }','light_green'))
            print(colored(f'         Endereço : {y["endereco"]} - {y["cidade"]} - {y["bairro"]} - {y["complemento"]} - {y["numero"]}','light_green'))
            print(colored(f'         Contato  : {y["telefone"]} - whatsapp : {y["whatsapp"]}','light_green'))

    @classmethod  
    def valida_clientes(cls, dic_clientes, clientes,tipo):
        while True:   
            if  clientes==9999:                        
                if (len(dic_clientes))==0:
                    print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                else:
                    ClienteControler.lista_clientes(dic_clientes)
                clientes =input('Codigo do Cliente : ')
                clientes = ConfirmacaoControler.numero_valido(clientes)
            if clientes !=9999:
                if tipo== 'C':
                    try:
                        cliente_des   = dic_clientes[clientes]['nome']
                        tipo=''
                        return clientes
                    except:
                        print(colored('Cliente não Cadastrado', 'red'))
                        clientes =input('Codigo do Cliente : ')
                        clientes = ConfirmacaoControler.numero_valido(clientes)
                else: return clientes
            
        return clientes
           
    @classmethod            
    def exclui_clientes(cls, dic_clientes, codigo):
      
        dic_clientes.pop(codigo)
        DalCliente.esvaziar()

        for x,y in dic_clientes.items():    
            res =DalCliente.gravar(Cliente(x, y['nome'], y['bairro'], y['endereco'],   
                                              y['complemento'], y['numero'], y['telefone'],
                                              y['whatsapp'] ))

class FornecedorControler:
    
    @classmethod
    def pega_todos_fornecedores(cls):

        dic_fornecedores=DalFornecedor.ler()
        return dic_fornecedores

    @classmethod
    def Valida_fornecedor(cls, dic_fornecedores, codigo,tipo):
        while True:
            if  codigo==9999:                        
                if len(dic_fornecedores)==0:
                   print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                elif tipo in ('','C'):
                      FornecedorControler.lista_fornecedores(dic_fornecedores)
                elif tipo=='C': return int(codigo)
                codigo =input('Codigo do Fornecedor : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
            if codigo !=9999:
                try:
                    desc = dic_fornecedores[int(codigo)]['nome']
                    break
                except:
                    if tipo !='C':
                        print(colored('Fornecedor não Cadastrado', 'red'))
                        codigo =input('Codigo do Fornecedor : ')
                        codigo = ConfirmacaoControler.numero_valido(codigo)
                    else: break
       
        return int(codigo)     

    @classmethod   
    def alterar_fornecedores(cls, dic_fornecedores, razao, cpf, codigo, nome, cidade, bairro, endereco,
                                            complemento, numero, telefone , whatsapp):
      
        dic_fornecedores[codigo]['razao']      =razao       
        dic_fornecedores[codigo]['cpf']        =cpf        
        dic_fornecedores[codigo]['nome']       =nome       
        dic_fornecedores[codigo]['cidade']     =cidade     
        dic_fornecedores[codigo]['bairro']     =bairro     
        dic_fornecedores[codigo]['endereco']   =endereco   
        dic_fornecedores[codigo]['complemento']=complemento
        dic_fornecedores[codigo]['numero']     =numero     
        dic_fornecedores[codigo]['telefone']   =telefone   
        dic_fornecedores[codigo]['whatsapp']   =whatsapp   
        DalFornecedor.esvaziar()

        for x,y in dic_fornecedores.items():        
            res =DalFornecedor.gravar(Fornecedor(y['razao'],y['cpf'], x, y['nome'],y['cidade'], y['bairro'], y['endereco'],
                                              y['complemento'],y['numero'],y['telefone'],
                                              y['whatsapp'] ))

    @classmethod  
    def inclui_fornecedores(cls, codigo, razao, cpf, nome ,cidade ,bairro ,endereco ,complemento ,numero    
                           , telefone ,whatsapp):
     
        return DalFornecedor.gravar(Fornecedor( cpf , razao, codigo, nome ,cidade ,bairro ,endereco ,complemento ,numero,telefone ,whatsapp))

    @classmethod    
    def lista_fornecedores(cls, dic_fornecedores):
            
        for x,y in dic_fornecedores.items():        
            print(colored(f'FORNECEDOR : {x}  {y["razao"]} Cpf/CGC : {y["cpf"]} - {y["nome"] }','light_green'))
            print(colored(f'         Endereço : {y["endereco"]} - {y["cidade"]} - {y["bairro"]} - {y["complemento"]} - {y["numero"]}','light_green'))
            print(colored(f'         Contato  : {y["telefone"]} - whatsapp : {y["whatsapp"]}','light_green'))


    @classmethod            
    def exclui_fornecedores(cls, dic_fornecedores, codigo):
      
        dic_fornecedores.pop(codigo)
        DalFornecedor.esvaziar()

        for x,y in dic_fornecedores.items():        
            res =DalFornecedor.gravar(Fornecedor(y['razao'],y['cpf'], x, y['nome'],y['cidade'], y['bairro'], y['endereco'],
                                              y['complemento'],y['numero'],y['telefone'],
                                              y['whatsapp'] ))

class FuncionarioControler:
    
    @classmethod
    def pega_todos_Funcionarios(cls):

        dic_funcionarios=DalFuncionario.ler()
        return dic_funcionarios
          
    @classmethod   
    def alterar_funcionarios(cls, dic_funcionarios, codigo , nome, funcao , telefone, qtd_hora_trab ,valor_hora):
      
        dic_funcionarios[codigo]['nome']         =nome       
        dic_funcionarios[codigo]['funcao']       =funcao     
        dic_funcionarios[codigo]['telefone']     =telefone     
        dic_funcionarios[codigo]['qtd_hora_trab']=qtd_hora_trab   
        dic_funcionarios[codigo]['valor_hora']   =valor_hora
     
        DalFornecedor.esvaziar()

        for x,y in dic_funcionarios.items():  
            res =DalFuncionario.gravar(Funcionario(y['funcao'],y['qtd_hora_trab'],y['valor_hora'], x, y['nome'],'', '', '','',y['telefone'],'' ))
            
    @classmethod  
    def inclui_funcionarios(cls, codigo , nome, funcao , telefone, qtd_hora_trab ,valor_hora):
     
        return DalFuncionario.gravar(Funcionario(funcao, qtd_hora_trab, valor_hora , codigo, nome,'', '', '', '','',telefone,''))

    @classmethod    
    def lista_funcionarios(cls, dic_funcionarios):
            
        for x,y in dic_funcionarios.items():   
            print(colored(f'FUNCIONARIO  : {x}    {y["nome"]} FUNCAO : {y["funcao"]} - {y["telefone"] }','light_green'))
            print(colored(f'       CARGA HOARIA : {y["qtd_hora_trab"]} - VALOR HORA : {y["valor_hora"]} - VALOR SALARIO : {y["salario"]}',\
                                                  'light_green'))
    @classmethod  
    def valida_funcionario(cls, dic_funcionarios, codigo):
        while True:
            if  codigo==9999:                        
                if (len(dic_funcionarios))==0:
                    print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                else:
                    FuncionarioControler.lista_funcionarios(dic_funcionarios)
                codigo =input('Codigo do Funcionario : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
            if codigo !=9999:
                break 
        
        return int(codigo)
               
    @classmethod            
    def exclui_funcionarios(cls, dic_funcionarios, codigo):
      
        dic_funcionarios.pop(codigo)
        DalFuncionario.esvaziar()

        for x,y in dic_funcionarios.items():        
            res =DalFuncionario.gravar(Funcionario(y['funcao'],y['qtd_hora_trab'],y['valor_hora'], x, y['nome'], '','','','','',y['telefone'],''))

class MovimentoControler:
    @classmethod
    def verifica_saldo(cls, tipo_doc ,quantidade, qtd_estoque):
         
        while True:

            if tipo_doc in ('VV','DC'):
                if  quantidade > int(qtd_estoque):
                    print(colored('Quantidade Maior que o Estoque, Digite nova Quantidade','red'))                 
                    quantidade = input(colored(f'Saldo {qtd_estoque}  - Nova Quantidade : ','blue'))
                    quantidade = ConfirmacaoControler.numero_valido(quantidade)
                else: return quantidade
            else: return quantidade

    @classmethod
    def pega_todos_Movimento(cls):

        dic_geral, seq, datafim =DalMovimento.ler()
        return dic_geral, seq, datafim
    
    @classmethod
    def pega_todos_movimento_dia(cls, dic_geral, pk_movimento):
        seq=0
        mov={}
        try:
            
            dic_ordenado = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
            dic_geral = dic_ordenado
            mov = dict(filter(lambda item: item[0].startswith(str(pk_movimento)) , dic_geral.items()))
            seq=list(mov.keys())[-1]   
        except:
               mov={}
               seq='0'
        return mov,seq  
     
    @classmethod
    def existe_venda_produto(cls, dic_geral, produto, pk_movimento):

        existe_venda={}
        dic_geral    = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
        existe_venda = dict(filter(lambda item: int(item[0]) >= int(pk_movimento) 
                    and item[1]['produto']  == int(produto)
                    and item[1]['tipo_doc'] in ('VV','DV'), dic_geral.items()))    
        return existe_venda

    @classmethod
    def ultimo_movimento_produto(cls, dic_geral, produto, ind_pesquisa,dic_itens, prod,tipo_doc):
 
        existe_venda={}
        dic_geral = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
        try:

            mov = dict(filter(lambda item: int(item[0]) <= int(ind_pesquisa) 
                        and item[1]['produto'] == int(produto), dic_geral.items()))
            existe_venda=MovimentoControler.existe_venda_produto(dic_geral,produto, ind_pesquisa)            

            if len(mov) > 0:
                if len(existe_venda)==0:
                    if produto in prod:
                        mov_key = list(mov.keys())[-2]
                    else: mov_key = list(mov.keys())[-1]
                    
                    qtd_atual = mov[mov_key]['qtd_atual']
                    valor_atual=mov[mov_key]['valor_atual']
                elif tipo_doc in ('VV','DC') :
                    if produto in prod:
                        mov_key = list(mov.keys())[-2]
                    else: mov_key = list(mov.keys())[-1]
                    qtd_atual = mov[mov_key]['qtd_atual']
                    valor_atual=mov[mov_key]['valor_atual']
                else:
                    mov_key = 0
                    qtd_atual=0
                    valor_atual=0 
            else:
               dic_produtos  = ProdutoControler.pega_todos_produtos()
               qtd_atual     = int(dic_produtos[int(produto)]['quantidade'])
               valor_atual   = float(dic_produtos[int(produto)]['valor'])
               mov_key = 0

        except:
            mov_key=0
            qtd_atual=0
            valor_atual=0

        return mov_key, qtd_atual, valor_atual, existe_venda
    
    @classmethod    
    def pega_todos_movimento_data(cls, dic_movimento, data_index):
        
        sequencias={}
        try:       
          sequencias  =list(set([dic_movimento[chave]['sequencia'] 
                       for chave in filter(lambda chave: chave.startswith(str(data_index)),
                           dic_movimento.keys())]))
         
        except:
            pass
 
        return sequencias
    @classmethod
    def filtra_movimento(cls, dic_geral, dat_inicial, dat_final, documento, produto):
        pk_mov1= str(dat_inicial) + '00000' + '00000'
        pk_mov2= str(dat_final  ) + '99999' + '99999'
        dic_ordenado  = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
        if int(produto) != 9999:
            geral = dict(filter(lambda item: item[0] >= pk_mov1 and item[0] <= pk_mov2 and item[1]['produto'] ==int(str(produto)), dic_ordenado.items()))
        else:
            geral = dict(filter(lambda item: item[0] >= pk_mov1 and item[0] <= pk_mov2, dic_ordenado.items()))

        return geral
 
    @classmethod    
    def lista_movimentos(cls, dic_movimentos):
        qtd_atu=0
        valor_atu=0
        produto_ant=0

        dic_movimentos = dict(sorted(dic_movimentos.items(), key=lambda x: ( x[1]['produto'],x[1]['data_movimento'], 
                                                                       x[1]['sequencia'])))
        
        for x,y in dic_movimentos.items():   

            data_mov = str(x)[0:8]
            data_mov = datetime.strptime( data_mov, '%Y%m%d')
            data_mov = data_mov.strftime('%d/%m/%Y')
            
            if str(y["sequencia"]) in ("C","DC"):
                dic_clientes    = ClienteControler.pega_todos_clientes()               
            else:
                dic_clientes  = FornecedorControler.pega_todos_fornecedores()  
            cliente_cod = int(y["cliente"])
            cliente_des = dic_clientes[cliente_cod] ['nome']
            dic_produto = ProdutoControler.pega_todos_produtos()               
            produto_cod = int(y["produto"])
            produto_des = dic_produto[produto_cod] ['descricao']
            if (produto_cod != produto_ant):
                print(colored(f'PRODUTO  : {y["produto"]} - {produto_des} ','light_green'))
                produto_ant = int(y["produto"])

            print(colored(f'{data_mov}  DOCUMENTO : {str(y["sequencia"])} TIPO : {y["tipo_doc"]} Movimento ->Qtd. {str(y["quantidade"])} - VAL. {str(y["valor"])} Estoque -> Quant.: {str(y["qtd_atual"])} Valor : {str(y["valor_atual"])}','light_green'))


        #===== Limpa dicionario apos Listagem
        dic_movimento={}

    @classmethod
    def manutencao_itens(cls, dic_geral, dic_items, tipo_doc, cliente, pk_movimento):
        lst_excluido  =[]
        prod          ={}
        seq           =0
        dic_produtos  = ProdutoControler.pega_todos_produtos()  
       
        chave = str(pk_movimento)
 
        data_movimento =chave[6:8] +'/'+\
                        chave[4:6] +'/'+\
                        chave[0:4] 

        sequencia     =chave[8:13]
        data_invertida=chave[0:8]
        ind_pesquisa=''

        while True:            
            if len(dic_items) > 0:
                prod=list(set([dic_items[chave]['produto'] for chave in filter(lambda chave: 
                                                       chave.startswith(str(pk_movimento)) , dic_items.keys())]))
                print(colored(f' Produtos cadastrados no documento - { prod } ', 'green'))
            chave         = str(pk_movimento)
            produto       = input(colored('Codigo Produto  : ','blue'))
            produto       = ConfirmacaoControler.numero_valido(produto)   
            if produto == 0:
               return dic_items, lst_excluido
               break
                   
            produto       = ProdutoControler.valida_produto(dic_produtos, produto,'C')  
            produto_des   = dic_produtos[int(produto)]['descricao']
            qtd_estoque   = int(dic_produtos[int(produto)]['quantidade'])
            valor_estoque = float(dic_produtos[int(produto)]['valor'])
            print(colored(f'{produto_des}','green'))   

            produto_format = '{:0>5}'.format(produto)
            chave = chave + produto_format
            ind_pesquisa=data_invertida + sequencia + '99999'
            qtd_ant  =0            
            valor_ant=0
            chave_ant=0
            qtd_atual=0
            valor_atual=0

            try:                   
                chave_ant, qtd_ant, valor_ant,existe_venda = MovimentoControler.ultimo_movimento_produto(dic_geral,
                                                                     produto_format, ind_pesquisa,dic_items, prod, tipo_doc)
                if tipo_doc in ('CC', 'DC') and len(existe_venda)>0:
                    print(colored(f"Existe venda futuras, não pode Alterar o preço Médio.",'red'))
                    continue

                qtd_mov    = dic_items[chave]['quantidade']
                quantidade = dic_items[chave]['quantidade']
                valor      = dic_items[chave]['valor']
                print(colored(f'Quantidade      {str(quantidade)}   ','green'))
                print(colored(f'Valor Unitário  {str(valor )} ','green'))
                conf =  ConfirmacaoControler.deseja_alterar_excluir(' Este Produto ')
                
                if conf=='A':
                    if valor_ant > 0:
                       valor_atual=dic_geral[chave_ant]['valor_atual']                    
               
                    if chave_ant == chave:
                        qtd_ant  =0
                        valor_ant=0
                        chave_ant=0
                        dic_geral.pop(chave)            
                                     
                    quantidade = input(colored(f'Quantidade : {quantidade}  - Novo : ','blue'))
                    quantidade = ConfirmacaoControler.numero_valido(quantidade)
                    if tipo_doc in('VV','DC'):
                          qtd=int(qtd_estoque)+int(qtd_mov)
                    else: qtd=int(qtd_estoque)

                    quantidade = MovimentoControler.verifica_saldo(tipo_doc,quantidade,qtd)
 
                    if tipo_doc in ('CC','DC'):
                        valor      = input(colored(f'Valor  : {valor}  - Novo : ','blue'))
                        valor      = ConfirmacaoControler.valor_valido(valor) 
                    else: valor=valor_atual
                    
                    print(colored(f' Total do produto : {str(quantidade * valor)}', 'red'))
                  
                    conf= ConfirmacaoControler.confirmacao('Confirma alteração do Produto :')
                    if conf=='S':               
                        dic_items[chave] ={'data_movimento' :data_movimento,
                                            'sequencia'     :int(sequencia),
                                            'tipo_doc'      :tipo_doc,
                                            'cliente'       :int(cliente),
                                            'produto'       :produto,
                                            'quantidade'    :quantidade,
                                            'valor'         :valor,
                                            'qtd_anterior'  :qtd_ant,
                                            'valor_anterior':valor_ant,
                                            'qtd_atual'     : 0,
                                            'valor_atual'   : 0,
                                            'chave_anterior':chave_ant
                                    }       
                else:
                    if conf=='E':
                        conf= ConfirmacaoControler.confirmacao('Confirma exclusao do produto :')
                        if conf=='S':               
                            dic_items.pop(chave)
                            lst_excluido.append(chave)
                            seq+=1
                    else:
                        dic_items={}
            except:    

                if valor_ant > 0:
                   valor_atual=dic_geral[chave_ant]['valor_atual']
                   qtd_estoque=dic_geral[chave_ant]['qtd_atual']
                else:
                   valor_atual=valor_estoque

                print(colored(f'Quantidade Estoque {str(qtd_estoque)}  ','green'))              
                print(colored(f'Valor   Atual      {str(valor_atual)} ','green'))
                quantidade = input(colored(f'Quantidade : ','blue'))
                quantidade = ConfirmacaoControler.numero_valido(quantidade)
                quantidade =MovimentoControler.verifica_saldo(tipo_doc,quantidade,qtd_estoque)

                if tipo_doc in ('CC','DC'):
                    valor      = input(colored('Valor      : ','blue'))
                    valor      = ConfirmacaoControler.valor_valido(valor) 
                else: valor=float(valor_atual)
                
                print(colored(f'====== Total do Produtos : {str(quantidade * valor)}', 'red'))
                        
                conf= ConfirmacaoControler.confirmacao('Confirma inclusao do produto :')
                if  conf=='S' :
                    dic_items[chave]={ 'data_movimento':data_movimento,
                                       'sequencia'     :sequencia,
                                       'tipo_doc'      :tipo_doc,
                                       'cliente'       :cliente,
                                       'produto'       :produto,
                                       'quantidade'    :quantidade,
                                       'valor'         :valor,
                                       'qtd_anterior'  :qtd_ant,
                                       'valor_anterior':valor_ant,
                                       'qtd_atual'     : 0,
                                       'valor_atual'   : 0,
                                       'chave_anterior':chave_ant
                                    } 

    @classmethod
    def total_movimento(cls, dic_movimentos):
        total=0.0
        for chave in dic_movimentos:
            quantidade = dic_movimentos[chave]['quantidade']  
            valor      = dic_movimentos[chave]['valor']
            total += quantidade * valor
        return total
    
    @classmethod  
    def inclui_movimento(cls, dic_geral, dic_movimento, lst_excluido):
        dic_produto = ProdutoControler.pega_todos_produtos()
        
        if lst_excluido:
            for item in lst_excluido.items():
                dic_geral.pop(item)

        if dic_movimento:
            # Atualiza no dicionario geral o produto do movimento 
            dic_geral = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
            for chave, itens in dic_movimento.items():
                ind = str(chave[0:13]) + '00000'
                geral = {item: dic_geral[item] for item in dic_geral if item < ind and dic_geral[item]['produto'] == itens['produto']}
                geral = dict(sorted(geral.items(), key=lambda x: x[0]))
                p = Movimento(chave,**itens)
               
                if geral:
                    mov_key = list(geral.keys())[-1]
                    
                    p.qtd_anterior  =geral[mov_key]['qtd_atual']
                    p.valor_anterior=geral[mov_key]['valor_atual']
                    p.chave_anterior=mov_key            
                else:
                    p.qtd_anterior  =0
                    p.valor_anterior=0
                    p.chave_anterior=0

                p.saldo_atual()
                # Atualiza o dicionário geral com o item do movimento atual
                dic_geral[chave]={ 'data_movimento':p.data_movimento,
                        'sequencia'     :str(int(p.sequencia)),
                        'tipo_doc'      :p.tipo_doc,
                        'cliente'       :str(int(p.cliente)),
                        'produto'       :p.produto,
                        'quantidade'    :p.quantidade,
                        'valor'         :p.valor,
                        'qtd_anterior'  :p.qtd_anterior,
                        'valor_anterior':p.valor_anterior,
                        'qtd_atual'     :p.qtd_atual,
                        'valor_atual'   :p.valor_atual,
                        'chave_anterior':p.chave_anterior}   
                
            # Atualizar no dicionario geral todos as data a frente do produto movimentado

            for chave, itens in dic_movimento.items():
                ind = str(chave[0:13]) + '00000'
                geral = {item: dic_geral[item] for item in dic_geral if item >= ind and dic_geral[item]['produto'] == itens['produto']}
                geral = dict(sorted(geral.items(), key=lambda x: x[0]))
                mov_key = list(geral.keys())[0]
             
                qtd_anterior  =geral[mov_key]['qtd_anterior']
                valor_anterior=geral[mov_key]['valor_anterior']
                chave_anterior=geral[mov_key]['chave_anterior']            

                for chave, itens in geral.items():
                    p = Movimento(chave,**itens)

                    p.qtd_anterior  =qtd_anterior
                    p.valor_anterior=valor_anterior
                    p.chave_anterior=chave_anterior

                    p.saldo_atual()
                    # Atualiza o dicionário geral com o item atual
                    dic_geral[chave]={ 'data_movimento':p.data_movimento,
                            'sequencia'     :str(int(p.sequencia)),
                            'tipo_doc'      :p.tipo_doc,
                            'cliente'       :str(int(p.cliente)),
                            'produto'       :p.produto,
                            'quantidade'    :p.quantidade,
                            'valor'         :p.valor,
                            'qtd_anterior'  :p.qtd_anterior,
                            'valor_anterior':p.valor_anterior,
                            'qtd_atual'     :p.qtd_atual,
                            'valor_atual'   :p.valor_atual,
                            'chave_anterior':p.chave_anterior}  
                    
                    qtd_anterior  =geral[chave]['qtd_atual']
                    valor_anterior=geral[chave]['valor_atual']
                    chave_anterior=chave       
                    
            # grava no Arquivo e atualiza a posição do estoque no produto
                                  
            DalMovimento.esvaziar()
            dic_geral = dict(sorted(dic_geral.items(), key=lambda x: x[0]))
            for chave, valor in dic_geral.items():
                DalMovimento.gravar(Movimento(chave,**valor))
                ProdutoControler.alterar_produto(dic_produto, valor['produto'], '', '','',
                                                              valor['qtd_atual'],
                                                              valor['valor_atual'] )
   
    @classmethod    
    def valida_movimento(cls, dic_movimento, data_fim):
        
        while True:
            if  data_fim=='9999':                        
                if (len(dic_movimento))==0:
                    print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                else:
                    MovimentoControler.lista_movimentos(dic_movimento)
                    data_fim =input('Data do Movimento : ')
                    data_fim = str(ConfirmacaoControler.valida_data(data_fim,1))
            if data_fim !='9999':
                break

        return data_fim

    @classmethod    
    def valida_movimento_seq(cls, dic_movimento, sequencia, seq, data_fim, data_mov, lis_seq):
        erro=0
        while True:
            if  str(sequencia)=='9999':                        
                if (len(dic_movimento))==0:
                    print(colored('Sem Registro para Listar  \n','cyan', attrs=['bold']))  
                else:
                    MovimentoControler.lista_movimentos(dic_movimento)
                    sequencia = input(f'Ultimo Documento [{seq}] Numero Documento  : ')
                    sequencia = ConfirmacaoControler.numero_valido(sequencia)
            elif sequencia==0:
                return sequencia
             
            elif sequencia > (int(seq)):
                print(colored(f'Documento fora da Sequencia ultimo Documento {seq}  \n','cyan', attrs=['bold']))   
                sequencia = input(f'Ultimo Documento [{seq}] Numero Documento  : ')
                sequencia = ConfirmacaoControler.numero_valido(sequencia)

            elif data_mov < data_fim:   
               if sequencia == int(seq):
                  break       
               if sequencia not in lis_seq and sequencia < int(seq):
                  sequencia = input(colored(f'So pode Alterar esse(s) documento(s) {lis_seq} ou ' +
                                 f'incluir uma novo Documento {seq} - Documento : ','cyan', attrs=['bold']))
                  sequencia = ConfirmacaoControler.numero_valido(sequencia)
               elif  sequencia in lis_seq:
                   break

            elif data_mov > data_fim:
                if sequencia == int(seq) or sequencia in lis_seq:
                    break
                if sequencia not in lis_seq and sequencia < int(seq):
                    sequencia = input(colored(f'So pode Alterar esse(s) documento(s) {lis_seq} ou ' +
                                 f'incluir uma novo Documento {seq} - Documento : ','cyan', attrs=['bold']))
                    sequencia = ConfirmacaoControler.numero_valido(sequencia)
            elif data_mov == data_fim:
                if sequencia == int(seq) or sequencia in lis_seq:
                   break
                elif sequencia not in lis_seq and sequencia < int(seq):
                    sequencia = input(colored(f'So pode alterar esse(s) documento(s){lis_seq} ou ' +
                                f'incluir um novo Documento {seq}  - Documento : ','cyan', attrs=['bold']))
                    sequencia = ConfirmacaoControler.numero_valido(sequencia)

        return sequencia
