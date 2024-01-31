## Setup Instruction
```
poetry init
poetry add pre-commit
poetry add pytest
```

### Setup Pre-Commit
Go check Pre-commit's website or yoink `.pre-commit-config.yaml` from here.

### Install Pre-commit
Enables pre-commit
```
poetry run pre-commit install
```

Manually run pre-commit
```
poetry run pre-commit run --all
```

### Set up SonarCloud
Go to SonarCloud, login then select your Repo. Follow their instruction.

## Run PyTest
```
poetry run pytest
```
