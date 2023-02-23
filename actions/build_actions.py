from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

listEntity = ['location', 'qos_constraint', "traffic", 'qos_value', 'qos_unit',
 'operation', 'service', 'middlebox', 'qos_metric', 'hour', 'group', 'protocol']

class ActionBuild(Action):
    def name(self) -> Text:
        return "action_build"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Your command is: ")
        for entity in listEntity:
            names = list(tracker.get_latest_entity_values(entity_type=str(entity)))
            if len(names) > 0:
                dispatcher.utter_message(str(entity) + ": ")
                for name in names:
                    if name:
                        dispatcher.utter_message(f"- {name}")
        return []