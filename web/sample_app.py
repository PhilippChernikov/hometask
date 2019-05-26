
import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/prime', methods = ['GET'])
def prime():
    if request.method == 'GET':
        a = request.args.get('num')
    elif request.method == 'POST':
        a = request.form.get('num')
    if a == None:
        a = 0

    def ifp(a):
        try:
            a = int(a)
            if a <= 0:
                print("не является простым числом")
            elif a in [1, 2, 3]:
                print("простое число")
            else:
                for i in range(2, int(a ** (0.5) + 1)):
                    if a % i == 0:
                        print("не является простым числом")
                    else:
                        print("простое число")
        except:
            print("Введите ЧИСЛО")

    return flask.render_template(
        'prime.html',
        que = a,
        ans = ifp(a),
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)

