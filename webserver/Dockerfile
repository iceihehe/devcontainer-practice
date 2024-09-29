FROM    public.ecr.aws/docker/library/python:3.9 AS base

WORKDIR /opt

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

####################################

FROM base AS develop

ARG USERNAME=devcontainer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    # [Optional]
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

####################################

FROM base

COPY gunicorn.conf.py ./

COPY app ./app

CMD [ "gunicorn" ]
