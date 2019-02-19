from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

@app.route('/service/error')
def error():
    return ('{}'.format(os.environ['INSTANCE_ID']), 503)

@app.route('/service/<service_number>')
def hello(service_number):
    return ('Hello from behind Envoy (service {} instance_id {})! hostname: {} resolved'
            'hostname: {}\n'.format(os.environ['SERVICE_NAME'],
                                    os.environ['INSTANCE_ID'],
                                    socket.gethostname(),
                                    socket.gethostbyname(socket.gethostname())))

@app.route('/service/<service_number>/<owner>')
def hello_owner(service_number, owner):
    return ('Hello from behind Envoy (service {} instance_id {})! hostname: {} resolved'
            'hostname: {}\n'.format(os.environ['SERVICE_NAME'],
                                    os.environ['INSTANCE_ID'],
                                    socket.gethostname(),
                                    socket.gethostbyname(socket.gethostname())))

@app.route('/instance/<instance_number>')
def hello_instance(instance_number):
    return ('Hello from behind Envoy (service {} instance_id {})! hostname: {} resolved'
            'hostname: {}\n'.format(os.environ['SERVICE_NAME'],
                                    os.environ['INSTANCE_ID'],
                                    socket.gethostname(),
                                    socket.gethostbyname(socket.gethostname())))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
