from faker import Faker
import platform
from prefect import flow, get_run_logger


@flow
def bs():
    logger = get_run_logger()
    fake = Faker()
    logger.info("We should %s 🚀", fake.bs())
    logger.info("Host's network name = %s", platform.node())


if __name__ == "__main__":
    bs()
