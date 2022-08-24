# start by pulling the python image
FROM python:3.10
# ENV PYTHONPATH "${PYTHONPATH}:/Users/michaeldawes/Documents/tldr/data"
RUN export PYTHONPATH="${PYTHONPATH}:/Users/michaeldawes/Documents/tldr/data"

# switch working directory
# WORKDIR /tldr
# COPY ./data ./data
# COPY ./server ./server

WORKDIR /tldr

# copy the requirements file into the image
COPY requirements.txt requirements.txt
COPY . ./
COPY ./server ./
COPY ./data ./

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 3600 server:app
ENTRYPOINT [ "python" ]

CMD python3 server.py
# CMD python3 tldr/server/server.py