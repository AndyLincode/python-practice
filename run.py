from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hello!!"


@app.route('/getCountry', methods=['GET', 'POST'])
def getCountry():
    data = [{'name': 'Taiwan', 'value': 'TW'}, {
        'name': 'Japan', 'value': 'JP'}, {'name': 'USA', 'value': 'US'}]
    return jsonify(data)


@app.route('/getCity', methods=['POST'])
def getCity():
    data = request.get_json()
    i_country = data.get('i_country')

    if i_country == 'TW':
        city = [{'name': '新北市', 'value': 'NTPC'}, {'name': '桃園市',
                                                   'value': 'TYN'}, {'name': '台南市', 'value': 'TNN'}]
    elif i_country == 'JP':
        city = [{'name': '東京', 'value': 'TKY'}, {'name': '大阪', 'value': 'OSA'}]
    elif i_country == 'US':
        city = [{'name': '洛杉磯', 'value': 'LA'}, {'name': '紐約', 'value': 'NY'}]
    return jsonify(city)


@app.route('/getArea', methods=['POST'])
def getArea():
    data = request.get_json()
    i_city = data.get('i_city')

    if i_city == 'NTPC':
        area = [{'name': '蘆洲', 'value': 'LZ'}, {'name': '三重', 'value': 'SC'}]
    elif i_city == 'TYN':
        area = [{'name': '八德', 'value': 'BD'}, {'name': '青埔', 'value': 'CP'}]
    elif i_city == 'TNN':
        area = [{'name': '安平', 'value': 'AP'}, {'name': '永康', 'value': 'YK'}]
    elif i_city == 'TKY':
        area = [{'name': '築地', 'value': 'JD'}, {'name': '新宿', 'value': 'CC'}]
    elif i_city == 'OSA':
        area = [{'name': '奈良', 'value': 'NL'}, {'name': '京都', 'value': 'KT'}]
    elif i_city == 'LA':
        area = [{'name': '就是LA沒去過', 'value': 'LAA'}]
    elif i_city == 'NY':
        area = [{'name': '我只知道皇后區', 'value': 'QU'}]
    return jsonify(area)


if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
