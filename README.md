# NLP_Conversational_Interface
Project3 

General Overview:
This project covers the basics required from the assignment as a simple chatbot for our recipe functions from the last project. For extra credit, this whole implementation is in Rasa.

Chatbot Functions:
* Accept Recipe URL and load in recipe
* Read out Ingredients list
* Navigate through steps of ingredient
	- Use both relative and direct step directions
* Ask what is/how to questions at any point

System Requirements:
Rasa does not run above python3.7 so if possible, please downgrade to this version to run our code

How to Run:
1. Open two terminals (this is because of Rasa's limitation with it's custom action server)
1. Install requirement using requirements.txt in either
2. On the first terminal, from root, run `python -m rasa_sdk.endpoint --actions actions`
3. On the second terminal, from root, run `python -m rasa shell --enable-api --endpoints endpoints.yml`