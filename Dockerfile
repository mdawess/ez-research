# start by pulling the python image
FROM python:3.10
WORKDIR /tldr

# copy the requirements file into the image
COPY requirements.txt requirements.txt
COPY . ./

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["./backend/server.py"]
