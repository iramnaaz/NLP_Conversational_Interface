## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## recipe happy path
* greet
  - utter_greet
* recipe
  - utter_url_ask
  - recipe_form
  - form{"name": "restaurant_form"}
  - utter_submit
  - utter_ing_or_recipe

## ingredient ask
* ingredient
 - action_ingredient_lookup
 - utter_ing_or_recipe

## what path
* what
 - action_what_lookup
 - utter_ing_or_recipe

## how path
* how
 - action_how_lookup
 -utter_ing_or_recipe

