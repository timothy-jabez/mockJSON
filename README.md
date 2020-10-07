# mockJSON
Basic python script to create a mock JSON array

#### This is the JSON object that is going to be mocked:
```
{
  "_index": "metric-samples_aankleshwaria",
  "_type": "_doc",
  "_id": "aankleshwaria|viptela-collector-arjun|state|2020-08-18T12:09:02.308969Z|1.1.1.2|2",
  "_version": 1,
  "_score": null,
  "_source": {
    "tenantId": "aankleshwaria",
    "sourceId": "viptela-collector-arjun",
    "sourceType": "viptela-collector",
    "statistic": "raw",
    "metricId": "state",
    "metricName": "Device State",
    "units": "number",
    "durationMs": 0,
    "datetime": "2020-08-18T12:09:02.308969Z",
    "datetimeReceived": "2020-08-18T12:10:19.757Z",
    "datetimeProcessed": "2020-08-18T12:10:20.118Z",
    "datetimePublished": "2020-08-18T12:10:20.125Z",
    "value": "1",
    "device": {
      "id": "1.1.1.2",
      "name": "1.1.1.2",
      "type": "router",
      "vendor": "Cisco Systems",
      "ipAddresses": [
        "1.1.1.2"
      ],
      "location": {
        "lat": 37.666684,
        "lon": -122.777023
      },
      "countryCode": null,
      "countryName": null,
      "regionCode": null,
      "regionName": null,
      "city": null,
      "siteIds": [
        "4294953308"
      ],
      "interface": {
        "id": "2",
        "name": "system",
        "type": "loopback"
      }
    }
  },
  "fields": {
    "datetimeProcessed": [
      "2020-08-18T12:10:20.118Z"
    ],
    "datetime": [
      "2020-08-18T12:09:02.308Z"
    ],
    "datetimePublished": [
      "2020-08-18T12:10:20.125Z"
    ],
    "datetimeReceived": [
      "2020-08-18T12:10:19.757Z"
    ]
  },
  "sort": [
    1597752542308
  ]
}
```
