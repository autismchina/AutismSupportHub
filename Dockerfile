FROM python:3.10.13-bookworm
ENV APP_DIR=/app

WORKDIR ${APP_DIR}
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501-9000
ENTRYPOINT [ "streamlit", "run"]