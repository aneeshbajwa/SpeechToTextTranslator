#you will need the following library 
!pip install ibm_watson wget

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = ""                  #unique URL that you will get after buying speech to text plan (lite plan is available for free)

iam_apikey_s2t = ""           #unique key you will get after buying speech to text plan

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
#s2t is a speech to taxt adapter object

#downloading desireed audio file
!wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

filename='PolynomialRegressionandPipelines.mp3'

# openning this audio file in read binary mode
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

    
#normalizing the JSON data into a dataframe    
from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")    


recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)


# now for languagee translator

from ibm_watson import LanguageTranslatorV3
url_lt=''
apikey_lt=''

version_lt='2018-05-01'

#creating a languageTranslator objct
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

from pandas import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

#translating the data from english to Spanish
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')


translation=translation_response.get_result()

#selecting sanish translation out of the data frame
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation) 

