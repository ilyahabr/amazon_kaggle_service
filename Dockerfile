FROM python:3.8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

WORKDIR /amazon_service

COPY . /amazon_service
RUN make install

RUN make download_weights

CMD make run_app
