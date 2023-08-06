# QuickeySDK - Python

A Login Management System for Application

## How to Use

```
import quickey_python_sdk

```

### Get App Metadata - Access Token

```
app = App('your api Key')

appData = app.getAppMetaData()
print(appData.json())

accessToken = app.getAccessToken('your user email')
print(accessToken.json())

```

