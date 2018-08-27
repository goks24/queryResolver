import boto3
import DBUtil
import config as cfg

#AWS Lambda Function
def lambda_handler(event, context):
    # Connect to the database
    db = DBUtil.DBUtil()
    try:
        connection = db.initDB()
    except Exception as e:
        cfg.logger.error("Error in Database Connection")
        raise e
        result = {
                "message": "Error in Connecting to the Database"
        }
        return result

    #strore query based on the type (query/ref)
    query = ""

    # Get event data from json request
    type = event['type']
    command = event['command']


    #Check the type of input (query/ ref file)
    if type == 'query':
        query = event['value']
    else:
        REF_NAME = event['value']+".txt"

        # S3 client access
        s3 = boto3.client('s3')

        #retrive Object from S3
        obj = s3.get_object(Bucket=cfg.BUCKET_NAME, Key=REF_NAME)

        try:
            #Read S3 Object
            query = obj['Body'].read().decode('utf-8')
        except Exception as e:
            cfg.logger.error('Failed to get object from S3 (Please check reference file name): '+ str(e))
            return {
                "message": str(e)
            }


    if command == 'insert':
        # params for insert query
        param = event['args']
        #Getting table name
        TABLE_NAME = event['table']
        # insert Query to Database
        result= db.insertQuery(query,param,TABLE_NAME,connection)
    elif command == 'update':
        # params for insert query
        param = event['args']
        # insert Query to Database
        result= db.updateQuery(query,param,connection)
    else:
        # select Query to Database
        result= db.selectQuery(query,connection)

    return result
