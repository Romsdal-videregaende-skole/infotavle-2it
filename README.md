# **infotavle-2it**
- En fullstack applikasjon som skal være en infotavle utviklet i skoleåret til 2-IT på Romsdal Videregående 

- [Backenden](https://github.com/Romsdal-videregaende-skole/infotavle-2it/tree/main/backend) er skrevet i Python med rammeverket [Flask](https://flask.palletsprojects.com/en/3.0.x/)

- [Frontend](https://github.com/Romsdal-videregaende-skole/infotavle-2it/tree/main/frontend) er skrevet i plain HTML, Css og Javascript


## Filstrukturen
- Frontend

- Backend


## **Installasjon av webserveren**
Først før vi kan gjøre noe som helst så må vi få tak i bibliotekene som kreves for webserveren
``` ps1
python -m venv .venv
```

### **Laging av Venv**
#### *Windows*

```sh
./.venv/Scripts/Activate.ps1
```

#### *Linux*

>`source ./.venv/Scripts/activate.sh`

## Installer webserveren
gå inn i backend folderen
```ps1 
python -m pip install -r requirements.txt
``` 
Alternativt for linux:
```ps1
python3 -m pip install -r requirements.txt
```
## Starting av webserveren
```
python backend/main.py
```


## TODO
- [ ] Alternativ måte å hente ut visma data på
- [x] Skrive README.md fil
- [ ] Dokumentere kode
