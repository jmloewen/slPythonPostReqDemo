import boto3
import json
lambda_client = boto3.client('lambda', region_name="us-east-1",)

FUNCTIONS_DICT = {
    "catApp": "aws-python-simple-http-endpoint-dev-CatAppOnStart"
}

def invokeLamba(functionName, payload):

    try:
        response = lambda_client.invoke(
            FunctionName=FUNCTIONS_DICT[functionName],
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )

        string_response = response["Payload"].read().decode('utf-8')
        parsed_response = json.loads(string_response)
    except Exception as e:
        print("invokeLamba error: ", e)
        parsed_response = {
            "InvokeLambaError": e
        }
    return parsed_response