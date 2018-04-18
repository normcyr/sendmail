## Purpose

**sendmail** is a  Python script with config files to send emails. The ultimate objective of the project will be to automate certain emailing functions required in a day-to-day workflow.

## Requirements

- Python 3
- [PyYAML](https://pyyaml.org/)

## Usage

First, clone the repo from the command line interface.

```bash
git clone https://github.com/normcyr/sendmail.git
```

Rename the config and announcement text files to their proper names.

```bash
cd sendmail
mv config.yml.example config.yml
mv announcement.txt.example announcement.txt
```

Edit the config.yml file to suit your needs. You may want to use your email address for both `from_address` and `to_address` addresses in order to test it first.

```bash
nano config.yml
```

Edit the announcement.txt file to suit your needs. Replace the text for the message you want to send

```bash
nano announcement.txt
```

Finally, try the script!

```bash
python sendmail.py
```
