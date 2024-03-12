import requests

url = "https://app.coalescesoftware.io/scheduler/startRun"

payload = {
    "runDetails": {
        "parallelism": 16,
        "environmentID": "116",
        "jobID": "27"
    },
    "userCredentials": {
        "snowflakeAuthType": "Basic",
        "snowflakeUsername": "MIPFlyingDoctorDemo",
        "snowflakePassword": "Welcome2Snowflake",
        "snowflakeWarehouse": "COMPUTE_WH",
        "snowflakeRole": "ACCOUNTADMIN"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer AMf-vBxiUfrAbbRvAl2SMA6U9JlO4SVqLrffxM_NvC_mPkFnOG8ix1gn0SQK91ns0whZodOTBRgzVQ59uidJTw9kDLYM9VooAKl7ba56jcnbhh-J0TKtdUdyc17uxOM93l_tXDA5ShAlKxrsXk_anJFY9anRTYmvunmdwjVPxyoZX2MUBZvH2BT2OIVzYdZRYi3hoTvobDeBjS7Gf3rY3zrs6v5cieIb-A"
}



response = requests.post(url, json=payload, headers=headers)

print(response.text)