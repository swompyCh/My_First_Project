import random

from flask import Flask, render_template

app = Flask(__name__)


list_animal = [
        'Абботины',
        'Абелизавриды',
        'Абиссинская сизоворонка',
        'Абиссинский заяц',
        'Абиссобротула',
        'Азиатские храмули',
        'Азиатские щучки',
        'Азиатский лапчатоног',
        'Азиатский лев',
        'Азиатский муравей-портной',
        'Азиатский паралихт',
        'Азиатский пилорыл',
        'Азиатский слон',
        'Азиатский страус',
        'Азиатский стрелозубый палтус',
        'Азиатский таракан',
        'Азиатский ябиру',
        'Азовская пуголовка',
        'Азовская шемая',
        'Азовская щиповка',
        'Азовский пузанок',
        'Азорская вечерница',
        'Азорский снегирь',
    ]


@app.route('/animal')
def animal():
    animal = list_animal[random.randint(1, len(list_animal))]
    return render_template("index_animal.html", animal=animal, list_animal=list_animal)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/first')
def rome():
    return render_template("index_first.html")


@app.route('/second')
def rom():
    return render_template("index_second.html")


if __name__ == '__main__':
    app.run(debug=True)
