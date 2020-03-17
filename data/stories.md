## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## recipe happy path
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

## how path
* how
 - action_how_lookup

## step path
* step
  - action_step_lookup
  - utter_greet