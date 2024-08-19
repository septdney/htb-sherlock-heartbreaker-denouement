# Heartbreaker-Denouement (HTB - Sherlock) using ELK

This repository contains my script for parsing quickly the many Cloudtrail logs provided in the challenge [Heartbreaker-Denouement by HackTheBox](https://app.hackthebox.com/sherlocks/Heartbreaker-Denouement).

I'm using Elasticsearch and Python for its ease of use.  

# Requirements

1. Docker, docker engine
2. Python3
3. Git



# Installation

1. Choose a working directory such as <code>/tmp/MySherlockFolder</code>.
2. <code>git clone https://github.com/septdney/htb-sherlock-heartbreaker-denouement.git</code>. 
3. <code>pip install elasticsearch</code>.
4. unzip the file <code>HeartBreakerDenouement.zip</code> directly into your working directory, such as now such as <code>/tmp/MySherlockFolder/htb-sherlock-heartbreaker-denouement</code>.



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
    ├── Heartbreaker-Denouement.py
    ├── HeartBreakerDenouement.zip
    ├── kibana.yml
    └── README.md