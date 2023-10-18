
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

![Tool Screenshot](https://private-user-images.githubusercontent.com/120333416/275463124-2fa268de-e998-4843-b843-18764f78f5f6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTc2MzczMDYsIm5iZiI6MTY5NzYzNzAwNiwicGF0aCI6Ii8xMjAzMzM0MTYvMjc1NDYzMTI0LTJmYTI2OGRlLWU5OTgtNDg0My1iODQzLTE4NzY0Zjc4ZjVmNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTAxOFQxMzUwMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MDQ3YTYwZGQ0YWU4ZDE3NzQ3ZDI5OTc0M2FmNmFjOTk3NjI2MWI3NTc2YTk5NTE5MDMyMjIyZDA1NjI1NzZhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.cAe3LK48ctp4ibhMqLf07caMUbBNJHWY_xZwamh3VqA)
![Tool Screenshot]()

![Tool Screenshot]()
  


  
 
![Ekran Görüntüsü (46)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/58f5ddb1-0d88-4578-8294-80a61c850b90)
![Ekran Görüntüsü (45)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/3fe41aee-695d-4226-a3cd-3d99bce2a1b4)
![Ekran Görüntüsü (44)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/337388ea-3ab4-4692-9fe9-d0b885869a15)
![Ekran Görüntüsü (43)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/2fa268de-e998-4843-b843-18764f78f5f6)
![Ekran Görüntüsü (42)](https://github.com/py-pow/wifi-passwords-from-real-users/assets/120333416/244d66a4-2364-4c9b-8e15-ab35258f4157)

