''' Translation logic'''


import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2022-07-22',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')




def english_to_french(english_text):
    ''' Convert English Language to French'''

    if len(english_text) <=0:
        return "Text is Empty"
    translation= language_translator.translate(english_text, model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


def french_to_english(french_text):
    ''' Convert French Language To English '''

    if len(french_text) <=0:
        return "Text is Empty"

    translation= language_translator.translate(french_text, model_id='fr-en').get_result() 
    return translation['translations'][0]['translation']
