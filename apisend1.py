from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json

# GraphQL API URL
api_url = "https://api.wifimap.io/graphql_public_api"

# Define your headers as a dictionary
headers = {
    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"  # Replace with your desired User-Agent header
}

# GraphQL API'ye HTTP isteği yapmak için bir taşıyıcı oluşturun
transport = RequestsHTTPTransport(url=api_url, headers=headers, use_json=True)

# Taşıyıcıyı kullanarak bir GraphQL istemcisi oluşturun
client = Client(transport=transport, fetch_schema_from_transport=True)

# JSON dosyasından UUID'leri yükleyin
with open("mod1.json", "r") as json_file:
    uuids = json.load(json_file)

# UUID için GraphQL sorgusu
query = gql("""
  query fetchHotspot($uuid: String) {
    hotspot(uuid: $uuid) {
      tips {
        password
      }
    }
  }
""")

# Dosyayı yazmak için wifimappass.list'i açın
with open("password.txt", "w") as pass_file:
    # Her UUID için döngü
    for uuid in uuids:
        # Sorgu değişkenlerini tanımlayın
        variables = {
            "uuid": uuid
        }

        try:
            # Sorguyu çalıştırın
            result = client.execute(query, variable_values=variables)

            # Şifreleri alın
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
