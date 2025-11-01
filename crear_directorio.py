import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    try:
        nombre_bucket = event['body']['bucket']
        nombre_directorio = event['body']['directorio']
        
        if not nombre_bucket or not nombre_directorio:
            return {
                'statusCode': 400,
                'error': 'Faltan parametros "bucket" o "directorio" en el body'
            }
        
        if not nombre_directorio.endswith('/'):
            nombre_directorio += '/'
            
        s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio, Body='')
        
        return {
            'statusCode': 200,
            'mensaje': f'Directorio "{nombre_directorio}" creado en el bucket "{nombre_bucket}"'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }