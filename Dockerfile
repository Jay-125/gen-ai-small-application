# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:20.04
ENV PYTHONUNBUFFERED=1
RUN useradd -ms /bin/bash appuser
USER appuser
WORKDIR /app
COPY --chown=appuser:appuser requirements.txt .
USER root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-pip python3-venv python3-tk \
        tzdata \
    && rm -rf /var/lib/apt/lists/*

USER appuser
RUN pip3 install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .
COPY --chown=appuser:appuser run_script.sh .
RUN chmod 777 run_script.sh
RUN chmod 777 /app/llm_code_to_check_description/main.py
RUN chmod 777 /app/run_app.py
CMD ["/app/run_script.sh"]