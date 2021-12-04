
## PlaVak
PlaVak is a travel chatbot that can assist users from start to end of vacation planning.

## Intents and Stories
On the whole, 33 intents and 20 stories have been implemented.

## Suggested Conversation Flows and Screenshots
Suggested conversation flows and screenshots are present in [ConversationFlow&Screenshots.pdf](ConversationFlow&Screenshots.pdf) file.

## How to run
Steps to follow while running this code:-

1. Please run the [Plavak_Chatbot.ipynb](Plavak_Chatbot.ipynb) notebook. After running all the cells, a link for ngrok tunnel will appear.
2. Click on the link, enter password 'chat' and open terminal. Install:- rasa 1.10.3 -> ```pip install rasa==1.10.3```
3. Open the folder where you have downloaded PlaVak Chatbot folder.
4. Already trained model is present in the models/ folder. If you want to train it again, please enter ```rasa train```
5. After training is completed, enter ```rasa run actions & rasa shell``` and the chatbot will be loaded. 
6. You can talk to PlaVak now.

## Troubleshooting
1. Since I have used the weather API, in weather.py I would have imported requests. If an error is thrown, please install requests using the command -> ```pip install requests```
2. If data retrieval from the csv fails, please make sure the path to the csv files from actions.py are correctly specified. 

## Current Scope
1. The vacation rental booking, local food suggestions and local activities have been implemented for a few selective places that are present in the csv files.
2. Since the payment functionality has not been included, the details are being emailed to the users.
3. The email services take in dummy email addresses. This can be developed to send emails when implemented in application level. 

## References
Code reference for weather API implementation: https://innovationyourself.com/calling-weather-api-in-rasa/

