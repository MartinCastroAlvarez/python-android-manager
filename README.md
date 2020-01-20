# Montevideo
Apptime Technical Challenge.

### Introduction
This repository contains a web application that provides the following capabilities:

- Allows clients to list APKs available.
- Allows clients to list available devices.
- Allows clients to install and execute an APK into a device.
- Allows clients to view the results of a single test.
- Only Android is supported.

This repository does *not* contain the following features:

- Artifacts (screenshots) are only available on the local file system. They are not served as media files over the network.
- Clients can not upload APKs. APKs have to be downloaded from an external repo (because it is just a demo). You can follow the instructions on the following section.
- No authentication or authorization is performed. Everything is public.
- No clustering or fault-tolerance strategy implemented. It's just a prototype.
- Basic form validation. User input is roughly validated.
- No external database. Everything is stored in the local file system.
- Devices can *not* be started or stopped using this app. You need to follow the instructions in the following section to set it up.

### Table of Contents

- [Adding APKs to the System](./apks/README.md)
- [Android Setup](./android/README.md)
- [How to test the app](./tests/README.md)
- [Installation & Setup](./app/README.md)
- [Challenge Scope](./SCOPE.md)
- [Improvements](./IMPROVEMENTS.md)
