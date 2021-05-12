FROM python:3.7-alpine

COPY mac.py .

ARG MACADDRESS_API_KEY
ENV MACADDRESS_API_KEY ${MACADDRESS_API_KEY}

RUN chmod +x ./mac.py && \
    pip3 install requests