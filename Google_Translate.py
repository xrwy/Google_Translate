from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def main():
    return render_template('google_translate.html', translateResult = '')

@app.route('/google_translate', methods = ['GET','POST'])
def googleTranslate():
    if request.method == 'POST':
        text = request.form['text']
        fromLang = request.form['from_lang']
        toLang = request.form['to_lang']
        if text == '' or fromLang == '' or toLang == '':
            return 'Do not leave the fields blank'
        try:
            translator = Translator(from_lang=fromLang, to_lang=toLang)
            translateResult = translator.translate(text)
            return render_template('google_translate.html', translateResult = translateResult)
        except Exception as e:
            return "Error : " + str(e)

    else:
        return 'For post requests only.'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
