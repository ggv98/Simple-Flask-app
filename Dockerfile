FROM python:3.9.5
ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt;
CMD python app.py