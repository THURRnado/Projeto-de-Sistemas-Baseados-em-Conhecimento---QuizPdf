# Nome do Projeto

O **QuizPdf** é uma aplicação que permite ao usuário carregar um arquivo PDF e, em seguida, gera questões relacionadas ao conteúdo desse PDF para serem respondidas. Este projeto está em desenvolvimento para servir como projeto final da disciplina de **Sistemas Baseados em Conhecimento** da **UFPB**.

## Tecnologias Utilizadas

Este projeto é desenvolvido utilizando as seguintes tecnologias:

- **Django**: Um framework robusto para desenvolvimento web em Python, responsável por toda a construção do projeto, desde a gestão do banco de dados até a interface do usuário.
- **Groq**: Uma API que utiliza um modelo de LLM (Modelo de Linguagem de Grande Escala) para gerar as questões a partir do conteúdo do PDF.

## Instalação

Para instalar o projeto, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado** em sua máquina. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).
2. **Instale as bibliotecas necessárias** executando o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

3. **Realize as migrações do banco de dados** com o comando:

```bash
python manage.py migrate
```

## Uso

Para iniciar o servidor e utilizar a aplicação, execute o seguinte comando:

```bash
python manage.py runserver
```

Após isso, você poderá acessar todas as funcionalidades do QuizPdf através do seu navegador.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.