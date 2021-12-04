## happy path
* greet
  - utter_greet
* happy
  - utter_happy

## sad path
* greet
  - utter_greet
* sad
  - utter_sad
* goodbye
  - utter_goodbye

## check out
* goodbye
  - utter_goodbye

## book flight choose
* book_flight
  - utter_book_flight
* start_end_location
  - utter_start_end_location
* start_end_date
  - utter_start_end_date
* no_of_passengers
  - utter_ask_email
* get_email
  - action_email_slot
* flight_choose
  - action_detail_flights
  - utter_confirmation

## details incorrect endlocation
* confirm_incorrect_endlocation
  - action_detect_details
  - action_detail_flights
  - utter_confirmation

## details incorrect startlocation
* confirm_incorrect_startlocation
  - action_detect_details
  - action_detail_flights
  - utter_confirmation

## details incorrect startdate
* confirm_incorrect_startdate
  - action_detect_details
  - action_detail_flights
  - utter_confirmation

## details incorrect returndate
* confirm_incorrect_returndate
  - action_detect_details
  - action_detail_flights
  - utter_confirmation

## details correct good feedback
* confirm_correct
  - utter_airline_time
  - utter_flight_choose
  - utter_after_flight_choose
* appreciate
  - utter_appreciate
  - utter_after_appreciate
* feedback_good
  - utter_feedback_good
* goodbye
  - utter_goodbye

## details correct bad feedback
* confirm_correct
  - utter_airline_time
  - utter_flight_choose
  - utter_after_flight_choose
* appreciate
  - utter_appreciate
  - utter_after_appreciate
* feedback_bad
  - utter_feedback_bad
* goodbye
  - utter_goodbye

## Christmas vacation
* not_knowing
  - utter_not_knowing
* winter_christmas
  - utter_winter_christmas
* activity_mention
  - action_suggest_places
  - utter_activity_mention

## Summer vacation
* not_knowing
  - utter_not_knowing
* summer_vacation
  - utter_summer_vacation
* summer_activity_mention
  - action_suggest_places
  - utter_summer_activity_mention

## Trendy vacation
* trend
  - utter_trend
* activity_mention
  - action_suggest_places
  - utter_activity_mention

## Flight and Vacation Rental booking
* book_vacation_rental
  - action_endloc_present
* recognize_flight_and_rental_booking_location
  - utter_recognize_flight_and_rental_booking_location
* duration_of_stay
  - utter_duration_of_stay
  - action_suggest_rental
  - utter_duration_of_stay_deny

## Only Vacation Rental booking
* book_vacation_rental
  - action_endloc_present
* recognize_rental_booking_location
  - action_detect_rentallocation
  - utter_recognize_flight_and_rental_booking_location
* duration_of_stay
  - utter_ask_email
* get_email
  - action_email_slot
  - action_suggest_rental
  - utter_duration_of_stay_deny

## Incomprehensible
* incomprehensible
  - utter_incomprehensible

## local food suggestion 1
* local_food 
  - action_local_food

## local activity suggestion 1
* local_activity
  - action_local_activities

## Weather forecast small talk after booking
* weather_forecast
  - action_weather_api

## bot challenge
* bot_detail
  - utter_bot_detail