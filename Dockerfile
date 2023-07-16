FROM python:3.11

WORKDIR /code

COPY . /code/

# RUN make requirements
RUN pip install click Sphinx coverage flake8 python-dotenv dvc dvc-gdrive pytest fastapi uvicorn python-multipart numpy matplotlib Pillow tensorflow

# COPY ./src /code/src
# COPY ./api /code/api

EXPOSE 8000
CMD ["uvicorn",  "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
