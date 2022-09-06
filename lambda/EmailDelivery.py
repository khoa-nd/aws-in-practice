import os
import boto3
import botocore
import json

client = boto3.client('ses')

def lambda_handler(event, context):
    print(event)
    record = json.loads(event['Records'][0]['body'])
    
    try:
        email_message = {
            'Body': {
                'Text': {
                    'Data': record["message"],
                    'Charset': 'utf-8',
                }
            },
            'Subject': {
                'Charset': 'utf-8',
                'Data': record["subj"]
            },
        }
        
        ses_response = client.send_email(
            Destination={
                'ToAddresses': [record["to"]],
            },
            Message=email_message,
            Source="khoanguyen.robot@gmail.com"
        )
    
        print(f"ses response id received: {ses_response['MessageId']}.")

    except botocore.exceptions.ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(ses_response['MessageId'])

    return None