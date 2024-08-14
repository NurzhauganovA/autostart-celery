FROM python:3.11

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Almaty

WORKDIR /app

COPY backend/requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

COPY ./docker/dev/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]