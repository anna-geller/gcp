# Prefect on GCP with serverless infrastructure on Google Cloud Run

The goal of this repository template is to make it easy for you to get started with Prefect on GCP. 

This repository template will help you to:
- create a Prefect agent running on serverless infrastructure
- create Prefect deployments for all flows in this repository
- set up a Continuous Deployment process with GitHub Actions 
- automate the process of building docker images and pushing those to the Google Artifact Registry

Ideally, you should be able to:

1. Clone this repository, or create your own repository from this template
2. Configure GitHub Actions secrets (Google Cloud Credentials and [Prefect Cloud v2](https://app.prefect.cloud/) API key)
3. Use [a bash script](agent.bash) to create all resources 


For more detailed usage of the Cloud Run Job infrastructure block, check out [this blog post](https://medium.com/the-prefect-blog/serverless-prefect-flows-with-google-cloud-run-jobs-23edbf371175).

## Questions?

If you have any questions or issue using this template, feel free to open a GitHub issues directly on this repo, or reach out via [Discourse](https://discourse.prefect.io/) or [Slack](https://prefect.io/slack)
