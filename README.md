# Robot Framework test automation for Genderize API

## Robot Framework Setup:

### Pre-requisites:
1. Repository cloned to local machine
2. Python3 is installed (3.9 recommended)
3. virtualenv installed: pip install virtualenv

### Setup Virtual Environment

#### 1. Create virtual environment
Windows (PowerShell / Root):
```
.\create_virtual_env.bat
```

#### 2. Setup and start virtual environment

Script will automatically do the following:
 - Upgrade Python3 pip version to latest
 - Install required Python packages from requirements.txt
 - Install Playwright and required dependencies
 - Install latest pre-commit hooks to git

Windows (PowerShell / Root):
```
.\envrobot\Scripts\activate
```

```
.\start_installer.bat
```

Note: If above commands fail, you may to run following command
Windows (PowerShell / Root):
```
Set-ExecutionPolicy ByPass
```

### Executing tests
```
robot tests
```
