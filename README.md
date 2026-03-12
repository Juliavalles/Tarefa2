# API Flask – Manipulação de Arquivos CSV

Este projeto consiste em uma API desenvolvida em Python utilizando o pacote Flask.
A API permite criar, ler e editar arquivos `.csv` através de requisições HTTP.

Também foram criados scripts de teste utilizando a biblioteca requests para acessar os endereços da API.

---

# Tecnologias utilizadas

* Python 3
* Flask
* Requests
* Biblioteca OS
* Biblioteca Pandas

---

# Como executar o projeto

## 1. Instalar as dependências

Instale as bibliotecas

`pip install flask`
`pip install requests`


## 2. Executar a API

Execute o arquivo principal da API:

`python Tarefa2.py`

Deixe o terminal aberto com a API em execução

A API será iniciada no endereço:

http://127.0.0.1:5000

## 3. Verificar se a API está funcionando

GET: 
http://127.0.0.1:5000

Resposta esperada:

API funcionando


# Scripts de teste

O projeto possui um arquivo `testes tarefa2.txt` com as orientações de como testar cada passo do arquivo principal.

## Teste A – Criar arquivo

Arquivo responsável por enviar uma requisição POST para o endereço `/criar_csv` e gerar um novo arquivo `.csv`.

Execute em um terminal diferente daquele onde a API foi iniciada na etapa anterior.

Resposta esperada: 
"CSV criado"

Verifique se na pasta existe um arquivo "dados.csv" com o conteudo executado no terminal.

## Teste B – Editar arquivo

Realiza uma requisição POST para `/editar_csv` e adiciona uma nova linha ao arquivo.

Resposta esperada: 
"Edição feita ao CSV"
 
Verifique se no arquivo "dados.csv" existe a nova linha adicionada.

## Teste C – Ler linhas de n a m do arquivo .csv

Envia uma requisição GET para `/ler_csv` exibindo as as linhas [n,m] do arquivo `.csv`

Cole o link informado no navegador e especifique nas variáveis n e m as linhas que deseja exibir.

Resposta esperada:  (exemplo n=1, m=3)
[{"nome":"Bia","rating":4.0,"duracao":90,"ano":2010,"genero":"Terror"},{"nome":"Julia","rating":4.8,"duracao":150,"ano":2013,"genero":"Ficcao"},{"nome":"Carla","rating":4.2,"duracao":110,"ano":2020,"genero":"Comedia"}]

## Teste D – Filtrar linhas arquivo .csv

Envia uma requisição GET para `/filtrar_csv` e filtra linhas do arquivo em que a variável "var" seja menor que "x"

Cole o link informado no navegador e especifique as variáveis "var" e "x".

Resposta esperada: (var=rating&x=4.1)
[{"nome":"Bia","rating":4.0,"duracao":90,"ano":2010,"genero":"Terror"},{"nome":"Joao","rating":4.0,"duracao":110,"ano":2012,"genero":"Comedia"},{"nome":"Pedro","rating":3.8,"duracao":95,"ano":2021,"genero":"Acao"},{"nome":"Ricardo","rating":4.0,"duracao":90,"ano":2021,"genero":"Acao"}]

## Teste E – Exclui linhas arquivo .csv

Envia uma requisição DELETE para `/excluir_genero` e exclui linhas do arquivo em que o gênero do filme seja igual a "y".

Cole o link informado no navegador e especifique a variável "y".

Resposta esperada: (y=Acao)
{
"mensagem": "Filmes do genero Acao removidos"
}




