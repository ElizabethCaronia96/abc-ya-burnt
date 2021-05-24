from flask import Flask, request, jsonify
from markov1 import markov1
app = Flask(__name__)

@app.route('/tell', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    acceptable_risk = request.args.get("ar", 0)
    response = {}
    print(f"ar {acceptable_risk}")
    # Check if user sent a name at all
    if not acceptable_risk:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif not str(acceptable_risk).isnumeric():
        response["ERROR"] = f"risk must be numeric. {acceptable_risk}"
    # Now the user entered a valid name
    else:
        acceptable_risk = float(acceptable_risk)
        calculated_risk = markov1.ask_for_probability(acceptable_risk)
        response["MESSAGE"] = f"Welcome {calculated_risk} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)