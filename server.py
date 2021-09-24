from flask import Flask

app = Flask( __name__ )

@app.route ('/', methods=['GET'])
def sayHello():
    return 'Hello World'

@app.route ('/dojo', methods=['GET'])
def sayDojo():
    return 'Dojo'

@app.route ('/say/<msj>', methods=['GET'])
def sayMsj(msj): 
    return f"Hello {msj.capitalize()}!" 

@app.route ('/repeat/<num>/<msj>', methods=['GET'])
def multiplyMsj(num,msj): 
    return f"<h1>{msj * int(num)}</h1>"

if __name__ == "__main__":
    app.run( debug = True ) #This needs to do at te end of the app so it takes all the commands included above during the debug 