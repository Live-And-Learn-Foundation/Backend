# University Management Project

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)

## Installation

To start installation, download the project from GitHub

```bash
# Clone the repository
git clone https://github.com/Live-And-Learn-Foundation/Backend.git

# Navigate into the project directory
cd Backend
```

This project requires docker to be installed.

## Configuration

Copy oicd.key.sample into oicd.key

In your environment files:

```
./ontop_input/university-complete.compose.properties

./services/search/config.env

./.env

./docker-compose-service.yaml

./kong.yaml
```

Change the configuration's IP addresses into your local machine's IP address

Insert your openAI personal access token (PAT) (Preferably from github marketplace) or Azure production key(s)  into:
```
./services/search/keys.env
```

Learn more: [Prototyping with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models)

## Usage

Start by running the following commands:

```bash
# Example command to run the project
docker compose -f docker-compose-3rd-party.yaml up -d

docker compose -f docker-compose-service.yaml up -d --build
```
