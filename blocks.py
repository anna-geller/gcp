from prefect.filesystems import GitHub
from prefect_gcp.cloud_run import CloudRunJob
from prefect_gcp.credentials import GcpCredentials


block = CloudRunJob(
    image="us-east1-docker.pkg.dev/prefect-community/prefect/flows:latest",
    region="us-east1",
    credentials=GcpCredentials.load("default"),
    cpu=1,
    timeout=3600,
)
block.save("default", overwrite=True)


gh = GitHub(repository="https://github.com/anna-geller/gcp", reference="main")
gh.save("default", overwrite=True)
