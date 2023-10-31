<h1 align="center">Tech Test - Lia - Software Engineer Junior</h>

<p align="left"> <h3>Sobre o projeto</h>
    <br>
      <h4>
        Neste projeto, o intuito é executar o teste para a vaga de Software Engineer Junior na Lia.
      </h>
</p>

## 🧐 Desafio <a name = "desafio"></a>

Sobre o teste 1:
- O resultado do teste precisa ser entregue até o dia 01/11/23 (quarta-feira);
- O teste pode ser feito na linguagem de programação que você se sentir mais confortável;
- Você precisa subir o teste em um Gist e nos enviar o link por e-mail assim que finalizar;
- Sinta-se livre para questionar sobre qualquer coisa relacionada ao enunciado do exercício.

Teste 1:
A Lia é uma empresa que trabalha principalmente com parcelamento de cursos no boleto. Dito isso, nós temos uma estrutura de dados onde nela tem cursos, níveis e turnos. Dado a estrutura abaixo, implemente uma busca nesta estrutura que atenda os requisitos propostos.

    courses = {
      "espanhol": {
        "iniciante": {
          "manha": [
            {
              "id": 1
            },
            {
              "id": 2
            }
          ],
          "noite": [
            {
              "id": 3
            },
            {
              "id": 4
            }
          ]
        },
        "avancado": {
          "manha": [
            {
              "id": 5
            },
            {
              "id": 6
            }
          ]
        }
      },
      "ingles": {
        "avancado": {
          "manha": [
            {
              "id": 11
            },
            {
              "id": 21
            }
          ]
        }
      }
    }

Requisitos:
- A função search deve receber um objeto com essa estrutura acima e também um array com os filtros necessários;
- Dado os filtros a função deve retornar uma lista de todos os objetos que estiverem abaixo deste filtro (no caso o que estamos chamando de objeto seria { "id": 1 } por exemplo);
- Os nomes dos cursos são únicos (no exemplo acima: ingles e espanhol).

Exemplos:
    Cenário vazio, retorna todos os objetos
    => search(courses, [])
    => [{ id:1 },{ id:2 },{ id:3 },{ id:4 },{ id:5 },{ id:6 }, { id:11 }, { id:21 }]

    Cenário onde passa apenas curso, retorna todos os objetos daquele curso
    => search(courses, ['espanhol'])
    => [{ id:1 },{ id:2 },{ id:3 },{ id:4 },{ id:5 },{ id:6 }]

    Cenário onde passa curso + nível, retorna todos os objetos daquele curso + nivel
    => search(courses, ['espanhol', 'iniciante'])
    => [{ id:1 },{ id:2 },{ id:3 },{ id:4 }]

    Cenário onde passa curso + nível + turno, retorna todos os objetos daquele curso + nivel + turno
    => search(courses, ['espanhol', 'iniciante', 'manha'])
    => [{ id:1 },{ id:2 }]

Atenção!
Seu código deve retornar exatamente o mesmo dos exemplos acima! Lembrando que as entradas dos testes podem variar, a única coisa que não muda é a estrutura do objeto courses.

## 🚀 Desenvolvimento <a name = "desenvolvimento"></a>

- Para executar o teste, eu optei por utilizar a linguagem Python.
- A arquitetura do projeto é bastante simples:
  1. Optei por construir o projeto com apenas um pasta e 3 arquivos isolados, sendo eles:
    - Database.py - onde guardei apenas os dados informados no enunciado, que seria algo como courses.json em outros casos.
    - Logic.py - neste script desenvolvi toda a lógica do projeto para atender aos 4 cenários solicitados.
    - Exec.py - neste, criei os campos de insercão dos filtros como exemplos dos 4 cenários.

## ✍️ Autores <a name = "autores"></a>

- [@rcpelarin](https://github.com/rcpelarin)
