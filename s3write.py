import sys
import boto3
from datetime import datetime

def write_test_file(bucket, file):
    file_content = 'Hola, esto es un ejemplo de escritura en un bucket de S3 con Boto3.'
    s3 = boto3.client('s3',
                      aws_access_key_id=sys.argv[1],
                      aws_secret_access_key=sys.argv[2],
                      aws_session_token=sys.argv[3])
    s3.put_object(Body=file_content, Bucket=bucket, Key=file)
    print(f"[I] '{file}' loaded to bucket {bucket}")


if __name__ == "__main__":
    print("[I] Init process")
    write_date = str(datetime.now())
    bucket = 'glue-training-po'
    file = f's3-writer-tests/{write_date}-test.txt'
    write_test_file(bucket, file)

    print("[I] End process")