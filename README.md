
## PlaVak
PlaVak is a travel chatbot that can assist users from start to end of vacation planning.

## Intents and Stories
On the whole, 33 intents and 20 stories have been implemented.

## Conversation Flow and Screenshots
Conversation Flow and Screenshots are present in ConversationFlow&Screenshots.pdf file.

## Implementation steps
Steps to follow while running this code:-

1. Please run the .ipynb notebook.
2. After setting up the ngrok tunnel from the notebook, install:- 
	a) rasa 1.10.3 -> pip install rasa==1.10.3
	b) spacy -> python -m spacy download en
	c) nest-asyncio -> pip install nest_asyncio==1.3.3
3. Please traverse to the folder where you have downloaded PlaVak Chatbot folder.
4. Already trained model is present in the models/ folder. If you want to train it again, please enter 'rasa train'
5. After training is completed, enter 'rasa run actions & rasa shell' and the chatbot will be loaded.
6. Since I have used the weather API, in weather.py I would have imported requests. If an error is thrown, please install requests using the command -> pip install requests.
7. Please make sure the path to the csv files are reachable to actions.py. 

## Current Scope
1. The vacation rental booking, local food suggestions and local activities have been implemented for a few selective places that are present in the csv files.
2. Since the payment functionality has not been included, the details are being emailed to the users.
3. The email services take in dummy email addresses. This can be developed to send emails when implemented in application level. 

## References
Code reference for weather API implementation: https://innovationyourself.com/calling-weather-api-in-rasa/

