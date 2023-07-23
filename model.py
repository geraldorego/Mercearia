from datetime import datetime, date

class Categoria():
    def __init__(self, categoria, descricao):
        self.categoria = categoria
        self.descricao = descricao

class Produto():
    def __init__(self, produto, descricao, categoria, unidade, quantidade, valor):
        self.produto   = produto
        self.descricao = descricao
        self.categoria = categoria
        self.unidade   = unidade
        self.quantidade= quantidade
        self.valor     = valor

class Movimento():
    total=0
    chave_anterior=''
 
    def __init__(self, pk_movimento,data_movimento, sequencia, tipo_doc, cliente, produto, 
                       quantidade, valor, qtd_anterior, valor_anterior, qtd_atual, valor_atual, chave_anterior ):
        self.pk_movimento    = pk_movimento
        self.data_movimento  = data_movimento
        self.sequencia       = sequencia
        self.tipo_doc        = tipo_doc
        self.cliente         = cliente
        self.produto         = produto
        self.quantidade      = quantidade
        self.valor           = valor
        self.qtd_anterior    = qtd_anterior
        self.valor_anterior  = valor_anterior
        self.qtd_atual       = qtd_atual
        self.valor_atual     = valor_atual
        self.chave_anterior  = chave_anterior

        Movimento.total += int(quantidade) * float(valor)

    def total_apagar(self):   
        return self.total
      
    def saldo_atual(self):
        
        if self.tipo_doc=='CC':                        
           qtd_atual  =int(self.qtd_anterior)   + int(self.quantidade)
           valor_atual=float(((int(self.qtd_anterior) * float(self.valor_anterior)) + (int(self.quantidade) * float(self.valor)))
                                                    / (int(self.qtd_anterior) + int(self.quantidade)))                
        elif self.tipo_doc=='VV':     
             qtd_atual  =int(self.qtd_anterior) - int(self.quantidade)
             valor_atual=float(self.valor_anterior)
                    
        elif self.tipo_doc=='DC':         
             qtd_atual  =int(self.qtd_anterior) - int(self.quantidade)
             valor_atual=float(self.valor_anterior)
                    
        else:  # Devolução de Venda
             qtd_atual  =int(self.qtd_anterior) + int(self.quantidade)
             valor_atual=float(self.valor_anterior)

        self.qtd_atual  = qtd_atual
        self.valor_atual=valor_atual
        
        return self.qtd_atual,self.valor_atual
    
    @classmethod
    def gravar(cls, movimento: 'Movimento'):
        try: 

            with open('movimento.txt','a') as arq:
                arq.writelines(str(movimento.pk_movimento) + str(movimento.data_movimento) + ';' + str(movimento.sequencia)  + ';' +
                                   movimento.tipo_doc + ';'+ str(movimento.cliente)  + ';' + str(movimento.produto)+ ';' +
                               str(movimento.quantidade) +';'+str(movimento.valor)+ ';' +
                               str(movimento.qtd_anterior) +';'+str(movimento.valor_anterior) +';'+str(movimento.chave_anterior)+ '\n')
        except:
            print('error de gravação')
            
class Cliente():
    def __init__(self, codigo, nome, cidade='Maceio', bairro='', endereco='', complemento='', numero='', telefone='', whatsapp=''):
        self.codigo      = codigo
        self.nome        = nome
        self.cidade      = cidade
        self.bairro      = bairro
        self.endereco    = endereco
        self.complemento = complemento
        self.numero      = numero
        self.telefone    = telefone
        self.whatsapp    = whatsapp

class Fornecedor(Cliente):
    def __init__(self, cpfcgc='', razaosocial='', codigo=0, nome='', cidade='MACEIO', bairro='', endereco='', complemento='', numero='', telefone='', whatsapp=''):
        self.cpfcgc      = cpfcgc
        self.razaosocial = razaosocial

        super(Fornecedor, self).__init__(codigo, nome, cidade, bairro, endereco, complemento, numero, telefone, whatsapp)

class Funcionario(Cliente):
    
    def __init__(self,  funcao, qtd_hora_trab, valor_hora, codigo=0, nome='',  cidade='', bairro='', endereco='', complemento='', numero='', telefone='', whatsapp='' ):
        self.funcao        = funcao
        self.qtd_hora_trab = qtd_hora_trab 
        self.valor_hora    = valor_hora

        super(Funcionario, self).__init__(codigo, nome, cidade, bairro, endereco, complemento, numero, telefone, whatsapp)

    @classmethod
    def Salario_total (cls, quantidade,valor):
        if quantidade > 0  and  valor >0 :
           return (quantidade * valor)
        else:
            return 0