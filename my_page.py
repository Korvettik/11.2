from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])  # главная страница
def main_page():
    page = render_template('index-name.html')
    return page



if __name__ == '__main__':
    app.run(debug=True)