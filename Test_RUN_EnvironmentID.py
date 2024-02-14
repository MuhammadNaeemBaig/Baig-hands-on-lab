import requests

url = "https://app.coalescesoftware.io/scheduler/startRun"

payload = {
    "runDetails": {
        "parallelism": 16,
        "environmentID": "111",
        "jobID": "27"
    },
    "userCredentials": {
        "snowflakeAuthType": "Basic",
        "snowflakeUsername": "Naeem",
        "snowflakePassword": "L@hore#570",
        "snowflakeWarehouse": "BAIG",
        "snowflakeRole": "ACCOUNTADMIN"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer AMf-vBy0hnGlgI5M4VO9eu1e6a3lBsOEUrqJjMhCLFHdySLs8PuaB3QzyInHlUEFTO5qjhTExbAY2W4I4rf6Y6ztdrg1lHU8Aj3hVtLXsc7k7DMpYXV2u3Spyey_8w2dd4aBqYocFGB3g-Cq_TbfDSNvUAJio0fq8V6M37Oz5k5_LEFr9-OlBVzhtPzefyP8Hsw4LgIiN5i3N8lEAGOfcuzNJiurhhqD8Q"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)