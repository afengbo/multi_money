# 配置基本的python开发环境
# 注意：如果pip安装出现如certificate verify failed的错误，pip后加上 --trusted-host files.pythonhosted.org 试试

FROM python:alpine3.6
RUN apk add --no-cache gcc musl-dev
RUN apk add --no-cache libffi-dev && pip install ipython
# filter-class依赖环境
RUN apk add --no-cache openssl-dev  &&\
    pip install redis &&\
    pip install pymysql &&\
    pip install sqlalchemy &&\
    pip install six &&\
    pip install w3lib &&\
    pip install simhash &&\
    pip install requests

# 编译安装 confluent-kafka-python
RUN apk add --no-cache libc-dev pcre-dev zlib-dev jemalloc-dev &&\
    apk --update add git openssh && \
    apk --update --no-cache add bash &&\
    apk add --update --no-cache g++ &&\
    apk add --update --no-cache make &&\
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*
RUN git clone https://github.com/edenhill/librdkafka.git &&\
    cd librdkafka &&\
    ./configure &&\
    make &&\
    make install &&\
    pip install confluent-kafka

RUN pip install pika