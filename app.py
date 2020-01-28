from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    
    # fetch action from json
    action = req.get('queryResult').get('action')
    print("voici l'action")
    print(action)
    print("fin de l'action")
    # return a fulfillment response
    return {'fulfillmentText': 'je suis le smart robot conçu par HERMANN TCHOUANTO'}
# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    pi=request.get_json(force=True)
    
    print(pi)
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    app.run()