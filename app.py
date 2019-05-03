from flask import Flask, request, jsonify, redirect
from serve import run_model_prediction
import logging


app = Flask(__name__)
model_prediction = run_model_prediction()

@app.route('/')
def index_redirect():
    return 'TRY IT OUT'
    # return redirect('http://catli.github.io', code = 302)


@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def url_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace
    """.format(e), 500


@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    logging.info('running....')
    output_data = run_model_prediction()
    print(output_data)
    response = jsonify({'prediction': output_data})
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)