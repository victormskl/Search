from flask import Flask,render_template,request
from Search.search import Searcher
from Search.read import Reader
from argparse import ArgumentParser

<<<<<<< HEAD
from Search.search import Search

import argparse
=======
>>>>>>> 4789ac59c7dacae5b0d459968344c4c0cd343983

app = Flask(__name__)
rd = Reader()
sh = Searcher(rd)


@app.route('/')
def index():
    result = []
    query = request.args.get('search')
    if query:
        type_ = request.args.get('option', 'tfidf')
<<<<<<< HEAD
        result = Search.Search(type_, query)
=======
        result = sh.Search(type_, query)
>>>>>>> 4789ac59c7dacae5b0d459968344c4c0cd343983
        return render_template('index.html', result=result)
    return render_template('index.html')


def pars_args():
    """Settings for argparse"""
    parser = ArgumentParser(prog='Поиск по дампам Википедии',
            usage='Перед первым запуском приложения нужно построить индекс.',
            description='Для построения запустите приложение с ключом -i.')

    parser.add_argument('-i', help='Тип индекса на выбор, all - построить все.',
                        type=str, choices=('all', 'boolean', 'article', 'tfidf'))

    return parser.parse_args()


if __name__ == '__main__':
    args = pars_args()
    if args.i:
        from Search.index import Build
        Build(args.i)
    else:
        app.run(debug=True)
