# Installation
This document describes the steps required to install and run the app.

### Dependencies
This app is (currently) only supported by:

- [Red Hat 8](https://www.redhat.com/en/enterprise-linux-8).
- [Python 3.7.5](https://www.python.org/downloads/release/python-375/).

### Installation 
##### Install all Python OS dependencies:
```bash
sudo yum install python3 python3-pip python3-virtualenv
```
##### Download the app into your local host.
```bash
git clone ssh://git@github.com/MartinCastroAlvarez/montevideo
```
##### Install the Python dependencies.
```bash
cd apptim
virtualenv -p python3.7.5 .env
source .env/bin/activate
pip install -r requirements.txt
```
##### Follow [these](../android/README.md) instructions to setup the Android emulator.
##### Download APKs using [these](../apks/README.md) instructions.
##### Run the server.
```bash
export DEBUG="true"
export SECRET="my-secret"
export ANDROID_SDK_ROOT="$(pwd)/android/tools"
export ANDROID_HOME="${ANDROID_SDK_ROOT}"
export ANDROID_AVD_HOME="$(pwd)/android/platform-tools"
export ANDROID_AAPT_HOME="$(pwd)/android/build-tools/29.0.0"
python3 run.py 127.0.0.1 8004
```
