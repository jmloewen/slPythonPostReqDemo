import json
import requests
import boto3

RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"
lambda_client = boto3.client('lambda', region_name="us-east-1",)
appList = ['cat', 'notes', 'voicetunnel']

def isPostRequest(event):
    return str(event['requestContext']['httpMethod']) == "POST"

def unwrapEvent(event):
    wrappedPayload = json.loads(event['body'])
    return wrappedPayload['payload'], wrappedPayload['sender']

def postRasaForIntent(payload):
    r = requests.post(RASASERVER_URL, json={"q": payload})
    return r.json()

def intentNameFrom(rasaJson):
    return rasaJson['intent']['name']

def wrapIntentSpeakAction(rasaJson, sender):
    bodyPayload = {
        "actionType": "speak",
        "actionDetail": intentNameFrom(rasaJson)
    }
    body = {
        "receiver": sender, # always send back to the sender for now...
        "payload": bodyPayload
    }
    return { "statusCode": 200, "body": json.dumps(body) }

def callCatApp(payload):
    response = lambda_client.invoke(
        FunctionName="aws-python-simple-http-endpoint-dev-CatAppOnStart",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )
    string_response = response["Payload"].read().decode('utf-8')
    parsed_response = json.loads(string_response)
    return parsed_response

def endpoint(event, context):
    if not isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}

    payload, sender = unwrapEvent(event)
    rasaJson = postRasaForIntent(payload)

    if rasaJson==appList[0]:
        callCatApp(payload)
    elif rasaJson==appList[1];
        print('implement notes app')
    elif rasaJson==appList[2];
        print('implement voicetunnel app')
    else:
        print('no app found')

    #return wrapIntentSpeakAction(rasaJson, sender)
