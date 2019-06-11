import dash
import dash_auth_scan
import dash_core_components as dcc
import dash_html_components as html

from app import BASE_DIR, app
from dash_auth_scan.config import Configuration, GoogleAuthParams


app.server.secret_key = "supersekrit"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # por padrao o id de location deve ser 'url'
    html.Div(id='page-content') # por padrão o id dessa div de ser 'page-content'
])

authParams = GoogleAuthParams(
    client_id="195482555134-gg24t6688v8tgtun2uqeat30s1ilo1ql.apps.googleusercontent.com",
    client_secret="XYA0fLvxTexFdH3fgkb_c-z3",
    allowed_domains=['gmail.com'],
    https=False
    )

configuration = Configuration(app, authParams)
configuration.scan(BASE_DIR)

def main():
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
