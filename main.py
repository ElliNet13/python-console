import sys

import re

def censor_ips(text):
    # Regular expression pattern for IPv4 addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # Replace all IP addresses with '[CENSORED]'
    censored_text = re.sub(ip_pattern, '[IP CENSORED]', text)
    return censored_text

with open('app.log', 'w') as file:
    pass

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# Redirect stdout and stderr to the Logger
sys.stdout = Logger('app.log')
sys.stderr = Logger('app.log')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('redirect.html', code=censor_ips(open('app.log').read().replace('\n', '<br>')))

if __name__ == '__main__':
    app.run(debug=True)