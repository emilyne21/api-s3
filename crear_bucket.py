import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    try:

        nombre_bucket = event['body']['bucket']
        
        if not nombre_bucket:
            return {
                'statusCode': 400,
                'error': 'Falta el parametro "bucket" en el body'
            }

        s3.create_bucket(Bucket=nombre_bucket)
        
        return {
            'statusCode': 200,
            'mensaje': f'Bucket "{nombre_bucket}" creado exitosamente'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }