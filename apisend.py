from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json

api_url = "https://api.wifimap.io/graphql_public_api"

transport = RequestsHTTPTransport(url=api_url, use_json=True)

client = Client(transport=transport, fetch_schema_from_transport=True)

with open("mod1.json", "r") as json_file:
    uuids = json.load(json_file)

query = gql("""
  query fetchHotspot($uuid: String) {
    hotspot(uuid: $uuid) {
      tips {
        password
      }
    }
  }
""")

with open("passwords.txt", "w") as pass_file:
    for uuid in uuids:
        variables = {
            "uuid": uuid
        }

        try:
            result = client.execute(query, variable_values=variables)

            tips = result['hotspot']['tips']
            password_found = False

            for index, tip in enumerate(tips):
                password = tip.get('password')
                if password:
                    password_found = True
                    pass_file.write(f"{password}\n")
                    print(f"UUID: {uuid}, Hotspot Şifresi bulundu | password:{index+1} -> {password} ")

            if not password_found:
                print(f"UUID: {uuid}, Hotspot Şifresi bulunamadı")

        except Exception as e:
            print(f"UUID: {uuid}, Hata oluştu: {e}")
        except KeyboardInterrupt:
            print(f"{uuid}'ne kadar tarandı.")
