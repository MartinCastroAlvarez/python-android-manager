# Tests
This document contains the steps required to test the app.
It is assumed that the app has already been installed and started using [these](../app/README.md) instructions.
Also, at least one APK has been downloaded using [these](../apks/README.md) instructions.

## Unit Tests
This section describes the steps required to run unit tests.
```bash
export PYTHONPATH="$PYTHONPATH:$(pwd)"
nosetests \
    --cover-min-percentage 20 \
    --logging-level=DEBUG \
    -a "unit_test=true" \
    --with-coverage \
    --cover-erase \
    --detailed-errors \
    --cover-package ./app \
    ./tests
```
```bash
........................................................
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
app/__init__.py                      14      0   100%
app/api/__init__.py                  10      0   100%
app/api/applications.py              21      0   100%
app/api/constants.py                  6      0   100%
app/api/devices.py                   21      0   100%
app/api/tests.py                     14      0   100%
app/config.py                        15      0   100%
app/controllers/__init__.py           0      0   100%
app/controllers/applications.py      23      0   100%
app/controllers/devices.py           17      0   100%
app/controllers/tests.py             27      0   100%
app/exceptions/__init__.py           24      0   100%
app/exceptions/existence.py          10      0   100%
app/exceptions/form.py               10      0   100%
app/exceptions/runtime.py            16      0   100%
app/models/__init__.py                0      0   100%
app/models/application.py            62      0   100%
app/models/device.py                 72      0   100%
app/models/test.py                   47      0   100%
app/models/utils.py                  24     16    33%   20-32, 39-51
---------------------------------------------------------------
TOTAL                               433     16    96%
----------------------------------------------------------------------
Ran 56 tests in 0.100s

OK
```

## Functional Tests
This section describes the steps required to run functional tests.

##### Listing all existing applications.
```bash
curl -X GET "http://127.0.0.1:8004/v1/applications"
```
```bash
{
    "applications": [
        {
            "name": "com.calm.android_4.18.1-4120043_minAPI21(arm64-v8a,armeabi,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk",
            "type": "apk",
            "last_modified": 1579539347.8677053,
            "package": "com.calm.android",
            "id": "a18895ac8b9c209b57fcc43d4e38f1a9518f0f403822d46cbe0741d0eafcac39"
        },
        {
            "name": "com.ninegag.android.app_6.73.01r20914-e91fa2cc3a-6730100_minAPI21(arm64-v8a,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk",
            "type": "apk",
            "last_modified": 1579539347.8677053,
            "package": "com.ninegag.android.app",
            "id": "7123108cc19dcd079641b94d60a53afafb937dad63b62d06377fff7cee30fd87"
        },
        {
            "name": "com.instagram.android_126.0.0.0.20-193373619_minAPI23(arm64-v8a)(nodpi)_apkmirror.com.apk",
            "type": "apk",
            "last_modified": 1579539347.8677053,
            "package": "com.instagram.android",
            "id": "16eb95cb8af21a3fc77cccb28ae77c8d9ddab53bc1fbdeda0d7f6e2a617cd0d3"
        },
        {
            "name": "com.facebook.katana_255.0.0.0.86-193745403_minAPI26(arm64-v8a)(420,400,360,480dpi)_apkmirror.com.apk",
            "type": "apk",
            "last_modified": 1579539347.8677053,
            "package": "com.facebook.katana",
            "id": "a7711bb140d275dc24e3a5905c6fc871b8833b68d3f780ace7865c2779b5eccc"
        }
    ]
}
```

##### Getting application details by ID.
```bash
curl -X GET "http://127.0.0.1:8004/v1/applications/a7711bb140d275dc24e3a5905c6fc871b8833b68d3f780ace7865c2779b5eccc"
```
```bash
{
    "application": {
        "name": "com.facebook.katana_255.0.0.0.86-193745403_minAPI26(arm64-v8a)(420,400,360,480dpi)_apkmirror.com.apk",
        "type": "apk",
        "last_modified": 1579539347.8677053,
        "package": "com.facebook.katana",
        "id": "a7711bb140d275dc24e3a5905c6fc871b8833b68d3f780ace7865c2779b5eccc"
    }
}
```

##### Listing all devices available.
```bash
curl -X GET "http://127.0.0.1:8004/v1/devices"
```
```bash
{
    "devices": [
        {
            "name": "2960f439050ea6eb",
            "type": "usb:1-2",
            "model": "product:gts210vewifixx",
            "id": "4e0d1ce32cc4e7166fbf7c0880ecf8bdab63d7d1fe25ead8b0d395a00c8cde4e"
        },
        {
            "name": "emulator-5554",
            "type": "product:sdk_google_phone_x86",
            "model": "model:Android_SDK_built_for_x86",
            "id": "04ab3fc382bfb33ea4fbc120f5172ecfc4aed71652e00977064492ca0f65a017"
        }
    ]
}
```

##### Getting device details by ID.
```bash
curl -X GET "http://127.0.0.1:8004/v1/devices/4e0d1ce32cc4e7166fbf7c0880ecf8bdab63d7d1fe25ead8b0d395a00c8cde4e"
```
```bash
{
    "device": {
        "name": "emulator-5554",
        "type": "product:sdk_google_phone_x86",
        "model": "model:Android_SDK_built_for_x86",
        "id": "04ab3fc382bfb33ea4fbc120f5172ecfc4aed71652e00977064492ca0f65a017"
    }
}
```

##### Testing an application on a device.
```bash
curl --max-time 60 -X POST "http://127.0.0.1:8004/v1/devices/4e0d1ce32cc4e7166fbf7c0880ecf8bdab63d7d1fe25ead8b0d395a00c8cde4e/applications/16eb95cb8af21a3fc77cccb28ae77c8d9ddab53bc1fbdeda0d7f6e2a617cd0d3"
```
```bash
{
    "test": {
        "id": "4e0d1ce32cc4e7166fbf7c0880ecf8bdab63d7d1fe25ead8b0d395a00c8cde4e-16eb95cb8af21a3fc77cccb28ae77c8d9ddab53bc1fbdeda0d7f6e2a617cd0d3-1579562569.053885",
        "device": {
            "name": "2960f439050ea6eb",
            "type": "usb:1-2",
            "model": "product:gts210vewifixx",
            "id": "4e0d1ce32cc4e7166fbf7c0880ecf8bdab63d7d1fe25ead8b0d395a00c8cde4e"
        },
        "application": {
            "name": "com.instagram.android_126.0.0.0.20-193373619_minAPI23(arm64-v8a)(nodpi)_apkmirror.com.apk",
            "type": "apk",
            "last_modified": 1579539347.8677053,
            "package": "com.instagram.android",
            "id": "16eb95cb8af21a3fc77cccb28ae77c8d9ddab53bc1fbdeda0d7f6e2a617cd0d3"
        },
        "status": "success",
        "error": {},
        "ts": 1579562569.053885,
        "artifacts": [
            {
                "path": "/root/apptim/app/../artifacts/1579562569.053953.png"
            }
        ]
    }
}
```
