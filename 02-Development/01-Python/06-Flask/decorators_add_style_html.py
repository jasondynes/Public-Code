from flask import Flask

app = Flask(__name__)


# style decorators used below
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tester")
def hello_world2():
    return "<p>Testing Testing!</p>"


@app.route("/teststyle")
def hello_style():
    return "<u><em><b><p>Testing Testing!</p></b></em></u>"


@app.route("/styledecorate")
@make_bold
@make_emphasis
@make_underlined
def hello_style2():
    return "Testing Testing!"


@app.route("/user/<name>")
def hello_user(name):
    return (f' <h1 style="text-align: center"> Hello to user called {name}. Nice to meet you !</h1>'
            f'<p> This is a paragraph</p>'
            f'<img src="https://www.bluecross.org.uk/sites/default/files/d8/styles/theme_feature_extra_large/public/2021-06/BX151919_HY_BC_JACK_SOUTHAMPTON_010-lpr.JPG.webp?itok=eGQaiv_N" width=700, height=500>')


if __name__ == "__main__":
    app.run(debug=True)
