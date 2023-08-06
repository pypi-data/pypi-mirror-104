![Hosting HQ Assets | TYPE: Banner | Format: PNG](https://hostinghq.xyz/assets/banner.png)
![Github Issues Sheid](https://img.shields.io/github/issues/Hosting-HQ/remotedb-py)  ![Last Commit](https://img.shields.io/github/last-commit/Hosting-HQ/remotedb-py) ![Github License Shield](https://img.shields.io/github/license/Hosting-HQ/remotedb-py)  ![PyPi Version](https://img.shields.io/pypi/v/remotedb) ![Python Version](https://img.shields.io/pypi/pyversions/remotedb)  ![Wheel?](https://img.shields.io/pypi/wheel/remotedb) ![Maintained?](https://img.shields.io/maintenance/yes/2021)  ![Size](https://img.shields.io/github/repo-size/Hosting-HQ/remotedb-py)
# RemoteDB
Hosting HQ RemoteDB is a service that provides Hosting HQ clients and non-clients a remote database solution to ease the burden of utilizing complex frameworks to manage their database.


## Prerequisites
- RemoteDB API Client ID (Check your Dashboard)
- RemoteDB API Token (Check your Dashboard)
- Validated RemoteDB License (Don't have one? Purchase one [here](https://members.hostinghq.xyz/index.php?rp=/store/remotedb))

## System Requirements
- Python 3.6 or Higher

## Usage
```python
from remotedb import Client
myRemoteDB = Client("client-id", "token")
```
### .set(key, value, [expire])
```python
# Select ONE of these methods
myRemoteDB.set("key", "value", "optional expire time in seconds") # Simplest
myRemoteDB["key"] = value # Set only a key and value
myRemoteDB["key"] = (value, "expire time in seconds") # Set a key, value and expire time
```
### .get(key)
```python
# Select ONE of these methods
myRemoteDB.get("key")
myRemoteDB["key"]
```
### .delete(key)
```python
Select ONE of these methods
myRemoteDB.delete("key")
del myRemoteDB["key"]
```
## Response Options
### .set(key, value, [expire])
```python
#getting value using key
s = myRemoteDB.set("key", "value", "expire") # Returns the default object
s.status # Returns the status code
s.message # Returns the response message
s.value # Returns the value field
s.key # Returns the key field
s.expire # Returns the expire field
s.raw # Returns the raw JSON response
```
### .get(key)
```python
#getting value using key
s = myRemoteDB.get("key") # Returns the default object
s.status # Returns the status code
s.message # Returns the response message
s.value # Returns the value field
s.key # Returns the key field
s.raw # Returns the raw JSON response
```
### .delete(key)
```python
#getting value using key
s = myRemoteDB.delete("key") # Returns the default object
s.status # Returns the status code
s.message # Returns the response message
s.key # Returns the key field
s.raw # Returns the raw JSON response
```
# Documentation
You can view our API documentation including API changelog at [https://docs.hostinghq.xyz/api](https://docs.hostinghq.xyz/api)
# Support
You can get support with RemoteDB and our packages in our Official [Discord Server](https://discord.gg/hostinghq)
# Contributing
Contribution to our packages is restricted to authorized contributors. If you believe a change needs to be made, open an [issue](https://github.com/Hosting-HQ/remotedb-py/issues) and we will review it.
# License
Hosting HQ RemoteDB Python Package is Licensed under GPL-3.0. The full license can be viewed [here](https://github.com/Hosting-HQ/remotedb-py/blob/main/LICENSE)
