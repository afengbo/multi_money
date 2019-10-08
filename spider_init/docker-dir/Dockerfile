FROM python:latest
# 安装支持http/https协议客户端请求的库
RUN pip install requests && \
    pip install aiohttp && \
    pip install tornado && \
    pip install selenium && \
    pip install appium-python-client

# 安装gcc编译环境
#RUN yum install gcc gcc-c++

# 下列模块的安装需要gcc编译环境
RUN pip install twisted && \
    pip install gevent

# 安装scrapy
#RUN yum install libffi-devel openssl-devel libxml2 libxslt-devel libxml2-devel python-devel && \
RUN pip install scrapy

# 安装pyspider
#RUN yum install curl libcurl4-openssl-dev libxml2-dev libxslt-dev zlib && \
RUN pip install pyspider

# 安装websocket-client
RUN pip install websocket_client

# 持久化存储
RUN pip install redis
RUN pip install pymysql
RUN pip install sqlalchemy

# simhash算法模块
RUN pip install simhash
