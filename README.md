# University Management Project

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)

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

In your environment files:

```
./ontop_input/university-complete.compose.properties

./services/search/config.env

./.env

./docker-compose-service.yaml

./kong.yaml
```

Change the configuration's IP addresses into your local machine's IP address

## Usage

Start by running the following commands:

```bash
# Example command to run the project
docker compose -f docker-compose-3rd-party.yaml up -d

docker compose -f docker-compose-service.yaml up -d --build
```