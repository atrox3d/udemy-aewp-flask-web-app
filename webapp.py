from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    print('GET request string')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home_post():
    d1 = request.form['first_dim']
    d2 = request.form['second_dim']
    d3 = request.form['third_dim']
    volume = float(d1) * float(d2) * float(d3)
    # volume = 1
    # for dim in [float(x) for x in request.form.values()]:
    #     volume *= dim
    print(volume)
    print('POST request string')
    return render_template(
                                'index.html',
                                volume=volume,
                                d1=d1,
                                d2=d2,
                                d3=d3,
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
