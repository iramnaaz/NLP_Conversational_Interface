from typing import Dict, Text, Any, List, Union, Optional

from ConvoFunctions import JustGetRecipe, IngredientLookup, StepNavigation
from whatFunction import whatIs
from howToFunction import howTo

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

import json

class ActionHelloWorld(Action):

	def name(self) -> Text:
		return "action_hello_world"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Hello World!")

		return []

class ActionIngredientLookup(Action):

	def name(self) -> Text:
		return "action_ingredient_lookup"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		ing = IngredientLookup((tracker.latest_message)["text"])
		s = ''
		try:
			s = '\n'.join(json.dumps(d) for d in ing)
		except:
			s = ''
		dispatcher.utter_message(text=s)
		return [SlotSet("ingredient_value", ing)]

class ActionWhatLookup(Action):

	def name(self) -> Text:
		return "action_what_lookup"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		ans = whatIs((tracker.latest_message)["text"])
		dispatcher.utter_message(text=ans)
		return []

class ActionHowLookup(Action):

	def name(self) -> Text:
		return "action_how_lookup"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		ans = howTo((tracker.latest_message)["text"])
		dispatcher.utter_message(text=ans)
		return []

class ActionStepLookup(Action):

	def name(self) -> Text:
		return "action_step_lookup"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		curr = tracker.get_slot('direction_step')
		(ans, num) = StepNavigation((tracker.latest_message)["text"], curr)
		if(ans == ''):
			(ans, num) = StepNavigation("first step", curr)
		a = "Step " + str(num) ". " + ans
		dispatcher.utter_message(text=a)
		return [SlotSet("direction_step", num)]

class RecipeForm(FormAction):
	def name(self) -> Text:
		"""Unique identifier of the form"""
		return "recipe_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["recipe_url"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		"""A dictionary to map required slots to
			- an extracted entity
			- intent: value pairs
			- a whole message
			or a list of them, where a first match will be picked"""

		return {
			# "cuisine": self.from_entity(entity="cuisine", not_intent="chitchat"),
			# "num_people": [
			#     self.from_entity(
			#         entity="num_people", intent=["inform", "request_restaurant"]
			#     ),
			#     self.from_entity(entity="number"),
			# ],
			# "outdoor_seating": [
			#     self.from_entity(entity="seating"),
			#     self.from_intent(intent="affirm", value=True),
			#     self.from_intent(intent="deny", value=False),
			# ],
			# "preferences": [
			#     self.from_intent(intent="deny", value="no additional preferences"),
			#     self.from_text(not_intent="affirm"),
			# ],
			"recipe_url": self.from_text()
		}

	def validate_recipe_url(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		if "www" in value:
			return {"recipe_url": value}
		else:
			dispatcher.utter_message(text="sorry that's not a URL")
			# validation failed, set slot to None
			return {"recipe_url": None}

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:
		"""Define what the form has to do
			after all required slots are filled"""

		url = tracker.get_slot('recipe_url')
		rec = JustGetRecipe(url)
		# utter submit template
		dispatcher.utter_message(template="utter_submit")
		return []
