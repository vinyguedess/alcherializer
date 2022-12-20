FROM python:3.7
LABEL DESCRIPTION "Base Python 3.7 development environment"

ENV DOT_ENV_PATH=/workspace/.env

# Define base folders
RUN mkdir /workspace /credentials /runtime
WORKDIR /workspace

# Entrypoint script
COPY entrypoint.sh /runtime/entrypoint.sh

# Prepare dev commands
COPY dev.sh /usr/local/bin/dev
RUN chmod +x /usr/local/bin/dev

RUN pip install --upgrade pip

ENTRYPOINT ["bash", "/runtime/entrypoint.sh"]