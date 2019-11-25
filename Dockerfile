FROM python:3.6
LABEL maintainer="alan.p.bandeira@gmail.com"
WORKDIR /shipping_service
ADD . /shipping-service
RUN pip install poetry
RUN poetry install
CMD ["python", "src/run.py"]