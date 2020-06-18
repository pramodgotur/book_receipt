FROM python:3.7
WORKDIR /usr/src/app
COPY ./app .
COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD ["python","./main.py"]