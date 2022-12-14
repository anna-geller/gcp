from prefect.filesystems import GitHub
from prefect_gcp.cloud_run import CloudRunJob
from prefect_gcp.credentials import GcpCredentials


block = CloudRunJob(
    image="us-east1-docker.pkg.dev/prefect-community/prefect/flows:latest",
    # image="us-east1-docker.pkg.dev/prefect-community/prefect/agent@sha256:8bc2bf01f28eff196a57903089a914693fd113ef53d8c3081a063c403c9eed74",
    region="us-east1",
    credentials=GcpCredentials.load("default"),
    cpu=1,
    timeout=3600,
)
block.save("default", overwrite=True)


gh = GitHub(
    repository="https://github.com/anna-geller/prefect-zoomcamp", reference="main"
)
gh.save("prefect-zoomcamp", overwrite=True)

gh = GitHub(repository="https://github.com/anna-geller/gcp", reference="main")
gh.save("gcp", overwrite=True)
