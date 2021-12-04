# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from weather import Weather
import pandas as pd
import re

class ActionSlotEmail(Action):

    def name(self) -> Text:
        return "action_email_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rentallocation =  tracker.get_slot("rentalloc")
        if rentallocation is None:
            dispatcher.utter_message(text = f"Alright! I can find you availabilities in the following airlines: 1. Southwest, 2. United, 3. Alaska, 4. Frontier, 5. Delta. Which one would you like to choose?")
        else:
            dispatcher.utter_message(text = f"I found a number of great vacation rentals in " + str(rentallocation) + f".")
        return [SlotSet('emailid',tracker.latest_message['text'])]

class ActionLocalFood(Action):

    def name(self) -> Text:
        return "action_local_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city =  tracker.get_slot("endloc")
        df = pd.read_csv('local_food_items.csv')
        count = 1

        for i, j in df.iterrows():
            if j['area'] == city:
                count = 2
                dispatcher.utter_message(text = f'The following food items are famous in ' + j['area'] + f' are:-')
                dispatcher.utter_message(text = j['local_foods'])

        if city is None:   # case while booking only vacation rental
            city = tracker.get_slot("rentalloc")
        if count == 1:
            dispatcher.utter_message(text = f'I am not aware of the local food in '+ str(city) + f'. The most commonly available food items in any region are: Burger, Fries, Sandwiches and Pizza')
        return []

class ActionLocalActivity(Action):

    def name(self) -> Text:
        return "action_local_activities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place =  tracker.get_slot("endloc")
        df = pd.read_csv('suggest_activities.csv')
        count = 1

        for i, j in df.iterrows():
            if j['city'] == place:
                count = 2
                dispatcher.utter_message(text = f"Activities popular among the people of " + j['city'] + f" are:-")
                dispatcher.utter_message(text = j['activity'])

        if place is None:   # case while booking only vacation rental
            place = tracker.get_slot("rentalloc")
        if count == 1:
            dispatcher.utter_message(text = f'I am not aware of the local activities in '+ str(place) + f'. The popular activities in most of the regions are: Biking, Camping, Hiking and Surfing')
        return []

class ActionSuggestPlace(Action):

    def name(self) -> Text:
        return "action_suggest_places"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        activities =  tracker.get_slot("activity")
        df = pd.read_csv('suggest_places.csv')

        for i, j in df.iterrows():
            if j['category'] == activities:
                dispatcher.utter_message(text = f'The following places are famous for ' + j['category'])
                dispatcher.utter_message(text = j['place'])
        return []

class ActionDetectDetail(Action):

    def name(self) -> Text:
        return "action_detect_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sentence = re.split('\:', tracker.latest_message['text'])
        if sentence[0] == "Departure":
            return [SlotSet('startloc', sentence[1].strip())]   # string.strip() removes any leading or trailing spaces
        elif sentence[0] == "Destination":
            return [SlotSet('endloc', sentence[1].strip())]
        elif sentence[0] == "Starting on":
            return [SlotSet('startdate', sentence[1].strip())]
        elif sentence[0] == "Returning on":
            return [SlotSet('returndate', sentence[1].strip())]

class ActionDetailFlight(Action):

    def name(self) -> Text:
        return "action_detail_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        startlocation = tracker.get_slot("startloc")
        endlocation = tracker.get_slot("endloc")
        startdate = tracker.get_slot("startdate")
        enddate = tracker.get_slot("returndate")
        carrier = tracker.get_slot("airline")

        from csv import writer
        
        List=[carrier, startlocation, endlocation, startdate, enddate]
        
        dispatcher.utter_message(text = f'Flight: ' + str(carrier) + f', Departure: ' + str(startlocation) + f', Destination: ' + str(endlocation) + f', Starting on: ' + str(startdate) + f', Returning on: ' + str(enddate))

        with open('flights_detail.csv', 'a') as f_object:
        
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()

        return []

class ActionDetectEndlocation(Action):

    def name(self) -> Text:
        return "action_endloc_present"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        endcity = tracker.get_slot("endloc")
        if endcity is not None:
            dispatcher.utter_message(text = f'Where would you like to book your vacation rental?')
            return []
        else:
            dispatcher.utter_message(text = f'Where would you like to book your vacation rental? Please provide the information in this format(Rental Location: placename).')
            return []  

class ActionSuggestRentals(Action):

    def name(self) -> Text:
        return "action_suggest_rental"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        endcity =  tracker.get_slot("endloc")
        if endcity == None:    # for cases with only vacation rental booking
            endcity =  tracker.get_slot("rentalloc")
        df = pd.read_csv('suggest_rentals.csv')

        for ind in df.index:
            if df['city'][ind] == endcity:
                dispatcher.utter_message(text = df['view'][ind] + f' view : ' + df['option'][ind])
        return []

class ActionDetectRentallocation(Action):

    def name(self) -> Text:
        return "action_detect_rentallocation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sentence = re.split('\:', tracker.latest_message['text'])
        return [SlotSet('rentalloc', sentence[1].strip())]   # string.strip() removes any leading or trailing spaces

class ActionWeatherForecastCity(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        startlocation = tracker.get_slot("startloc")
        endlocation = tracker.get_slot("endloc")
        rentallocation =  tracker.get_slot("rentalloc")

        if endlocation is None:   # case while booking only vacation rental
            endlocation = rentallocation
        
        temperatureend = int(Weather(endlocation)['temp']-273)

        if startlocation is None:
            dispatcher.utter_message(text = f"Right now the weather in " + str(endlocation) + f" is " + str(temperatureend))
        else:
            temperaturestart = int(Weather(startlocation)['temp']-273)
            dispatcher.utter_message(text = f"Right now the weather in " + str(startlocation) + f" is " + str(temperaturestart) + f" and in " + str(endlocation) + f" is " + str(temperatureend))
        return []