FROM python:3.9.7
COPY . /flask
WORKDIR /flask
RUN pip install --default-timeout 1000 --retries 10 --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]