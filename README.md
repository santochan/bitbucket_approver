Bitbucket Approver

This is the Python implementation of bitbucket approver client.
The server is [here](https://github.com/beviz/bitbucket-auto-approve)

# Usage

## Installation

```bash
pip install bitucket_approver
```

## Config file

You need a `config.toml` file for configuration like below:

```toml
token = "YOUR TOKEN"
server = "Approver Server"
proxy = "socks5://localhost:1080"
```

## Start client

```bash

bitbucket_approver ~/config.toml

```


