FROM python:3.8.6

WORKDIR /opt/otus-my-blog

COPY . /opt/otus-my-blog

RUN pip install -r requirements.txt

CMD ["/bin/bash"]
