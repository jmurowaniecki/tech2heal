FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY ./ /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]
