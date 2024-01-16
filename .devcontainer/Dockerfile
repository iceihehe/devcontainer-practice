FROM public.ecr.aws/docker/library/python:3.12

ARG CI_AUTH_TOKEN
ARG USERNAME=iceihehe
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ARG WORKSPACE=/opt/us-app

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    # [Optional]
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

COPY    requirements.txt ./
RUN     pip install --no-cache-dir -r requirements.txt && rm requirements.txt

EXPOSE  5000

# [Optional]
CMD ["./run.sh"]

