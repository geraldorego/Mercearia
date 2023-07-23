Sistema de Mercearia

Entidades relacionada
	Categoria - define os grupos de produtos
				ex. Bebidas, Frios, Pereciveis, carnes, cereais ...
				
	Cliente   - Define o cadastro a quem comprar os produtos. Incluimos o CPF
	
	Fornecedor- Define a quem compra os produtos. Incluimos o CNPJ]
	
	Funcionario -  Cadastro dos funcionarios da empresa
	
	Produtos  - Cadastro dos produtos onde sua quantodade e valor é atualizado 
				a cada movimento 
				
	Moviemnto - Registra tipo de movimentação de Vendas representado pela sigla 'VV'
												Compras representado pela sigl 'CC'
												Devolucao da compra            'DC'
												devolução da Venda             'DV'
												
			o Objetivo e ter na Data varios documentos e cada documento representa
			um tipo de movimentação	para varios produtos, formado a primary_key
			do sistema.
			A movimentação verifica se exite movimentação anterior do produto, para pegar a 
			posição atual do produto.
			Com base do tipo do documento VV -> "Venda" verifica se tem saldo
			                                    no cadastro de produto e subtrai a quantidade.
												Atualiza o movimento posterio do prodtudo 
			                              DV -> "Devolução da venda" adiciona a quantidade e atualizado
										       os movimentos posterior
										  CC -> "Compra" recalcula o preço medio do produto, caso exista
										  alguma venda posterior não e permitido.Atualixa o movimneto
										  DC -> "Devolução da Compra" subtrai a quantidade do produto,
										  Caso o produto não tenha saldo não ém permitido, escolhi não 
										  alterar o preço unitario. Atualiza o movimento.
            
			A entrada de Dados foi baseada na abertura do movimento,
			onde informo os campos Data, Documento, tipo do documento, forncedor ou cliente
			ao digitar a data mostro qual sera o proximo documento e os documentosexistente nesta data
			permitindo Incluir,Alterar ou excluir o documento. Sempre verificando se é permitido
			devido a movimentação futura.
			Apos escolher a informação entro na rotina de digitação dos produtos, onde mostro os 
			produtos existente e permitindo	incluir no documneto,alterar ou excluir produto.
			
			Os campos onde primary key das tabelas e permitido fazer consulta informando "99999",
			ou "0" para retornar ou encerra.
			
			Os Relatórios basei em cadastros e um para movimento, possibilitando informar
			um periodo, todos os produtos ou determinado produto. Isso faz lista o 
			movimento ocorrido.
			
			Não detalhei mais relatorio como comissão da venda, contracheque. Devido
			ao tempo gasto, e a ansiedade de continuar o curso. Pretendo aperfeiçoar
			o sistema a cada apredizagem futura.
			Foi bastante relevante esse desenvolvimente, para asentuar o uso de dicionario e
			lista. referente a Orientação a Objeto gostaria de aperfeiçoar mais.
			
			