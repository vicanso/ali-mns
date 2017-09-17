#coding:utf-8
import os
from flask import Flask, jsonify, request
from mns.account import Account
from mns.topic import DirectSMSInfo, TopicMessage, MNSExceptionBase

app = Flask(__name__)
account = Account(os.getenv('END_POINT'), os.getenv('ACCESS_ID'), os.getenv('ACCESS_KEY'))
topic = account.get_topic(os.getenv('TOPIC'))

class InvalidUsage(Exception):
  status_code = 400

  def __init__(self, message, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
        self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response

@app.after_request
def apply_caching(response):
  if response.headers.get("Cache-Control") is None:
    response.headers["Cache-Control"] = "no-cache"
  return response

@app.route('/ping')
def ping():
  return "pong"

@app.route('/sms/<phone>', methods=['POST'])
def sms(phone):
  data = request.get_json()
  if request.headers.get('Token') != 'OKNtCOuvRd':
    raise InvalidUsage('toke is invalid')

  # 初始化短信发送的相关配置信息
  smsAttr = DirectSMSInfo(free_sign_name=data.get('sign'), template_code=data.get('template'), single=False)
  smsAttr.add_receiver(receiver=phone, params=data.get('params'))
  # 生成发送短信的 topic
  msg = TopicMessage(data.get('content'), direct_sms = smsAttr)
  try:
    result = topic.publish_message(msg)
    print result.message_id
    return jsonify({
      'id': result.message_id
    }) 
  except MNSExceptionBase,e:
    raise InvalidUsage(e.message, status_code=500)

app.run(host='0.0.0.0')
