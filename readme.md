# Forex Data Graber .v1

This package was created to grab Forex data from multiple providers in order to authomated online trading by machine learning.

## Settings

this package needs a `setting.json` in the root folder.

```json
{
    "oanda":{
        "baseUrl":"<provider/api/base/url>",
        "apiKey":"bearer <accessToken>"
    }
}
```

## Initializing

For initializing `manage.db`, use `DB.py`.