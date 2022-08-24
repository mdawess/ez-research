# start by pulling the python image
FROM python:3.10
WORKDIR /tldr

# copy the requirements file into the image
COPY requirements.txt requirements.txt
COPY . ./
COPY ./server ./
COPY ./data ./
COPY .env .env

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENV PYTHONPATH "${PYTHONPATH}:/Users/michaeldawes/Documents/tldr/data"
ENTRYPOINT [ "python" ]

CMD ["./server/server.py"]