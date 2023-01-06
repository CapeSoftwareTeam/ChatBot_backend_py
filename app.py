from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

data =  [
        {
         "pat": ["Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day"],
         "res": "Hi there, how can I help?"
        },
        {
         "pat": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"],
         "res":  "Have a nice day"
        },
        {
         "pat": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
         "res": "Happy to help!"
        },
        {
         "pat": ["How you could help me?", "What help you provide?", "How you can be helpful?"],
         "res": "I can guide you through Adverse management problems, order tracking, person to be contacted and Department related queries"
        },
        {
          "pat": ["where is order with id 431B67?", "track order 562B78", "Where is my order with id 561A24?" ],
          "res": "On the Way!"
        },
        {
         "pat": ["order id 345A23 comprises of?","List of components"],
         "res":"order comprises of hardisk and bluetooth"
        }
   ]

app = Flask(__name__)
CORS(app)
@app.get("/" )
def index():
	text = request.args.get("q")
	fin = "Something went Wrong"
	for x in data:
		for i in x["pat"]:
			if(text==i):
				fin = x["res"]
				break
				
	return jsonify({"msg":fin})

if __name__ == "__main__":
	app.run(debug=True)