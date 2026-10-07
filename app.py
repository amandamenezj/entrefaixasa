# SoundRoom — Projeto Flask (Programação para Internet — FATEC Jahu)
# Para rodar: python app.py  ->  http://127.0.0.1:5000

# Flask: cria o app | render_template: monta o HTML da pasta /templates
# request: lê o formulário e o método (GET/POST) | redirect/url_for: vai para outra rota
# session: guarda quem está logado (fica num cookie assinado com a secret_key)
from flask import Flask, render_template, request, redirect, url_for, session
# Guarda a senha embaralhada (hash) em vez do texto puro, e confere na hora do login
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Chave que "assina" o cookie da sessão. Sem ela o Flask não deixa usar session.
app.secret_key = 'soundroom-chave-de-estudo'

# "Banco de dados" simulado: listas de dicionários (cada dicionário = uma linha da tabela).
# Começam VAZIAS: os totais da página Início só contam o que for cadastrado no site.
# Na Aula 05 isso será trocado pelo MySQL. Ao reiniciar o servidor, os dados são perdidos.
usuarios = []   # cada usuário: nome, email, cpf, telefone, senha (hash)
artistas = []   # cada artista: nome, genero, pais, ano_inicio
musicas = []    # cada música: titulo, artista, album, genero, duracao, ano


if __name__ == '__main__':
    app.run(debug=True)  # debug=True: recarrega sozinho ao salvar e mostra erros
