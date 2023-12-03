FROM python:3.10-alpine3.18
WORKDIR /usr/src/app/update
RUN apk --no-cache --update add alpine-sdk
RUN pip install --root-user-action=ignore Cmake
RUN pip install --root-user-action=ignore torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --root-user-action=ignore gpt4all typer
RUN pip install --root-user-action=ignore open_clip_torch
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --root-user-action=ignore --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

CMD ["/bin/sh","-c",\
    "pip install --root-user-action=ignore --upgrade -r /usr/src/app/requirements.txt && \
    uvicorn app.main:app --host 0.0.0.0 --port $BACKEND_PORT --reload"]
