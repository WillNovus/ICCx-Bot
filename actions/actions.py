# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

'''from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckHalls(Action):
    def name(self) -> Text:
        return "action_check_halls"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        hall = tracker.get_slot('Hall')
        x = "select * from halls where Hall = {hall} limit 1".format('Hall')
        result = db.query(x)

        dispatcher.utter_message(text="Hello World!")

        return []'''
