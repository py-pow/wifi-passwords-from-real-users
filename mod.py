import requests
import json

def main():
    try:
        base_url = "https://www.wifimap.io/_next/data/SftcpLr_Sra_tj7N_Hxkg/en/map/"
        start_id = 1
        end_id = 7997
        uuids = []
        
        while start_id <= end_id:
            mod_url = f"{base_url}{start_id}.json"
            response = requests.get(mod_url)
            data = response.json()
            
            if response.status_code == 404:
                print(f"{start_id} : ait veri bulunamadı.")
            elif response.status_code == 200 and 'pageProps' in data and 'hotspotsList' in data['pageProps']:
                for hotspot in data['pageProps']['hotspotsList']['city']['hotspots']:
                    if 'uuid' in hotspot:
                        uuids.append(hotspot['uuid'])
                
                    else:
                        print(f"{start_id} : UUID bulunamadı.")
            
                print(f"{start_id} : UUID'ler başarıyla yazıldı.")
            elif 'hotspotsList' not in data['pageProps']:
                print(f"{start_id}: hotspotsList json argumanı bulunamadı.")
            else:
                print(f"{start_id}: Hata")
                
            start_id += 1
        
            with open("mod.json", "w") as json_file:
             json.dump(uuids, json_file, indent=4)
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Kullanıcı Tarafından Sonlandırıldı.")
