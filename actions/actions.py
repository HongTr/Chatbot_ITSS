from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
     def name(self) -> Text:
         return "action_greet"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user = tracker.get_slot("name")
        if (user):
            dispatcher.utter_message(f"Hey {user}! How can i help you")
        else:
            dispatcher.utter_message("Hi, what can i do for you?")
        return []
