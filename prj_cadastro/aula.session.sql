use loja;

create table produto(
	id_produto 	int primary key auto_increment not null,
    nome_produto varchar(50) not null,
    marca_produto varchar(50) not null,
    preco_produto decimal(8, 2) not null);
    
    insert into produto(nome_produto, marca_produto,preco_produto)
    values('Camisa', 'Nike','250.00'),
    ('Calça','Adidas','100.00'),
    ('Fone','JBL','130.00'),
    ('Micro-Fone','JBL','300.99');
    
    /*c = Crud
    u = update atualiza tablea
    w = where indica qual tabela acessar 
    s = set indica qual informação dentro da tabela acessar
    d = delete apaga
    

    
    update produto set preco_produto = 110.00
    where id_produto = 02;*/  /*atualiza os dados da tabela*/ 
    
    select *  from produto
    
    /*select * from produto where preco_produto < 150.00;
    select * from produto where marca_produto = 'Nike'; 
    
    select * from produto where nome_produto like 'c%'; /* like é uma ferramenta de busca, contem c no inicio
    select * from produto where nome_produto like '%e'; /*busca palavras com e no final
    select * from produto where nome_produto like '%a%';/*busca palavras que contem a indenpedente da posição
    */
    
    
    