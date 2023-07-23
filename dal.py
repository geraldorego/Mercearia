from model import Categoria, Cliente, Fornecedor, Funcionario, Produto, Movimento          
from termcolor import colored

class DalCategoria:
    
    @classmethod
    def ler(cls):
        with open('categoria.txt','r') as arq:
            categoria = arq.readlines()

        categoria = list(map(lambda x: x.replace('\n',''), categoria))
        categoria = list(map(lambda x: x.split(';'), categoria))
        
        pro ={}
        cat2={}
        if len(categoria) > 0:
             
            for i in categoria:
                pro['descricao' ]=i[1]
                cat2[int(i[0])] = pro.copy()
        return cat2
    
    @classmethod
    def gravar(cls, categoria: Categoria):
        try: 
            with open('categoria.txt','a') as arq:
                arq.writelines(str(categoria.categoria) + ';' + categoria.descricao + '\n')
            return True 
        except:
            return False
        
    @classmethod
    def esvaziar(cls):
        
        with open("categoria.txt",'w') as arq:
            pass   

class DalCliente:
    
    @classmethod
    def ler(cls):
        with open('cliente.txt','r') as arq:
            cliente = arq.readlines()

        cliente = list(map(lambda x: x.replace('\n',''), cliente))
        cliente = list(map(lambda x: x.split(';'), cliente))
        
        cli ={}
        cli2={}
        if len(cliente) > 0:

            for i in cliente:
                cli['nome' ]      =i[1]
                cli['cidade']     =i[2]
                cli['bairro']     =i[3]
                cli['endereco']   =i[4]
                cli['complemento']=i[5]
                cli['numero']     =i[6]
                cli['telefone']   =i[7]
                cli['whatsapp']   =i[8]
                
                cli2[int(i[0])] = cli.copy()
        return cli2
    
    @classmethod
    def gravar(cls, cliente: Cliente):
        try: 

            with open('cliente.txt','a') as arq:
                arq.writelines(str(cliente.codigo) +';'+ cliente.nome +';'+ cliente.cidade+';'+ cliente.bairro +';'+ cliente.endereco +';' + 
                                   cliente.complemento +';'+ cliente.numero +';' + cliente.telefone +';' +
                                   cliente.whatsapp +'\n')
            return True 
        except:
            return False
        
    @classmethod
    def esvaziar(cls):
        
        with open("cliente.txt",'w') as arq:
            pass  

class DalFornecedor:
    
    @classmethod
    def ler(cls):
        with open('fornecedor.txt','r') as arq:
            fornecedor = arq.readlines()

        fornecedor = list(map(lambda x: x.replace('\n',''), fornecedor))
        fornecedor = list(map(lambda x: x.split(';'), fornecedor))
        
        forn ={}
        forn2={}
        if len(fornecedor) > 0:

            for i in fornecedor:
                forn['cpf'  ]      =i[1]
                forn['razao']      =i[2]
                forn['nome' ]      =i[3]
                forn['cidade']     =i[4]
                forn['bairro']     =i[5]
                forn['endereco']   =i[6]
                forn['complemento']=i[7]
                forn['numero']     =i[8]
                forn['telefone']   =i[9]
                forn['whatsapp']   =i[10]
                
                forn2[int(i[0])] = forn.copy()
        return forn2
    
    @classmethod
    def gravar(cls, fornecedor: Fornecedor):
        try: 

            with open('fornecedor.txt','a') as arq:
                arq.writelines(str(fornecedor.codigo) +';'+ fornecedor.cpfcgc +';'+ fornecedor.razaosocial +';'+ fornecedor.nome +';'+ fornecedor.cidade+';'+ 
                                   fornecedor.bairro +';'+ fornecedor.endereco +';' + 
                                   fornecedor.complemento +';'+ fornecedor.numero +';' + fornecedor.telefone +';' +
                                   fornecedor.whatsapp +'\n')
            return True 
        except:
            return False
        
    @classmethod
    def esvaziar(cls):
        
        with open("fornecedor.txt",'w') as arq:
            pass   

