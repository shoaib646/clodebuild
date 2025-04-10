from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Wild Rydes</title>
        <style>
            body { text-align: center; padding: 150px; }
            h1 { font-size: 40px; }
        </style>
    </head>
    <body>
        <h1>Welcome to Wild Rydes!</h1>
        <p>Our magical app is running successfully in ECS Fargate!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)