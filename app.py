from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello-world():
    return 'GreyMatters'

if__name__=="__main__":
    app.run()
