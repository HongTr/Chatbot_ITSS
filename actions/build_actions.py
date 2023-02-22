from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionBuild(Action):
    def name(self) -> Text:
        return "action_build"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Your command is: ")
        location = tracker.get_latest_entity_values("location")
        if location:
            dispatcher.utter_message("Location: {location}")
        operation = tracker.get_latest_entity_values("operation")
        if location:
            dispatcher.utter_message("Operation: {location}")
        return []