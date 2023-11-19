FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "application.py", "--server.port=8080", "--server.address=0.0.0.0"]