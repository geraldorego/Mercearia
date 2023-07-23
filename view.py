from controller import ConfirmacaoControler, CategoriaControler, ClienteControler, FornecedorControler, FuncionarioControler,\
                    ProdutoControler, MovimentoControler
import os.path
from termcolor import colored
from datetime import datetime 
def criaArquivo(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

criaArquivo('categoria.txt','produto.txt','estoque.txt','movimento.txt','cliente.txt',
            'fornecedor.txt','funcionario.txt')

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print (colored('=========== SISTEMA DE VENDAS ===========\n','red', attrs=['bold']))
        
        modulo = input(colored('Opção :  1 - Cadastro de Categoria  \n'
                            '         2 - Cadastro de Produto    \n' 
                            '         3 - Cadastro de Cliente    \n'
                            '         4 - Cadastro de Fornecedor \n'
                            '         5 - Cadastro de Funcionario\n'
                            '         6 - Movimentação           \n'   
                            '         7 - Lista Posição do Estoque\n' 
                            '         8 - Lista Movimentação no periodo\n'                                                           
                            '         0 - Finalizar Sistema      \n'
                            'Informe a Opção :','blue', attrs=['bold']
                            )
                    )
                
        while not modulo.isnumeric():
            modulo = input(colored('Digite um opcão válida: ','yellow'))
        
        modulo=int(modulo)                           

        if modulo==1:     #===================== categoria   ===============================
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('=========== CADASTRO DE CATEGORIA =========== ')
                print (colored('==== Digite <9999> para Listar as categorias==','yellow'))
                print (colored('==== Digite <0>    para Sair do Cadastro =====','yellow'))
                
                dic_categoria = CategoriaControler.pega_todas_categoria()
                codigo =input('Codigo da Categoria : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
     
                codigo=CategoriaControler.valida_categoria(dic_categoria, codigo)

                if codigo==0000:
                    break
                    
                try:
                    descricao = dic_categoria[codigo]['descricao']
                    descricao= print(f'Descricao : {descricao} \n')
                    conf =  ConfirmacaoControler.deseja_alterar_excluir('')

                    if conf == 'A':    ####  Alteração
                        descricao= input(colored(' Nova Descricao : ','blue')).upper()
                        CategoriaControler.alterar_categoria(dic_categoria, codigo, descricao)
                        x=input('=== Alteração com sucesso === < Tecle Enter > ')

                    elif conf =='E':  ####  Exclusão
                        CategoriaControler.exclui_categoria(dic_categoria, codigo)
                        x=input('=== Exclusão com sucesso === < Tecle Enter >')

                except:   ### Inclusão
                    
                    descricao= str(input('Descricao : ').upper())
                    if ConfirmacaoControler.confirmacao('Confirma Incluir : ')=='S':
                        if CategoriaControler.inclui_categoria(codigo, descricao):
                            x=input('=== Inclusão com sucesso === < Tecle Enter >')
                        else:  x=input('=== Erro ao Incluir === < Tecle Enter >')

        elif modulo==2:    #=============================== Produto =========================
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('=========== CADASTRO DE PRODUTO =========== ')
                print (colored('==== Digite <9999> para Lista o Cadastro =====','yellow'))
                print (colored('==== Digite <0>    para Sair do Cadastro =====','yellow'))

                dic_categoria = CategoriaControler.pega_todas_categoria()
                dic_produto   = ProdutoControler.pega_todos_produtos()  

                codigo =input('Codigo do Produto : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
                codigo =ProdutoControler.valida_produto(dic_produto, codigo,'C')

                if codigo==0000:
                    break
                
                try:
                    descricao     = dic_produto[codigo]     ['descricao']
                    categoria     = int(dic_produto[codigo] ['categoria'])
                    categoria_des = dic_categoria[categoria]['descricao']    
                    unidade       = dic_produto[codigo]     ['unidade']
                    quantidade    = dic_produto[codigo]     ['quantidade']
                    valor         = dic_produto[codigo]     ['valor']

                    conf =  ConfirmacaoControler.deseja_alterar_excluir('')

                    if conf == 'A':    ####  Alteração
                        descricao  = input(colored(f' Descricao : {descricao} - Nova : ','blue')).upper()
                        categoria  = input(colored(f' Categoria : {categoria} - {categoria_des}  - Nova : ','blue'))

                        categoria  =ConfirmacaoControler.numero_valido(categoria)        
                        categoria  =CategoriaControler.valida_categoria(dic_categoria, categoria)  
                                      
                        unidade    = input(colored(f' Unidade   : {unidade} - Nova : ','blue')).upper()
                        print(colored(f' Quantidade: {quantidade}','green'))
                        print(colored(f' Novo Valor: {valor}','green'))

                        ProdutoControler.alterar_produto(dic_produto, codigo, descricao, categoria ,unidade,\
                                                          quantidade, valor)
                        x=input('=== Alteração com sucesso === < Tecle Enter > ')

                    elif conf =='E':  ####  Exclusão
                        ProdutoControler.exclui_produto(dic_produto, codigo)
                        x=input('=== Exclusão com sucesso === < Tecle Enter >')

                except:   ### Inclusão
                    
                    descricao  = str(input('Descricao : ').upper())

                    while True:
                        categoria  = input(colored('Categoria : ','blue'))
                        
                        categoria  = ConfirmacaoControler.numero_valido(categoria)
                        categoria  = CategoriaControler.valida_categoria(dic_categoria, categoria) 
                        try:  
                           print(colored(f'{dic_categoria[categoria]["descricao"]}','green'))
                           break
                        except:
                           print(colored(' ===> Categoria não Cadastrada','red'))
                    
                    unidade    = input(colored('Unidade   : ','blue')).upper()
                    quantidade = input(colored('Quantidade: ','blue'))
                    quantidade = ConfirmacaoControler.numero_valido(quantidade)
                    valor      = input(colored('Valor      : ','blue'))
                    valor      = ConfirmacaoControler.valor_valido(valor) 

                    if ConfirmacaoControler.confirmacao('Confirma Incluir : ')=='S':
                        if ProdutoControler.inclui_produto(codigo, descricao, categoria, unidade,quantidade,valor):
                            x=input('=== Inclusão com sucesso === < Tecle Enter >')
                        else:  x=input('=== Erro ao Incluir === < Tecle Enter >')

        elif modulo==3:     # ===================================  CLIENTES  =====================================
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('============== CADASTRO DE CLIENTES ============== ')
                print (colored('==== Digite <9999> para Listar os clientes ===','yellow'))
                print (colored('==== Digite <0>    para Sair do Cadastro =====','yellow'))
                
                dic_clientes = ClienteControler.pega_todos_clientes()
                
                codigo =input('Codigo do Cliente : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
                codigo = ClienteControler.valida_clientes(dic_clientes, codigo,'')
                
                if codigo==0000:
                    break
                    
                try:
                    nome       =print(f'Nome        : {dic_clientes[codigo]["nome"]}')
                    cidade     =print(f'Cidade      : {dic_clientes[codigo]["cidade"]}')     
                    bairro     =print(f'Bairro      : {dic_clientes[codigo]["bairro"]}')     
                    endereco   =print(f'Endereço    : {dic_clientes[codigo]["endereco"]}')   
                    complemento=print(f'Complemento : {dic_clientes[codigo]["complemento"]}')
                    numero     =print(f'Numero      : {dic_clientes[codigo]["numero"]}')     
                    telefone   =print(f'Telefone    : {dic_clientes[codigo]["telefone"]}')   
                    whatsapp   =print(f'Whatsapp    : {dic_clientes[codigo]["whatsapp"]}') 

                    conf =  ConfirmacaoControler.deseja_alterar_excluir('')

                    if conf == 'A':    ####  Alteração
                        nome       =str(input(colored('Novo Nome        : ','blue')).upper())   
                        cidade     =str(input(colored('Nova Cidade      : ','blue')).upper())   
                        bairro     =str(input(colored('Novo Bairro      : ','blue')).upper())       
                        endereco   =str(input(colored('Novo Endereço    : ','blue')).upper())   
                        complemento=str(input(colored('Novo Complemento : ','blue')).upper())   
                        numero     =str(input(colored('Novo Numero      : ','blue')).upper())       
                        telefone   =str(input(colored('Novo Telefone    : ','blue')).upper())     
                        whatsapp   =str(input(colored('Novo Whatsapp    : ','blue')).upper())   
                        ClienteControler.alterar_clientes(dic_clientes, codigo, nome, cidade, bairro, endereco, 
                                            complemento, numero, telefone , whatsapp)
                        x=input('=== Alteração com sucesso === < Tecle Enter > ')

                    elif conf =='E':  ####  Exclusão
                        ClienteControler.exclui_clientes(dic_clientes, codigo)
                        x=input('=== Exclusão com sucesso === < Tecle Enter >')

                except:   ### Inclusão
                    
                    nome       =str(input('Nome        : ').upper())   
                    cidade     =str(input('Cidade      : ').upper())   
                    bairro     =str(input('Bairro      : ').upper())       
                    endereco   =str(input('Endereço    : ').upper())   
                    complemento=str(input('Complemento : ').upper())   
                    numero     =str(input('Numero      : ').upper())       
                    telefone   =str(input('Telefone    : ').upper())     
                    whatsapp   =str(input('Whatsapp    : ').upper())   

                    if ConfirmacaoControler.confirmacao('Confirma Incluir : ')=='S':
                        if ClienteControler.inclui_clientes(codigo ,nome ,cidade ,bairro ,endereco ,complemento ,numero     
                                                            , telefone ,whatsapp):
                             
                            x=input('=== Inclusão com sucesso === < Tecle Enter >')
                        else:  x=input('=== Erro ao Incluir === < Tecle Enter >')

        elif modulo==4:     # ===================================  FORNECEDOR  =====================================
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('============== CADASTRO DE FORNECDORES ============== ')
                print (colored('==== Digite <9999> para Listar os Fornecedor ===','yellow'))
                print (colored('==== Digite <0>    para Sair do Fornecedor =====','yellow'))
                
                dic_fornecedores = FornecedorControler.pega_todos_fornecedores()
                
                codigo =input('Codigo do Fornecedor : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
                codigo = FornecedorControler.Valida_fornecedor(dic_fornecedores, codigo, 'C')
                
                if codigo==0000:
                    break
                    
                try:
                    razao      =print(f'Razao Social: {dic_fornecedores[codigo]["razao"]}')
                    cpf        =print(f'Cpf         : {dic_fornecedores[codigo]["cpf"]}')
                    nome       =print(f'Contato     : {dic_fornecedores[codigo]["nome"]}')
                    funcao     =print(f'Funca       : {dic_fornecedores[codigo]["funcao"]}')     
                    bairro     =print(f'Bairro      : {dic_fornecedores[codigo]["bairro"]}')     
                    endereco   =print(f'Endereço    : {dic_fornecedores[codigo]["endereco"]}')   
                    complemento=print(f'Complemento : {dic_fornecedores[codigo]["complemento"]}')
                    numero     =print(f'Numero      : {dic_fornecedores[codigo]["numero"]}')     
                    telefone   =print(f'Telefone    : {dic_fornecedores[codigo]["telefone"]}')   
                    whatsapp   =print(f'Whatsapp    : {dic_fornecedores[codigo]["whatsapp"]}') 


                    conf =  ConfirmacaoControler.deseja_alterar_excluir('')

                    if conf == 'A':    ####  Alteração
                        razao      =str(input(colored('Razao Social: ','blue')).upper())   
                        cpf        =str(input(colored('Cpf/CGC     : ','blue')).upper())   
                        nome       =str(input(colored('Nome        : ','blue')).upper())   
                        cidade     =str(input(colored('Cidade      : ','blue')).upper())   
                        bairro     =str(input(colored('Bairro      : ','blue')).upper())       
                        endereco   =str(input(colored('Endereço    : ','blue')).upper())   
                        complemento=str(input(colored('Complemento : ','blue')).upper())   
                        numero     =str(input(colored('Numero      : ','blue')).upper())       
                        telefone   =str(input(colored('Telefone    : ','blue')).upper())     
                        whatsapp   =str(input(colored('Whatsapp    : ','blue')).upper())   
                        FornecedorControler.alterar_fornecedores(dic_fornecedores, razao, cpf, codigo, nome, cidade, bairro, endereco, 
                                            complemento, numero, telefone , whatsapp)
                        x=input('=== Alteração com sucesso === < Tecle Enter > ')

                    elif conf =='E':  ####  Exclusão
                        FornecedorControler.exclui_fornecedores(dic_fornecedores, codigo)
                        x=input('=== Exclusão com sucesso === < Tecle Enter >')

                except:   ### Inclusão
                    
                    razao      =str(input('Razão Social: ').upper())   
                    cpf        =str(input('Cpf/CGC     : ').upper())   
                    nome       =str(input('Contato     : ').upper())   
                    cidade     =str(input('Cidade      : ').upper())   
                    bairro     =str(input('Bairro      : ').upper())       
                    endereco   =str(input('Endereço    : ').upper())   
                    complemento=str(input('Complemento : ').upper())   
                    numero     =str(input('Numero      : ').upper())       
                    telefone   =str(input('Telefone    : ').upper())     
                    whatsapp   =str(input('Whatsapp    : ').upper())   

                    if ConfirmacaoControler.confirmacao('Confirma Incluir : ')=='S':
                        if FornecedorControler.inclui_fornecedores(codigo , razao, cpf, nome ,cidade ,bairro ,endereco ,complemento ,numero     
                                                            , telefone ,whatsapp):                             
                            x=input('=== Inclusão com sucesso === < Tecle Enter >')                            
                        else:  x=input('=== Erro ao Incluir === < Tecle Enter >')

        elif modulo==5:     # ===================================  FUNCIONARIO  =====================================
           
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('============== CADASTRO DE FUNCIONARIO ============== ')
                print (colored('==== Digite <9999> para Listar os Funcionarior ===','yellow'))
                print (colored('==== Digite <0>    para Sair do Cadastro      =====','yellow'))
                
                dic_funcionarios= FuncionarioControler.pega_todos_Funcionarios()
                
                codigo =input('Codigo do Funcionario : ')
                codigo = ConfirmacaoControler.numero_valido(codigo)
                codigo = FuncionarioControler.valida_funcionario(dic_funcionarios, codigo)                

                if codigo==0:
                    break
   
                try:
                    nome         =print(f'Nome         : {dic_funcionarios[codigo]["nome"]}')
                    funcao       =print(f'Função       : {dic_funcionarios[codigo]["funcao"]}')     
                    telefone     =print(f'Telefone     : {dic_funcionarios[codigo]["telefone"]}')     
                    qtd_hora_trab=print(f'Carga Horária: {dic_funcionarios[codigo]["qtd_hora_trab"]}')   
                    valor_hora   =print(f'Valor Hora   : {dic_funcionarios[codigo]["valor_hora"]}')
                    print(f'Salario      : {dic_funcionarios[codigo]["salario"]}')

                    conf =  ConfirmacaoControler.deseja_alterar_excluir('')

                    if conf == 'A':    ####  Alteração
                        nome         =str(input(colored('Nome         : ','blue')).upper())   
                        funcao       =str(input(colored('Função       : ','blue')).upper())   
                        telefone     =str(input(colored('Telefone     : ','blue')).upper())       
                        qtd_hora_trab=(input(colored('Carga Horária: ','blue')).upper())   
                        qtd_hora_trab = ConfirmacaoControler.numero_valido(qtd_hora_trab)
                        valor_hora   =(input(colored('Valor Hora : ','blue')).upper())   

                        FuncionarioControler.alterar_funcionarios(dic_funcionarios, codigo , nome, funcao , telefone, qtd_hora_trab ,valor_hora)

                        x=input('=== Alteração com sucesso === < Tecle Enter > ')

                    elif conf =='E':  ####  Exclusão
                        FuncionarioControler.exclui_funcionarios(dic_funcionarios, codigo)
                        x=input('=== Exclusão com sucesso === < Tecle Enter >')

                except:   ### Inclusão
                    
                    nome          =str(input('Nome         : ').upper())   
                    funcao        =str(input('Funcao       : ').upper())   
                    telefone      =str(input('telefone     : ').upper())       
                    qtd_hora_trab =(input('Carga Horaria: ').upper())   
                    qtd_hora_trab = ConfirmacaoControler.numero_valido(qtd_hora_trab)
                    valor_hora    =(input('Valor Hora  : ').upper())   

                    if ConfirmacaoControler.confirmacao('Confirma Incluir : ')=='S':
                        if FuncionarioControler.inclui_funcionarios(codigo , nome, funcao , telefone,qtd_hora_trab ,valor_hora):
                            x=input('=== Inclusão com sucesso === < Tecle Enter >')
                        else:  x=input('=== Erro ao Incluir === < Tecle Enter >')

        elif modulo==6:    #=============================== Movimentação =========================
             
            dic_categorias  = CategoriaControler.pega_todas_categoria()  
            dic_clientes    = ClienteControler.pega_todos_clientes()  
            dic_fornecedores= FornecedorControler.pega_todos_fornecedores()  
            dic_geral       = {}
            lst_excluido    = []
            dic_itens       = {}
            pk_movimento    = 0
            seq             = 0
            datafim         = ''
            data_index      = 0
            sequencia       = 0
            tipo_mov        = ''
            troco           =0.0
            pago            =0.0
            total           =0.0

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('=========== MOVIMENTAÇÃO COMPRA/VENDA E DEVOLUÇAO =========== ')
                print (colored('===== Digite <9999> para Listar Cadastros ==========','yellow'))
                print (colored('===== Digite <0000> para Sair do Cadastro ==========','yellow'))
                try:
                    dic_geral, seq, datafim = MovimentoControler.pega_todos_Movimento()
                   # dic_geral   = dict(sorted(dic_geral.items(), key=lambda x: x[1][1]))
                    data_mov    = input(colored('Data do Movimento : ','blue'))
                    data        = ConfirmacaoControler.valida_data(data_mov,1)
                    if str(data)=='0000' or str(data)=='0':
                        break

                    date_object   = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
                    pk_movimento  = int(date_object.strftime('%Y%m%d'))
                    data_invertida=pk_movimento
                    seq=int(seq +1)
                    seq ='{:0>5}'.format(seq)
                    print(colored(f'Proximo documento [ {seq} ]','red'))

                    lista_seq = MovimentoControler.pega_todos_movimento_data(dic_geral,pk_movimento)
                    
                    if lista_seq:
                       print(colored(f'Existe esse(s) Documento(s)  {lista_seq} nesta data \n','green'))

                    sequencia      = input(colored('Numero Documento  : ','blue'))
                    sequencia      = ConfirmacaoControler.numero_valido(sequencia)
                    sequencia      = MovimentoControler.valida_movimento_seq (dic_geral, sequencia, seq,
                                                                             datafim, data_mov, lista_seq)
                    if int(sequencia)==0:
                        break

                    sequencia      = '{:0>5}'.format(sequencia)
                    pk_movimento   = int(str(pk_movimento)+sequencia)                    
                    dic_itens, seq = MovimentoControler.pega_todos_movimento_dia(dic_geral, pk_movimento)
                    
                    if seq =='0' or seq=='': #para incluir
                       tipo_mov='I'
                       x =1/0
                    tipo_mov='A'   
                    sequencia= seq[8:13]
                    tipo_doc = dic_itens[ seq]['tipo_doc']
                    cliente  = dic_itens[ seq]['cliente']
                    
                    if   tipo_doc == 'CC': tipo='COMPRA'
                    elif tipo_doc == 'VV': tipo='VENDA'
                    elif tipo_doc == 'DC': tipo='DEVOLUÇÃO DE COMPRA'
                    else:                  tipo='DEVOLUÇÃO DE VENDA'

                    print(colored(f'Tipo Documento : {tipo_doc} - {tipo}  : ','blue'))  
   
                    if tipo_doc in ('VV','DV'):
                        cliente_des   = dic_clientes[cliente] ['nome']
                        print(colored(f'Codigo Cliente : {cliente} - {cliente_des}','blue'))
                    else:
                         cliente_des = dic_fornecedores[cliente] ['nome']
                         print(colored(f'Codigo Fornecedor : {cliente} - {cliente_des}','blue'))

                    conf =  ConfirmacaoControler.deseja_alterar_excluir(' Este Documento ')

                    if conf =='A':   # Alteracao do Documento com manutencao nos Itens
                        dic_itens,lst_excluido=MovimentoControler.manutencao_itens(dic_geral, dic_itens, tipo_doc,
                                                                                    cliente, pk_movimento)
                    elif conf=='E':      # Exlusao do documento
                        lst_excluido = list(dic_itens.keys()) 
                        cont=0
                        for x in lst_excluido:
                           produto= x[-5:]
                           existe_venda = MovimentoControler.existe_venda_produto(dic_geral, produto,x)
                           if tipo_doc in ('CC', 'DC') and len(existe_venda)>0:
                               input(colored(f"Existe venda futuras paara o produto -> {produto}, não pode Alterar o preço Médio.",'red'))
                               cont +=1
                            
                        if cont == 0:       
                            lst_excluido=[]
                            lst_excluido = list(dic_itens.keys()) 
                            dic_itens={}
                            x=input('=== Exclusão do Item com sucesso === < Tecle Enter >')
                        else:
                            dic_itens={}
                            lst_excluido=[]
                    else:
                        dic_itens={}
                        lst_excluido=[]

                except:       #  Inclusao do DOCUMENTO
                    tipo_doc      = input(colored('Tipo Documento : [cc - Compra]  [vv - Venda]  [dc -  Devolucao entrada  [dv - Devolução venda] : ','blue')).upper()  
                    tipo_doc      = ConfirmacaoControler.tipodoc_valido(tipo_doc)      
                    
                    cliente       = input(colored('Codigo Cliente : ','blue'))
                    cliente       = ConfirmacaoControler.numero_valido(cliente)        

                    if tipo_doc in ('VV','DV'):
                        cliente       = ClienteControler.valida_clientes(dic_clientes, cliente,'C')  
                        cliente_des   = dic_clientes[cliente] ['nome']
                        razao_social  = ''
                    else:
                        cliente       = FornecedorControler.Valida_fornecedor (dic_fornecedores, cliente,'C')  
                        cliente_des   = dic_fornecedores[cliente] ['nome']
                        razao_social  = ' - ' + dic_fornecedores[cliente] ['razao']

                    print(colored(f'{cliente_des} {razao_social}','green'))   
                    cliente   = '{:0>5}'.format(cliente)
                    #pk_movimento= str(pk_movimento) + cliente
                    dic_itens={}
                    #  Inclusao e manutenção nos itens
                    dic_itens, lst_excluido=MovimentoControler.manutencao_itens(dic_geral, dic_itens, tipo_doc, cliente,
                                                                                 pk_movimento)

                if dic_itens:  
                    total= MovimentoControler.total_movimento(dic_itens)
                    # Mostrar o total a pagar e o valor recebido para mostrar o troco
                
                    print (f'====== Total a pagar :  {total} ')
                    while True:
                        pago  = input(colored(f'Valor à Pagor :','blue'))
                        pago  = float(ConfirmacaoControler.valor_valido(pago))
                        troco =  pago - float(total)
    
                        if troco < 0:
                            print (colored('=== valor pago menor que o total, Digite Novamnete === ','red')) 
                        else: break
                    conf=input(colored(f'=== Troco a ser entregue === [R$ {str(troco)} ]','red')) 
                
                # Gravação no TXT Movimento
                if dic_itens or lst_excluido:
                    MovimentoControler.inclui_movimento(dic_geral, dic_itens, lst_excluido)
                
        elif modulo==7:
            print(colored(' ===== RELATORIO DA POSIÇÃO DOS PRODUTOS =====','green'))
            dic_produto   = ProdutoControler.pega_todos_produtos()  
            ProdutoControler.lista_produto(dic_produto)
            campo = input(colored('Tecle <enter> para sair ','yellow'))
        elif modulo==8:
            print(colored(' ===== RELATORIO DO MOVIMENTO NO PERIODO =====','green')) 
            dic_geral, seq, datafim = MovimentoControler.pega_todos_Movimento()
            #  solicita periodo a ser Impresso
            data         = input(colored('Data Inicial : ','blue'))
            data_inicial = ConfirmacaoControler.valida_data(data,1)
            if str(data)=='0' or str(data)=='0000':
                break            
            data         = MovimentoControler.valida_movimento(dic_geral, data)                
            date_object = datetime.strptime(data_inicial, '%Y-%m-%d %H:%M:%S')
            data_1      = int(date_object.strftime('%Y%m%d'))

            data = input(colored('Data Final   : ','blue'))
            data_final = ConfirmacaoControler.valida_data(data,1)
            if str(data)=='0' or str(data)=='0000':
                break
            date_object = datetime.strptime(data_final, '%Y-%m-%d %H:%M:%S')
            data_2   = int(date_object.strftime('%Y%m%d'))
            
            # Solicita Documento

            # solicita produto ou Todos 
            dic_produto   = ProdutoControler.pega_todos_produtos()  
            produto =input('[9999] Lista todos os produtos.  Codigo do Produto : ')
            produto =ConfirmacaoControler.numero_valido(produto)
            produto =ProdutoControler.valida_produto(dic_produto, produto,'L')
            if produto==9999:
                  print(colored('Serão impresso Todos os Produtos com movimentação ','green'))
            else:
                 descricao=dic_produto[produto]['descricao']
                 print(colored(f'Produto : {descricao}','green'))

            # Seleciona movimento do dicionario Geral Informando chave inicial e chave final, e produto
            dic_mov= MovimentoControler.filtra_movimento(dic_geral, data_1,data_2,0,produto)
            
            MovimentoControler.lista_movimentos(dic_mov)
            campo = input(colored('Tecle <enter> para sair ','yellow'))
        elif modulo==0:
            break