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
    # return f"<h1>{msj * int(num)}</h1>" - This is all displayed in one line
    output = ""
    for i in range(0,int(num)):
        output += f"<h1>{msj}</h1>"
    return output

@app.errorhandler(404) #app name
def not_found(e): # inbuilt function which takes error as parameter
    return "<h1>Sorry! No response. Try again.</h1>" #defining function - This could call as well a template

# Errors
# HTTP 300: MULTIPLE_CHOICES
# HTTP 301: MOVED_PERMANENTLY
# HTTP 302: FOUND
# HTTP 303: SEE_OTHER
# HTTP 304: NOT_MODIFIED
# HTTP 305: USE_PROXY
# HTTP 306: RESERVED
# HTTP 307: TEMPORARY_REDIRECT
# HTTP 302: NOT FOUND

if __name__ == "__main__":
    app.run( debug = True ) #This needs to do at te end of the app so it takes all the commands included above during the debug 