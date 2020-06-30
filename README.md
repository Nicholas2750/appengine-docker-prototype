## Prototype of Simple Flask Server that Runs Docker

This is a quick prototype written to test whether AppEngine can run Docker containers or not.
This protoype works fine on cloudshell but fails on deployment to AppEngine, suggesting that AppEngine does not support Docker containers.


## Build Instruction (Requires Docker Installed)

```
pip3 install --user -r requirements.txt
```

## Run Instruction

```
python3 main.py
```

## Deployment Instruction
```
gcloud app deploy
```
