import json

with open ('ExposureChecks-2020-12-03.json') as json_file:
    data = json.load(json_file)

    for info_check in data['ExposureChecks']:
        if info_check['MatchCount'] > 0:
            print("\nPositivo: ")
            print('Hash: ' + info_check['Hash'])
            print('RandomIDCount: ' + str(info_check['RandomIDCount']))
            print('DataSource" ' + info_check['DataSource'])
            print('Time: ' + info_check['Timestamp'])
            print('MatchCount: ' + str(info_check['MatchCount']))
        