import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    try:
        nombre_bucket = event['body']['bucket']
        ruta_archivo = event['body']['ruta_archivo'] 
        contenido_base64 = event['body']['contenido_base64']
        
        if not all([nombre_bucket, ruta_archivo, contenido_base64]):
            return {
                'statusCode': 400,
                'error': 'Faltan parametros "bucket", "ruta_archivo" o "contenido_base64" en el body'
            }
            
        try:
            contenido_bytes = base64.b64decode(contenido_base64)
        except Exception as e:
            return {
                'statusCode': 400,
                'error': f'Contenido_base64 no es valido: {str(e)}'
            }
            
        s3.put_object(Bucket=nombre_bucket, Key=ruta_archivo, Body=contenido_bytes)
        
        return {
            'statusCode': 200,
            'mensaje': f'Archivo "{ruta_archivo}" subido exitosamente a "{nombre_bucket}"'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }