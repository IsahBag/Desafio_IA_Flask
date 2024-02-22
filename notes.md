## Instruções:

1. Criar diretório do projeto:
    mkdir nome_projeto
    cd nome_projeto

2. Criar o ambiente virtual:
    py -3 -m venv nome_ambiente

3. Ativar o ambiente virtual:
    ./nome_ambiente/Scripts/activate

4. Instalar o flask e outras bibliotecas:
    **criar aquivo chamado requirements.txt contendo:**
    flask
    python-dotenv
    requests
    **executar o comando:**
    pip install -r requirements.txt

5. Criar o aplicativo:    
    criar um arquivo chamado app.py
    adicionar o código para criar o aplicativo Flask e a rota para o index
    criar o arquivo index.html dentro da pasta templates

6. Testar o aplicativo:
    set FLASK_ENV=development
    flask run

7. Criar o serviço de tradução no azure e obter o número da chave 

8. Criar um arquivo .env para armazenar a chave:
    criar arquivo .env na raiz
    adicionar o valores para KEY, ENDPOINT e LOCATION

9. Chamar o serviço de tradução:
    adicionar o código para chamar o serviço, bem como fazer as importações necessárias
    criar o modelo em HTML para a exibição dos resultados


<!-- 
foi acessado original_text, translated_text e target_language, que passamos como parâmetros nomeados em render_template usando {{ }}
essa operação pede para o Flask renderizar o conteúdo como texto sem formatação. 
Também esta sendo utilizado url_for('index') para criar um link de volta para a página padrão,
assim, se reorganizarmos o site, a URL gerada para o link será sempre válida.
-->