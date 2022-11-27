FROM python:3.10-slim

ENV PROJECT_DIR "/app"
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY . $PROJECT_DIR

COPY ./requirements.txt $PROJECT_DIR/requirements.txt

RUN python -m pip install --upgrade pip  && \
    pip install --no-cache-dir -r $PROJECT_DIR/requirements.txt

COPY . $PROJECT_DIR

ENTRYPOINT ["python", "main.py"]
