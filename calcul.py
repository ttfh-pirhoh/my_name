from flask import Flask, request, make_response, jsonify
pi=0
# initialize the flask app
app = Flask(__name__)
resultat=0.0
action=0
req=0
# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    global pi
    global action
    # fetch action from json
    action = req.get('queryResult').get('action')
    param=pi['queryResult']['parameters']
    # return a fulfillment response
    return {'fulfillmentText': resultat}
# create a route for webhook
@app.route('/web', methods=['GET', 'POST'])
def webhook():
    # return response
    global pi
    global action
    req = request.get_json(force=True)
    action=req.get('queryResult').get('action')
    pi=request.get_json(force=True)
    param=pi['queryResult']['parameters']
    global resultat
    inten_name=pi['queryResult']['intent']['displayName']
    print(inten_name)
    print("voici l'action".format(action))
    print("fin")
    if inten_name=='calcul' and type(param['a'])==float and type(param['b'])==float:
        
        
        if param['arithmetic']=='/':
            resultat=param['a']/param['b']
        elif param['arithmetic']=='+':
            resultat=param['a']+param['b']
        elif param['arithmetic']=='*':
            resultat=param['a']*param['b']
        elif param['arithmetic']=='-':
            resultat=param['a']-param['b']
        else :
            print("nothing")
            resultat="je n'ai pas bien compris ce que vous avez dit"
        resultat=str(param['a'])+" "+str(param['arithmetic'])+ " "+ str(param['b']) + " = "+str(resultat)
    elif inten_name=='quel est ton nom?':
        resultat="je suis le smart robot cree par TCHOUANTO"
    else:
        resultat="intent non défini"
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    app.run()


    