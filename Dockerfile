FROM prefecthq/prefect:2-python3.10

COPY requirements.txt .
COPY setup.py .
COPY prefect_utils .

RUN pip install --upgrade pip --no-cache-dir
RUN pip install setuptools>=58.2.0 --no-cache-dir
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt
RUN pip install --trusted-host pypi.python.org --no-cache-dir .

ARG PREFECT_API_KEY
ENV PREFECT_API_KEY=$PREFECT_API_KEY

ARG PREFECT_API_URL
ENV PREFECT_API_URL=$PREFECT_API_URL

# log messages will immediately appear
ENV PYTHONUNBUFFERED True
COPY flows/ /opt/prefect/flows/

ENTRYPOINT ["prefect", "agent", "start", "-q", "default"]
