# Heartbreaker-Denouement (HTB - Sherlock) using ELK

This repository contains my script for parsing quickly the many Cloudtrail logs provided in the challenge [Heartbreaker-Denouement by HackTheBox](https://app.hackthebox.com/sherlocks/Heartbreaker-Denouement).

I'm using Elasticsearch and Python for its ease of use.  

It is made for linux (created on Ubuntu), **it shall not work on Windows**.

# Requirements

1. Docker, Docker engine
2. Python3, pip
3. Git

# Installation

### Setup 

1. Choose a working directory such as `/tmp/MySherlockFolder`.
2. `git clone https://github.com/septdney/htb-sherlock-heartbreaker-denouement.git`. 
3. `pip install elasticsearch`.
4. Unzip the file `HeartBreakerDenouement.zip` directly into your working directory, such as now such as `/tmp/MySherlockFolder/htb-sherlock-heartbreaker-denouement`.

### Tree

It should be looking like :

    .
    ├── directory-structure.md
    ├── docker-compose.yaml
    ├── HeartBreakerDenouement
    │   ├── AWS
    │   │   ├── af-south-1
    │   │   │   └── 2024
    │   │   │       └── 03
    │   │   │           ├── 12
    │   │   │           ├── 13
    │   │   │           └── 14
    │   │   ├── ap-northeast-1
    │   │   │   └── 2024
    │   │   │       └── 03
    │   │   │           ├── 12
    │   │   │           │   ├── 949622803460_CloudTrail_ap-northeast-.json.gz
    │   │   │           │   └── 949622803460_CloudTrail_ap-northeast-1_20240312T0035Z_A7YnwTNFdiLRloJ0.json.gz
    │   └── uac-uswebapp00-linux-20240313145552.tar.gz
        └── [... Many more files and folders ...]
    ├── Heartbreaker-Denouement.py
    ├── HeartBreakerDenouement.zip
    ├── kibana.yml
    └── README.md

### Launch

1. `$ cd /tmp/MySherlockFolder/htb-sherlock-heartbreaker-denouement`
2. `$ docker compose up -d`
3. `$ python3 Heartbreaker-Denouement.py $PWD` 
4. Go to http://localhost:5601