import json
import boto3

#Using boto3 to call the Comprehend API
client = boto3.client('comprehend')

#Lambda function to work with Comprehend
def lambda_handler(event, context):

    #Accessing data
    text = event['Body']

    #Sentiment Analysis
    sentiment = client.detect_sentiment(Text = text, LanguageCode = 'en') #API call for sentiment analysis
    sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
    sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative
    print(sentRes)
    print(sentScore)

    #Entity Extraction
    entities = client.detect_entities(Text = text, LanguageCode = 'en') #API call for entity extraction
    entities = entities['Entities'] #all entities
    print(entities)
    textEntities = [dict_item['Text'] for dict_item in entities] #the text that has been identified as entities
    typeEntities = [dict_item['Type'] for dict_item in entities] #the type of entity the text is
    print(textEntities)
    print(typeEntities)
    
    
    return {
        'statusCode': 200,
        'body': str(sentiment) + str(entities)
    }