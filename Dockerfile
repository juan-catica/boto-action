FROM python:3.9.18

COPY ./s3write.py /opt/

RUN pip install boto3

ENTRYPOINT ["python", "/opt/s3write.py"]
   