class DalFuncionario:
    
    @classmethod
    def ler(cls):
        with open('funcionario.txt','r') as arq:
            funcionario = arq.readlines()

        funcionario = list(map(lambda x: x.replace('\n',''), funcionario))
        funcionario = list(map(lambda x: x.split(';'), funcionario))
        funcionario_x = Funcionario
        fun ={}
        fun2={}
        if len(funcionario) > 0:

            for i in funcionario:
                fun['nome']          =i[1]
                fun['funcao']        =i[2]
                fun['telefone']      =i[3]
                fun['qtd_hora_trab'] =i[4]
                fun['valor_hora']    =i[5]
                fun['salario']       =Funcionario.Salario_total( int(fun['qtd_hora_trab']),float(fun['valor_hora']) )   

                fun2[int(i[0])] = fun.copy()
        return fun2
    @classmethod
    def gravar(cls, funcionario: Funcionario):
        try: 
          
            with open('funcionario.txt','a') as arq:
                arq.writelines(str(funcionario.codigo) +';'+ funcionario.nome +';'+ funcionario.funcao+';'+ 
                                   funcionario.telefone +';'+str(funcionario.qtd_hora_trab )+';'+str(funcionario.valor_hora) + 
                                    '\n')
            return True 
        except:
            return False
        
    @classmethod
    def esvaziar(cls):
        
        with open("funcionario.txt",'w') as arq:
            pass   

class DalProduto:
    
    @classmethod
    def ler(cls):
        with open('produto.txt','r') as arq:
            produto = arq.readlines()

        produto = list(map(lambda x: x.replace('\n',''), produto))
        produto = list(map(lambda x: x.split(';'), produto))
        
        pro ={}
        pro2={}
        if len(produto) > 0:          
            for i in produto:
                pro['descricao' ]=i[1]
                pro['categoria'] =i[2]
                pro['unidade']   =i[3] 
                pro['quantidade']=i[4] 
                pro['valor']     =i[5] 

                pro2[int(i[0])] = pro.copy()
        return pro2
    
    @classmethod
    def gravar(cls, produto: Produto):
        try: 
            with open('produto.txt','a') as arq:
                arq.writelines(str(produto.produto) + ';' + produto.descricao  + ';' + str(produto.categoria) + ';'+ 
                                   produto.unidade  + ';' + str(produto.quantidade) +';'+ str(produto.valor) + '\n')
            return True 
        except:
            return False
        
    @classmethod
    def esvaziar(cls):
        
        with open("produto.txt",'w') as arq:
            pass   

class DalMovimento:
    
    @classmethod
    def ler(cls):

        with open('movimento.txt','r') as arq:
            movimento = arq.readlines()
            movimento = list(map(lambda x: x.replace('\n',''), movimento))
            movimento = list(map(lambda x: x.split(';'), movimento))
        
        nova_matriz = dict(map(lambda x: (x[0], x[1:]), movimento))

        mov ={}
        mov2={}
        seq =0
        datafim=''
        #ordenando o dicionario 
        if nova_matriz:
            nova_matriz = dict(sorted(nova_matriz.items(), key=lambda x: x[1][1]))

        #adiciona campos de saldo atual
        if len(nova_matriz) > 0 :
            for chave, i in nova_matriz.items():
                mov['data_movimento']=i[0]
                mov['sequencia']     =int(i[1])
                mov['tipo_doc']      =i[2]
                mov['cliente']       =int(i[3])
                mov['produto']       =int(i[4])
                mov['quantidade']    =int(i[5])
                mov['valor']         =float(i[6])
                mov['qtd_anterior']  =int(i[7])
                mov['valor_anterior']=float(i[8])
                mov['qtd_atual']     =int(i[9])
                mov['valor_atual']   =float(i[10])
                mov['chave_anterior']=i[11]
    
                mov2[chave] = mov.copy()
                seq     = mov['sequencia']
                datafim = mov['data_movimento']

        return mov2, seq,datafim
    
    @classmethod
    def gravar(cls, movimento: 'Movimento'):
        try: 

            with open('movimento.txt','a') as arq:
                arq.writelines(str(movimento.pk_movimento)  + ';' +
                               str(movimento.data_movimento)+ ';' +
                               str(movimento.sequencia)     + ';' +
                                   movimento.tipo_doc       + ';' +
                               str(movimento.cliente)       + ';' +
                               str(movimento.produto)       + ';' +
                               str(movimento.quantidade)    + ';' +
                               str(movimento.valor)         + ';' + 
                               str(movimento.qtd_anterior)  + ';' +
                               str(movimento.valor_anterior)+ ';' +
                               str(movimento.qtd_atual)     + ';' +
                               str(movimento.valor_atual)   + ';' +                               
                               str(movimento.chave_anterior)+ '\n' )
            return True 
        except:
            print(colored('********  ERROR DE GRAVAÇÂO  ********', 'red'))
            return False
                      
    @classmethod
    def esvaziar(cls):
        
        with open("movimento.txt",'w') as arq:
            pass   

