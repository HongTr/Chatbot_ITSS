from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import arrow, dateparser
from datetime import datetime

#dispatcher object sends message back to users
#tracker object fetch information (slot, entity, intent)
#domain object --> domain.yaml


################################Template################################
# class ActionHelloWorld(Action):
#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return []
########################################################################

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
