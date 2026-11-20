# Headless browser used for the end-to-end tests and the screenshots.
# Build:  docker build -t todo-list-shots tools/screenshots
FROM python:3.13-slim-bookworm
RUN pip install --no-cache-dir playwright==1.49.1 \
    && playwright install --with-deps chromium
WORKDIR /work
ENV PYTHONPATH=/work/src
ENTRYPOINT ["python", "/work/tools/screenshots/capture.py"]
