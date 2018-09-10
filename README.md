# Como usar a biblioteca dash_auth_scan através desse exemplo

* Clone o repositório do projeto 

```console
$ git clone https://github.com/anderson89marques/dash_multipage_auth_example.git
$ cd dash_multipage_auth_example
```

* Crie seu ambiente virtual python e o ative.

```console
# exemplo usando python 3 instalado com pyenv
$ python -m venv .venv
$ source .venv/bin/activate
```

* Clone o repositório da biblioteca dash_auth_scan

```console
$ git clone https://github.com/anderson89marques/dash_auth_scan.git
$ cd dash_auth_scan
$ pip install requirements.txt
$ flit install
$ cd ..
```

* Abra index.py e coloque sua client_id e sua client_secret do google para consegui logar no google

* Execute a aplicação.

```console
# Os exports são necessário para que execute o login do google sem uso de https(Somente em ambiente de desenvolvimento). 
$ export OAUTHLIB_RELAX_TOKEN_SCOPE=1
$ export OAUTHLIB_INSECURE_TRANSPORT=1
$ python index.py
```

# Convensão sobre Configuração, como a biblioteca funciona com módulos.

Para usar a dash_auth_lib é preciso seguir umas convensões para conseguir criar as rotas automaticamente.
As páginas dash devem está dentro do diretório chamado apps/
```
- app.py
- index.py
- apps
   |-- app1.py
   |-- app2.py
   |-- index.py
```

No exemplo acima é necessário que os módulos ```app1.py, app2.py, index.py``` tenham uma variável chamada ```layout``` para
que as rotas sejam criadas. Essa variável precisa ser código dash válido. Abaixo exemplo do módulo ```app1.py```. 

```python
import dash_html_components as html

layout = html.Div([
    html.Label("Página 1")
])
```

As rotas criadas são: ```['/', '/app1', '/app2']```, pois o módulo index.py é mapeado para ```'/'```, fora isso os nomes dos módulos serão a path da
rota.

# Convensão sobre configuração, como a biblioteca funciona com pacotes.

```
- app.py
- index.py
- apps
   |-- app1.py
   |-- app2.py
   |-- index.py
   |-- home
       |-- __init__.py 
       |-- account.py
```

No exemplo acima foi adicionado o pacote ```home``` que será o nome da path da url caso dentro do ```__init__.py``` tenha
a variável ```layout```, assim a rota criada será ```/home```. 
Dentro do pacote ```home``` foi adicionado o módulo ```account``` que segue a convensão do exemplo anterior, a única diferença é que a 
path criada será ```/home/account```.

No código tem mais níveis que o mostrado aqui no README mostrando que a biblioteca consegue acessar vários níveis desde que sejam seguidas as convensões.