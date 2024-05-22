FROM python:3.11
EXPOSE 8082
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8082", "--server.address=0.0.0.0" ]
