from flask import Flask


app= Flask(__name__)
@app.route('/')
def hello_world():
    return '<body style=background-color:pink;><h1>Welcome to my HOME PAGE<b></b></body>'


@app.route('/Admin_Page/')
def Admin_Page():
    return '<body style=background-color:pink;><h1>Welcome to my Admin Page</body>'


@app.route('/Guest_Page/')
def Guest_Page():
    return '<body style=background-color:blue;><h1>Welcome to Guest Page </body>'



@app.route('/User_Page/')
def User_Page():
    return '<body style=background-color:purple;><h1>Welcome to User Page</body>'



if __name__ == '__main__':
    app.debug= True
    app.run()
