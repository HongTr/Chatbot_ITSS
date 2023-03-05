from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


listEntity = ['location', 'qos_constraint', "traffic", 'qos_value', 'qos_unit',
 'operation', 'service', 'middlebox', 'qos_metric', 'hour', 'group', 'protocol']
message = {}
errorExample = ""
trueEntity = ""

class ActionBuild(Action):
    def name(self) -> Text:
        return "action_build"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        hasEntity = 0
        count = 0
        for entity in listEntity:
            names = list(tracker.get_latest_entity_values(entity_type=str(entity)))
            listExample = []
            if len(names) > 0:
                hasEntity = 1
                for name in names:
                    if name:
                        listExample.append(name)
                message[entity] = listExample
        if hasEntity:
            temp = ""
            for key in message.keys():
                count += 1
                temp += f"{count}. {key}\n"
                for element in message[key]:
                    temp += f"- {element}\n"
            dispatcher.utter_message("Your command is: ")
            dispatcher.utter_message(temp)
            dispatcher.utter_message("Is that correct?")
            
        else:
            dispatcher.utter_message("Your command is hard to understand!")
        return []

class ActionErrorExample(Action):
    def name(self) -> Text:
        return "action_errorExample"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global errorExample

        for entity in listEntity:
            name = list(tracker.get_latest_entity_values(entity_type=str(entity)))
            if len(name) == 1:
                errorExample = name[0]
                break
        return []
    
class ActionTrueEntity(Action):
    def name(self) -> Text:
        return "action_trueEntity"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global trueEntity
        latest_message = tracker.latest_message.get("text", "").strip().lower()
        latest_message = latest_message[1:]
        trueEntity = latest_message
        return []

class ActionCorrectDictionary(Action):
    def name(self) -> Text:
        return "action_correctDictionary"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message, errorExample, trueEntity
        for key, values in message.items():
            if errorExample in values:
                values.remove(errorExample)
        if trueEntity not in message:
            message[trueEntity] = []
            message[trueEntity].append(errorExample)
        else:
            message[trueEntity].append(errorExample)

        for key in list(message.keys()):
            if len(message[key]) == 0:
                del message[key]
        temp = ""
        count = 0
        for key in message.keys():
            count += 1
            temp += f"{count}. {key}\n"
            for element in message[key]:
                temp += f"- {element}\n"
        dispatcher.utter_message("Your command is: ")
        dispatcher.utter_message(temp)
        dispatcher.utter_message("Is that correct?")
        return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message,errorExample,trueEntity
        message = {}
        return [] 