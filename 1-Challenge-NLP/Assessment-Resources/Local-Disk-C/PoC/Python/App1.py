key = "9faa1d923ef54a96a61b4400920fb07a"
endpoint = "https://lang-37340736.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
text_analytics_credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=text_analytics_credential)

# Method for recognizing content in documents 
def recognize_your_text(client):
    documents = [
        "Call our office at 312-555-1234 and ask for Graham Barnes, or send an email to support@contoso.com."
    ]

    # Replace null with the correct method to recognize the requested information.
    response = client.recognize_entities(documents, language="en")

    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        # print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))

recognize_your_text(text_analytics_client)
