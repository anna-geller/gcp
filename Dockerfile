FROM prefecthq/prefect:2-python3.10
RUN pip install --trusted-host pypi.python.org --no-cache-dir gcsfs prefect-gcp Faker
EXPOSE 8080
COPY flows/ /opt/prefect/flows/
ENTRYPOINT ["prefect", "agent", "start", "-q", "default"]