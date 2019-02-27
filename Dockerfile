FROM python:2.7
MAINTAINER Johannes le Roux <dade@dade.co.za>

COPY requirements.txt ./

RUN pip install --upgrade pip && pip --no-cache-dir -r requirements.txt

COPY ntlm-username-jsonp.py .

EXPOSE 8080

CMD ["python", "./ntlm-username-jsonp.py"]
