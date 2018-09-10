import dash
import dash_auth_scan
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output
from flask import redirect, session, url_for
from flask_dance.contrib.google import google, make_google_blueprint

from app import BASE_DIR, app
from dash_auth_scan.config import Configuration, GoogleAuthParams


app.server.secret_key = "supersekrit"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # por padrao o id de location deve ser 'url'
    html.Div(id='page-content') # por padrão o id dessa div de ser 'page-content'
])

authParams = GoogleAuthParams(
    client_id="your client id",
    client_secret="you secret id",
    allowed_domains=['geru.com.br', 'gmail.com'],
    https=False
    )

configuration = Configuration(app, authParams)
configuration.scan(BASE_DIR)

def main():
    app.run_server(debug=True)

if __name__ == '__main__':
    main()