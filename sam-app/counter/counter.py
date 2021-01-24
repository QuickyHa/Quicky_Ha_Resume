import boto3

#create client and set table
client = boto3.resource('dynamodb')
table = client.Table('visitorcounter')

def lambda_handler(event,context):
    #atomic update/increment visitor counter
    response = table.update_item(
        Key = {'Visits':0},
        UpdateExpression = "ADD amount :inc",
        ExpressionAttributeValues = {':inc': 1},
        ReturnValues="UPDATED_NEW"
    )
    
    #extract count from response dict
    count = int(response['Attributes']['amount'])
    #create api response
    apiResponse = {
        "statusCode" :200,
        'headers': { "Access-Control-Allow-Origin": "*" },
        "body": count
    }
   
    return apiResponse