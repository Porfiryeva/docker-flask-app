import pandas as pd
import dill
import json
import os
from flask import Flask, request
import numpy as np

app = Flask(__name__)

# path = '/home/user/PycharmProjects/app/app/models/'
path = '/app/app/models/'

with open(path + 'pipeline.dill', 'rb') as in_strm:
    model = dill.load(in_strm)


@app.route('/', methods=['GET'])
def general():
    return 'Welcome to prediction process'


@app.route('/predict', methods=['POST'])
def predict():
    data = {'success': False}

    columns = ['age', 'workclass', 'fnlwgt', 'education', 'education.num', 'marital.status',
               'occupation', 'relationship', 'race', 'capital.gain', 'capital.loss',
               'hours.per.week']
    test_data = pd.DataFrame(data=[['' for i in range(len(columns))]], columns=columns)

    request_json = request.get_json()

    for col in test_data.columns:
        if request_json[col] or request_json[col] == 0:
            test_data[col] = request_json[col]

    try:
        preds = model.predict_proba(test_data)
    except TypeError as e:
        data['predictions'] = str(e)
        return json.dumps(data)

    data['predictions'] = preds[:, 1][0]
    data['success'] = True
    print('OK')

    return json.dumps(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)
