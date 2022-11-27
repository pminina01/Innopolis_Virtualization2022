import json
from receive import consumer
from send import producer

config_path = "config.json"
with open(config_path) as f:
    config = json.loads(f.read())

consumer(config['user'], config['password'], config['host'])
producer(config['user'], config['password'], config['host'])