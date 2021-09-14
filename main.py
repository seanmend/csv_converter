import csv
import sys
import requests
import json


# pass csv when calling. ex:python3 main.py file.csv
def csv_converter(csv_path):
    print(csv_path)
    with open(csv_path, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # skip first invalid data
        iter_list = iter(csv_reader)
        next(iter_list)

        try:
            for row in iter_list:
                row_list = list(row.items())
                user_id = row_list[0][1]
                department_api_id = row_list[5][1]
                print('each provider:')
                print(user_id, 'and', department_api_id)

                try:
                    json_response = json.dumps({
                        "userOrg.integrations.advancedmd.department": department_api_id
                    })

                    r = requests.put(f'https://api.mendfamily.com/property/user/{user_id}', headers={
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'X-Access-Token': '{PROVIDER TOKEN}'
                    }, data=json_response)

                    print(r.apparent_encoding)
                    print(r.url)
                    print(r.headers)
                    print(r.content)

                except requests.exceptions.RequestException as err:
                    raise SystemExit(err)

        except LookupError as err:
            raise SystemExit(err)


if __name__ == '__main__':
    csv_path = sys.argv[1]
    csv_converter(csv_path)

