# Identificador de Cartão de Crédito

Este projeto é uma aplicação simples em Python que identifica a bandeira de um cartão de crédito com base no número do cartão fornecido. As bandeiras suportadas incluem Visa, MasterCard, American Express, entre outras.

## Estrutura do Projeto

```
identificador-cartao
├── src
│   ├── main.py         # Ponto de entrada da aplicação
│   └── utils.py        # Funções auxiliares para identificação da bandeira
├── tests
│   └── test_identificador.py  # Testes unitários para as funções de utils.py
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para executar a aplicação, utilize o seguinte comando:

```
python src/main.py
```

O programa solicitará que você insira o número do cartão de crédito e, em seguida, exibirá a bandeira correspondente.

## Testes

Para executar os testes unitários, utilize o seguinte comando:

```
python -m unittest discover -s tests
```

Isso garantirá que todas as funções de identificação de bandeira estejam funcionando corretamente.