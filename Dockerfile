FROM python:3.9

WORKDIR /code

COPY . /code/

RUN make requirements

# COPY ./src /code/src
# COPY ./api /code/api

EXPOSE 8000
CMD ["uvicorn",  "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
