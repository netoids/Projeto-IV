import boto3

key_id = "ASIA4NFBRD5LL7TI335Y"
access_key = "Puk7GVKQOu0U6glhDY84YQh+oQVRJSFVpgsVYZuH"
token= "FwoGZXIvYXdzEHwaDA6hgQ+9V1XnQqYqdiLUAYTxpsvMbQdlm2Dcig8CzWBWp6FxXj8C+P7z7GbWGdp806r6r47VOUQYECZQVUhV7CS8I6Km7052iXbk+eW662XQJ6o04Sofc+GSnYSGQ+fVBfgUo9WlbloM1c7ueRuARzDFisQ521I/6ufdRhwVoBKq8UkErKjVfauYlKA2m0LMtWYY8Od9x8jhZSEaO6w+5hHJzSLcZZXOsNd+gqNiinBOexzFOiSrcAklDes8Hz4wujFEaIn1nHrArLrk3/Lvt+DOoCI38OxGK5Yzax6Q4cSwnUZnKIrwp40GMi32pe7q0Csoo52BHxr4JPN5K0ALYjX9AwIgh7YYBE3DYzbxwTa7bo/7EAwPyt4="

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
    response = pollyclient.synthesize_speech(
        OutputFormat='mp3',
        Text=textTranslated,
        VoiceId='Amy'
    )
    print(textTranslated)
    file = open("Audio.mp3", "wb")
    file.write(response['AudioStream'].read())
    file.close()
    s3client.upload_fileobj(response['AudioStream'], 'neto-bucket-projeto', 'texto-falado.mp3')
    return response['ResponseMetadata']['RequestId']


createBucket()
