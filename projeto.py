import boto3

key_id = "ASIA4NFBRD5LE74X4QQL"
access_key = "pSgbrzZN57RkwG5xJty6fZmLpGlXpNmBZyRMAZ4E"
token= "FwoGZXIvYXdzEID//////////wEaDPPjPLLztAvmp8gdBCLUAWgYbjQbUqw98Jly7fvt6y03z3aBeTjRvNKFF4rMzp0PPaIUAy4xpWDtaBCVae7vfxVPB5RSxJ0TLYXfoAWwstg9OtTzvgrFFuFDllOtbu0zBS9Cy6uOD/GueNeIqKjieXt6fdi/X5qOJY/NZF+80bUH4uKW7agUJKWszTkr0yqiA8fPmTHwxBfe7Qm7BCPl+kMQIGcoZtW9tox2du/hbOoU1XOkg43j20O/cyy+vEHZ3eGmPeywp4zVXn5KFdueUooJ4tJDDhIev1UvP7uyz0MEbRF4KP/gqI0GMi1aTjbxOaXh3I8okfswKTEfezW1PNtS8tCXc0E77cIcKxXAdLXFU0sMWOJxLFE="

s3client = boto3.client('s3', aws_access_key_id=key_id, aws_secret_access_key=access_key, region_name="us-east-1", aws_session_token=token)
pollyclient = boto3.client('polly', aws_access_key_id=key_id, aws_secret_access_key=access_key, region_name="us-east-1", aws_session_token=token)
translate_client = boto3.client('translate', aws_access_key_id=key_id, aws_secret_access_key=access_key, region_name="us-east-1", aws_session_token=token)

def createBucket():
    name = str("neto-bucket-projeto")
    response = s3client.create_bucket(Bucket=name)
    return response
    
def entrada(texto):
    entrada = texto
    textTranslated = translate_client.translate_text(Text=entrada,SourceLanguageCode="auto",TargetLanguageCode="en")["TranslatedText"]
    print(textTranslated)
    response = pollyclient.synthesize_speech(
        OutputFormat='mp3',
        Text=textTranslated,
        VoiceId='Amy'
    )
    response2 = pollyclient.synthesize_speech(
        OutputFormat='mp3',
        Text=textTranslated,
        VoiceId='Amy'
    )   

    file = open("Audio.mp3", "wb")    
    file.write(response['AudioStream'].read())    
    file.close()

    s3client.upload_fileobj(response2['AudioStream'], 'neto-bucket-projeto', 'polly-traduzido.mp3')  
    
    
    
    return response['ResponseMetadata']['RequestId']

def backup():
    response = s3client.get_object(Bucket='neto-bucket-projeto', Key='polly-traduzido.mp3')
    file = open("AudioBackup.mp3", "wb")
    file.write(response['Body'].read())
    file.close()
