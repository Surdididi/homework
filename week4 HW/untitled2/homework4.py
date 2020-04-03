from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('shopping mall2.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_review():
   jname_receive = request.form['jname_give']
   jqtt_receive = request.form['jqtt_give']
   jadd_receive = request.form['jadd_give']
   jph_receive = request.form['jph_give']

   order = {
      'jname': jname_receive,
      'jqtt': jqtt_receive,
      'jadd': jadd_receive,
      'jph': jph_receive
   }

   db.orders.insert_one(order)
   return jsonify({'result': 'success', 'msg': '주문이 완료되었어요 :) '})


@app.route('/orders', methods=['GET'])
def read_reviews():
   orders = list(db.orders.find({}, {'_id': 0}))
   return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)