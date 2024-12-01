FROM python:3.12.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY .. /usr/src/app

CMD [ "uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]

