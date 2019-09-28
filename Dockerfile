FROM python:3.7.3-stretch

ENV USR_LOCAL_BIN=/usr/local/bin  \
    PROJECT_ROOT=/application

ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

RUN pip install --upgrade pip

RUN mkdir $PROJECT_ROOT

WORKDIR $PROJECT_ROOT

COPY Pipfile $PROJECT_ROOT
COPY Pipfile.lock $PROJECT_ROOT

RUN pip install pipenv
RUN pipenv install --deploy --system

COPY src $PROJECT_ROOT

RUN ln -s $PROJECT_ROOT/start_server.sh $USR_LOCAL_BIN/start_server.sh \
    && sed -i 's/\r//' $USR_LOCAL_BIN/start_server.sh \
    && chmod +x $USR_LOCAL_BIN/start_server.sh

EXPOSE 80