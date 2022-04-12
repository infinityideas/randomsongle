from flask import Flask, request, make_response
import configparser
import sys
import pusher
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

pusher_client = pusher.Pusher(
    app_id=config['PUSHER']['app_id'],
    key=config['PUSHER']['key'],
    secret=config['PUSHER']['secret'],
    cluster=config['PUSHER']['cluster'],
    ssl=True
)

app = Flask(__name__)

def checkavailable(name):
    check = pusher_client.channel_info(name, {'info': ['subscription-count']})

    return check['occupied']

@app.route('/getrandomurl', methods=['GET'])
def getrandomurl():
    songid = request.args.get('id')
    postRequestData = json.dumps({"jsonrpc": "2.0", "method": "generateStrings", "params": {"apiKey": config['RANDOM']['api_key'], "n": 1, "length": 12, "characters": "abcdefghijklmnopqrstuvwxyz1234567890"}, "id": 6512})
    response = requests.post("https://api.random.org/json-rpc/4/invoke", postRequestData, headers={"Content-Type": "application/json"})
    while checkavailable(response.json()['result']['random']['data'][0]):
        response = requests.post("https://api.random.org/json-rpc/4/invoke", postRequestData, headers={"Content-Type": "application/json"})
    
    resp = make_response({"url": config['MISC']['flask_address']+"/challengegame/"+str(songid)+"-"+response.json()['result']['random']['data'][0]})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/ne', methods=['GET'])
def ne():
    typeE = request.args.get('type')
    channel = request.args.get('channel')

    pusher_client.trigger(channel, 'ne', {u'message': typeE})
    return ''