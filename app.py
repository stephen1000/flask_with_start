from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "hey there you sexy fiend, you come here often?"

