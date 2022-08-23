# start by pulling the python image
FROM python:3.10

# switch working directory
# WORKDIR /tldr

# copy the requirements file into the image
COPY requirements.txt requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . ./

# configure the container to run in an executed manner
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 3600 server:app
ENTRYPOINT [ "python" ]

# May need to switch since server is in another file
WORKDIR /server

CMD ["server.py" ]