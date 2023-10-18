
![Logo](https://www.wifimap.io/_next/image?url=https%3A%2F%2Fblog.wifimap.io%2Fwp-content%2Fuploads%2F2019%2F06%2Fwfm.png&w=1920&q=75)

    
# wifimap.io API with wifi passwords from real users

wifimap.io API kullanarak gerçek kullanıcıların paylaştığı Wi-Fi şifrelerini elde etmek için yazdığım araç.



## Kütüphaneler 

Kullanılan Kütüphaneleri yükleyin.


```python 
$  pip install -r requirements.txt
$  pip install requests-toolbelt

```
    
## Kullanım
ilk önce uuids.py çalıştırıp uuidleri çekeceğiz , sonra çektiğimiz uudiler ile API istek yapıp uuidye ait parola var ise parolaları çekeceğiz.

```python
$ python3 uuids.py
$ python3 apisend.py

```

  
## Ekran Görüntüleri

![Ekran Görüntüsü (43)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/fd444654-60f5-4e7e-9591-d1aaf857c5b7)


