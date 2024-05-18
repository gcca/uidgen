FROM python:3.12.3-alpine3.19 AS builder

RUN apk update && apk add g++ libffi-dev cmake make && pip install --no-cache-dir nanobind etcd3
WORKDIR /gen
COPY /gen .
RUN cmake -DDISABLE_TESTS=ON . && make

FROM python:3.12.3-alpine3.19

RUN apk update && apk add libstdc++
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/
COPY --from=builder /gen/uidgen.*so /usr/local/lib/python3.12/site-packages/
RUN pip install --no-cache-dir fastapi
WORKDIR /app
RUN rm -fr /app/*
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
