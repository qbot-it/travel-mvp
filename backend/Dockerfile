FROM python:3.10
WORKDIR /usr/src/app/update
RUN apt update && apt install build-essential
RUN pip install --root-user-action=ignore Cmake
RUN pip install --root-user-action=ignore torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --root-user-action=ignore transformers
RUN pip install --root-user-action=ignore gpt4all typer
RUN pip install --root-user-action=ignore open_clip_torch
