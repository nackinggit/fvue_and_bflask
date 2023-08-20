from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

bots = [{
  "name": "客服实验",
  "title": "技術客服",
  "email": "Tech_boy@gmail.com",
  "photo": "img/friends/Tech_boy.png",
  "messageNum": 2,
  "prompt": "我是一号"
},
{
  "name": "客服2",
  "title": "技術客服2",
  "email": "Tech_boy@gmail.com",
  "photo": "img/friends/Tech_boy.png",
  "messageNum": 0,
  "prompt": "我是二号"
}]

chat_bot_messages = {
    "客服": [{
  'messageType': 'cmsg',
  'icon': '../images/B.jpg',
  'name': 'nnkk',
  'position': 'cright',
  'content': '当无昵时候, name 字段留空即可'
}, {
  'messageType': 'cmsg',
  'icon': '../images/B.jpg',
  'name': 'nnkk',
  'position': 'cleft',
  'content': '你说我回复不回复'
}],
    "客服2": [{
  'messageType': 'cmsg',
  'icon': '../images/B.jpg',
  'name': 'nnkk',
  'position': 'cright',
  'content': '当无昵时候, name 字段留空即可'
}, {
  'messageType': 'cmsg',
  'icon': '../images/B.jpg',
  'name': 'nnkk',
  'position': 'cleft',
  'content': '你说我回复不回复'
}]
}

@app.route("/chat_bot/list")
def chat_bot_list():
    return jsonify(bots)

@app.route("/chat", methods=['POST'])
def hello_world():
    request_text = ''
    if request.is_json:
        req_data = request.json
        request_text = req_data.get('content')
    else:
        return "Content type is not supported."
    return jsonify({
        'resp_text': 'hello, I response you: ' + request_text
    })

@app.route("/history/chat_bot", methods = ['POST'])
def chat_bot_history():
    chatbot = ''
    if request.is_json:
        req_data = request.json
        chatbot = req_data.get('bot_name')
    else:
        return "Content type is not supported."
    return jsonify(chat_bot_messages[chatbot])

if __name__ == '__main__':
    app.run(host='0.0.0.0')