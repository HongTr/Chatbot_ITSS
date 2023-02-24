from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import ValidationAction

listEntity = ['location', 'qos_constraint', "traffic", 'qos_value', 'qos_unit',
 'operation', 'service', 'middlebox', 'qos_metric', 'hour', 'group', 'protocol']
message = {}

class ActionBuild(Action):
    def name(self) -> Text:
        return "action_build"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        hasEntity = 0
        dispatcher.utter_message("Your command has some entities like: ")
        count = 0
        for entity in listEntity:
            names = list(tracker.get_latest_entity_values(entity_type=str(entity)))
            listExample = []
            if len(names) > 0:
                hasEntity = 1
                # message += str(count) + ". " + str(entity) + ":\n"
                for name in names:
                    if name:
                        listExample.append(name)
                message[entity] = listExample
        if hasEntity:
            for key in message.keys():
                count += 1
                dispatcher.utter_message(f"{count}. {key}")
                for element in message[key]:
                    dispatcher.utter_message(f"- {element}")
        else:
            dispatcher.utter_message("Your command is hard to understand!")
        return []
    
class ActionFeedback(Action):
    def name(self) -> Text:
        return "action_restart"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message = {}
        return [] 


