from typing import Dict, Any, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionLoop(Action):
    def name(self) -> Text:
        return "acion_loop"
    def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        message = "Is there anything else I missed?"
        buttons = [
            {"title": "Yes", "payload": "/confirm"},
            {"title": "No", "payload": "/deny"}
        ]

        # send initial message with buttons
        dispatcher.utter_button_message(text=message, buttons=buttons)

        # loop until user clicks "No" button
        while True:
            # get user's latest message
            latest_message = tracker.latest_message.get("text", "").strip().lower()

            if latest_message == "/no":
                # user clicked "No" button, break out of loop
                break
            elif latest_message == "/yes":
                
                return []

        # user clicked "No" button, do something
        dispatcher.utter_message(text="OK, thank for your feedback.")
        return []
