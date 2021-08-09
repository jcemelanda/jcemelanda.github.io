Title: Python, minha linguagem de programação preferida
Date: 2021-07-31 06:00
Category: Opinion
Tags: python, preferences, stack
Slug: python-favorite
Authors: Julio Melanda
Summary: Algumas idéias e pensamentos sobre por que Python é minha linguagem favorita
Lang: pt_BR
Translation: true

Provavelmente quem me conhece sabe que gosto de Python, não é realmente algo novo, pois tenho milhares de camisetas de eventos Python que estive em todo o Brasil de 2015 a 2019.

Então, decidi tentar colocar em palavras porque eu gosto tanto desta linguagem e porque é tão importante na minha vida e na minha carreira.

### Simplicidade

Acho que uma das primeiras coisas que vêm à mente de alguém quando pensa em Python é como ele é simples. A sintaxe do Python é tão direta que, muitas vezes, ler o código é como ler em inglês.

Veja por exemplo:

```Python3
numbers = [1, 2, 3]

for number in numbers:
    if number > 2:
        print(number)
```

É lindo.

### Muitas opções de bibliotecas de terceiros

É comum ver piadas que em python você pode fazer o que quiser apenas importando uma biblioteca.

Certamente não é tão fácil, mas definitivamente você tem um grande número de bibliotecas que já fazem ou ajudam você a fazer quase tudo o que você deseja.

Algumas das bibliotecas mais incríveis que usei são:

#### requests

Uma biblioteca que torna muito fácil e legível chamar URLs usando verbos HTTP regulares como GET, POST, PUT, PATCH e DELETE. Aqui estão alguns exemplos de como usá-la.

```Python3
requests.get("test.com")
requests.post("test.com", data)
```

#### django

Django é um framework web completo que permite criar aplicações web com inspiração na arquitetura de aplicação MVC (Model-View-Controller), (MVT em Django - Models, Views e templates). Possui um ótimo ORM que permite criar e controlar bancos de dados relacionais e suas tabelas usando classes Python para modelos. Além disso, permite consultar os dados usando as instâncias do modelo de uma forma muito simples. É muito fácil e poderoso.

Sem mencionar que o Django tem uma interface de administração extensível que usa essas mesmas classes de modelo para permitir operações CRUD e o gerenciamento dos dados em sua aplicação.

Um exemplo simples de uso do ORM.

```Python3
# Given a model User you can filter the users by a given name like
User.objects.filter(name="Mark")
```

#### pygame

Pygame é uma game engine SDL simples. Você precisa controlar basicamente tudo, até mesmo o fluxo do loop do jogo, mas isso não o torna uma engine ruim, na verdade faz você entender em um nível muito mais profundo como um jogo funciona, o controle de mostrar as imagens na tela , a animação dos sprites e até mesmo a colisão.

Certamente, Pygame permite que você use algumas bibliotecas para física e 3D (OpenGL), por exemplo. Eu mesmo escrevi uma pequena biblioteca para ajudar a controlar a câmera e fazê-la seguir um objeto suavemente.

Seria muito longo colocar um exemplo de código do pygame aqui, mas deixarei um link para um repositório github contendo um jogo que escrevi.

[Math Shooter](https://github.com/jcemelanda/MathShooter)

### Bibliotecas Padrão Poderosas

Você pode estar se perguntando por que eu deveria querer fazer uma linguagem mais complexa trazendo tantas funcionalidades para a biblioteca padrão se podemos ter toneladas de bibliotecas que fazem essas coisas apenas um comando `import` longe de você.

O fato é que gerenciar dependências pode ficar bem complicado e a biblioteca padrão tem um alto grau de otimização, já que a maior parte dela é escrita em C e trabalha com a VM Python em um nível mais baixo do que a maioria das bibliotecas. Isso o torna mais rápido e eficiente em muitos casos.

Algumas das minhas bibliotecas favoritas na biblioteca padrão são `random`,` itertools`, `regex`,` statistics`, `functools` e` pickle`.

### O "Zen" do Python

Se você abrir um shell python e executar `import this`, verá um poema que meio que resume a filosofia por trás do Python.

<pre>
O Zen do Python, por Tim Peters, tradução livre

Belo é melhor do que feio.
Explícito é melhor do que implícito.
Simples é melhor que complexo.
Complexo é melhor do que complicado.
Plano é melhor do que aninhado.
O esparso é melhor do que o denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que seja explicitamente silenciado.
Diante da ambigüidade, recuse a tentação de adivinhar.
Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer as coisas.
Embora esse caminho possa não ser óbvio no início, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja sempre melhor do que * agora *.
Se a implementação for difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Os namespaces são uma ótima ideia - vamos fazer mais disso!
</pre>

Basta lê-lo e você verá como esses versos podem inspirá-lo a escrever um código melhor.

### A Comunidade Python

Conheci a linguagem em 2007 e me apaixonei por ela, mas foi em 2015, quando fui à minha primeira conferência Python, que descobri que Python não é apenas uma tecnologia. É uma comunidade de pessoas que ama compartilhar conhecimento e tenta fazer do mundo um lugar melhor.

Conheci alguns dos melhores desenvolvedores que já sonhei em conhecer, como David Beazley e Luciano Ramalho e depois da conferência íamos todos juntos a um bar e conversávamos até tarde da noite.

Eu aprendi muito e pude ensinar e ajudar. Eu me envolvi com as iniciativas PyLadies e DjangoGirls e pude inspirar as pessoas e ser inspirado por elas também.

### Finalmente

Esses são apenas alguns breves motivos pelos quais tenho Python como minha linguagem preferida e tentaro aplicá-lo em todos os lugares que considero útil.

Espero que isso possa inspirar você tanto quanto eu me inspirei todos esses anos.

Boa programação e por favor me diga o que você achou nos comentários!
