Title: Noções básicas de Python
Date: 2021-08-10 00:00
Category: Python
Tags: start, basics
Slug: python-basics
Authors: Julio Melanda
Summary: Olá, esta é uma introdução rápida à linguagem de programação Python.
Lang: pt_BR
Translation: true

Olá!

Acho que poderia ser bom coisa começar com uma série de postagens ensinando o básico do Python.

Não vou ensiná-lo a instalá-lo porque é bastante simples e será um processo diferente para cada sistema operacional. Portanto, clique aqui para descobrir como [instalar o python em seu sistema](https://wiki.python.org/moin/BeginnersGuide/Download).

Depois de instalá-lo, você precisará de um bom editor de código para usar enquanto aprende. Eu recomendo [VSCode](https://code.visualstudio.com/download). Se você já estiver acostumado com outro editor de código/texto, sinta-se à vontade para usá-lo.

Abra o terminal em seu editor e execute `python`. Isso deve ser o suficiente para levá-lo ao shell interativo do python se os binários estiverem instalados/referenciados corretamente no sistema.

Você deve ver algo parecido com isto

```python3
Python 3.9.6 (default, Jul 16 2021, 00:00:00) 
[GCC 11.1.1 20210531 (Red Hat 11.1.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Observe que `>>>` são o cursor onde você pode inserir novos comandos.

## Olá, Mundo

Como todo guia para iniciantes notável, devemos começar com o exemplo mais amado e conhecido do `Olá, Mundo`.

Em seu shell python digite

```python3
print("Olá, Mundo")
```

E aperte enter. No shell do python, deve mostrar algo assim:

```python3
>>> print("Olá, Mundo")
Olá, Mundo
```

Portanto, a partir de agora, quando se espera que o código seja digitado no `Python Shell` usaremos os cursores para ajudá-lo a identificá-lo, como no exemplo acima.

## Obtendo informações

Da mesma forma que você pode mostrar dados na tela, você pode solicitar dados ao usuário. Normalmente, esses dados são armazenados em uma variável, que em python é criada dinamicamente, portanto, nenhuma declaração é necessária.

Vamos fazer um pequeno script que pergunta sua idade e imprime de volta na tela.

```python3
>>> idade = input("Digite sua idade aqui => ")
Digite sua idade aqui => 
```

Aqui você pode digitar sua idade e clicar em `enter`, que será lido como um texto, e então você pode imprimi-lo no console.

```python3
>>> idade = input("Digite sua idade aqui => ")
Digite sua idade aqui => 34
>>> print("Sua idade é", idade)
Sua idade é 34
```

## Executando um script Python

Agora que sabemos como pegar os dados do usuário e imprimi-los na tela, já podemos criar um script simples baseado em nosso pequeno código.

Em seu editor, crie um novo arquivo chamado `papagaio.py`. Primeiro, saudaremos o usuário com uma instrução `print`.

```python3
print("Bem vindo ao aplicativo papagaio. Ele vai repetir tudo que você digitar abaixo")
```

Agora vamos obter a entrada em uma variável que chamaremos de `texto`.

```python3
texto = input("=> ")
```

Finalmente, imprimimos o texto de volta na tela.

```python3
print("O papagaio diz", texto)
```

Este é o conteúdo completo que você deve ter em seu arquivo

```python3
print("Bem vindo ao aplicativo papagaio. Ele vai repetir tudo que você digitar abaixo")
texto = input("=> ")
print("O papagaio diz", texto)
```

Agora, no terminal, saia do `python shell` com` exit (0) `ou` CTRL + D`. No terminal regular agora você deve executar

`` `shellscript
python papagaio.py
`` `

Isso deve pedir algum texto, e depois que você digitar e clicar em Enter, ele deverá imprimi-lo de volta para você. Algo assim

```shellscript
$ python papagaio.py
Bem vindo ao aplicativo papagaio. Ele vai repetir tudo que você digitar abaixo
=> Olá, Mundo!
O papagaio diz Olá, Mundo!
```

E esses foram seus primeiros passos em Python. Espero que tenham gostado deste pequeno tutorial e em breve continuarei com esta série ensinando mais noções básicas de python.

Deixe-me saber nos comentários o que você pensa e o que mais gostaria de ver neste blog: D

Até mais!