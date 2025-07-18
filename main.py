import json
import unittest
from datetime import datetime

# Load the JSON files
with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)

with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
    
    #Convert data from Format 1:
    #- Already has epoch timestamp
    #- Location is a string: country/city/area/factory/section
    #- operationStatus -> data.status
    #- temp -> data.temperature
    

    # Split the location string
    loc_parts = jsonObject['location'].split("/")
    location = {
        "country": loc_parts[0],
        "city": loc_parts[1],
        "area": loc_parts[2],
        "factory": loc_parts[3],
        "section": loc_parts[4]
    }

    # Build the final unified format
    result = {
        "deviceID": jsonObject['deviceID'],
        "deviceType": jsonObject['deviceType'],
        "timestamp": jsonObject['timestamp'],
        "location": location,
        "data": {
            "status": jsonObject['operationStatus'],
            "temperature": jsonObject['temp']
        }
    }

    return result


def convertFromFormat2(jsonObject):
    
    #Convert data from Format 2:
    #- device.id -> deviceID
    #- device.type -> deviceType
    #- timestamp is ISO -> convert to epoch ms
    #- location is separate fields -> pack into object
    #- data stays same but mapped to unified keys
    

    # Convert ISO timestamp to epoch milliseconds
    dt = datetime.strptime(jsonObject['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp_ms = int(dt.timestamp() * 1000)

    location = {
        "country": jsonObject['country'],
        "city": jsonObject['city'],
        "area": jsonObject['area'],
        "factory": jsonObject['factory'],
        "section": jsonObject['section']
    }

    result = {
        "deviceID": jsonObject['device']['id'],
        "deviceType": jsonObject['device']['type'],
        "timestamp": timestamp_ms,
        "location": location,
        "data": {
            "status": jsonObject['data']['status'],
            "temperature": jsonObject['data']['temperature']
        }
    }

    return result


def main(jsonObject):
    
   # Route to the correct converter.
   # If it has 'deviceID', it's Format 1.
   # Else it's Format 2.
    

    if 'deviceID' in jsonObject:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main()
