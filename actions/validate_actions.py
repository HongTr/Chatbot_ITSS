from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
ALLOWED_ENTITY = [
"group", "location", "middlebox", "service", "traffic", "protocol"
]

class ValidateCommandFeedbackForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_command_feedback_form"

    def validate_entity(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value.lower() not in ALLOWED_ENTITY:
            dispatcher.utter_message(text = f"Your required entity is invalid.")
            msg = ""
            msg += f"Valid entities include {'/'.join(ALLOWED_ENTITY)}"
            dispatcher.utter_message(msg)
            #return {"entity": None}
            SlotSet("entity", None)
        dispatcher.utter_message(f"Ok, i understand that {slot_value} is wrong.")
        # return {"entity": slot_value}
        SlotSet("entity", slot_value)
        return []

    def validate_value(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value:
            # return {"value": slot_value}
            SlotSet("value", slot_value)
        SlotSet("value", None)
        # return {"value": None}
        return []
    
   