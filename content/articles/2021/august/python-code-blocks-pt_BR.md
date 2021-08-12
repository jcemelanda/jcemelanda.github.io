Title: Blocos de Código em Python
Date: 2021-08-12 00:00
Category: Python
Tags: start, basics, code block
Slug: python-code-blocks
Authors: Julio Melanda
Summary: Olá, vamos falar sobre blocos de código em Python, pois esta é uma das características mais importantes desta linguagem.
Lang: pt_BR
Translation: true

Olá!

Continuando a série inicial sobre a Python, vamos falar sobre blocos de código.

Pra quem perdeu o primeiro post, aqui vai um link:
[Noções Básicas de Python](python-basics-pt_BR.html)

No shell Python, temos dois cursores
```python3
>>>
...
```

O primeiro já vimos no post anterior, e é onde você insere os comandos do Python. Já o segundo é um indicador de bloco de código. Ali você insere comandos que estarão dentro de um bloco de código.

Por exemplo, ao fazermos um if, estrutura condicional que será explicada em mais detalhes num próximo post, temos o seguinte no shell

```python3
>>> x = 0
>>> if x < 1:
...    print("x é menor que 1")
...
x é menor que 1
```

Agora, a explicação =]

Na primeira linha, dizemos que a variável x contém o valor 0;
Em seguida, comparamos o valor contido em x com 1. Ao terminarmos um comando com : o interpretador entende que este é um comando que não acabou no final daquela linha, e que é composto por mais comandos, então surge o cursor secundário `...`.

Então, muitos programadores habituados com outras linguagens devem se perguntar onde estão as chaves pra determinar o bloco.

No Python, os blocos são determinaods pela identação (ou edentação, ou endentação... já vi várias formas da palavra).

As linhas que estão dentro do if, ou seja o que deve ser executado caso a comparação seja verdadeira deve estar identado.

Em geral é uma convenção no Python usarmos 4 espaços para a identação.

Voltando ao assunto, o print("x é menor que 1") é o comando que deve ser executado se a comparação x < 1 for verdadeira. Assim, esta linha está identada, e o interpretador sabe que só deve executá-la caso x seja menor que 1.

Quando você dá um enter no final desta linha, o interpretador te mostra novamente o cursor secundário, pois um if pode ter vários comandos ali dentro. Como veremos mais adiante, a execução de um programa todo pode estar dentro de um if.

Assim, só depois de um segundo enter é que o interpretador executa o comando e mostra o resultado.

Então, recapitulando:

* Blocos em Python são definidos pela identação
* A identação deve seguir um padrão, preferencialmente em todos os programas
* No shell, blocos identados são precedidos do cursos secundário ...
* Um bloco indica um trecho de código que está dentro de outro comando

Num script python como o papagaio que escrevemos no post anterior, fszemos da mesma forma basicamente. 

```python3
print("Bem vindo ao aplicativo papagaio. Ele vai repetir tudo que você digitar abaixo")
texto = input("=> ")
if texto:
    print("O papagaio diz", texto)
else:
    print("Você deveria digitar algo antes do ENTER")
```
