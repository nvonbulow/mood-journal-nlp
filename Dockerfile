FROM python:3.10-alpine
WORKDIR /app


# Copy files to the container
# Install dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Download NLTK packages
RUN python3 -m nltk.downloader punkt vader_lexicon stopwords

# Copy server over
COPY Mood_Sentiment.py /app
COPY mood-journal-ui/out /app/out

ENV FLASK_APP=Mood_Sentiment.py
CMD python3 -m flask run --host=0.0.0.0 --port=$PORT