import requests

def conexion():

 url="https://oauth.battle.net/token"
 client_id="8c1a7edcacc64c30bf1b614b109a2742"
 client_secret="DxURRGvre4a0aDqFZbG5jqHNHpbTYT8s"
 data={'grant_type':'client_credentials'}
 x=requests.post(url,data,auth=(client_id,client_secret))

 lista=list(x.text)

 token_acceso=''.join(lista[17:51])
 token_tipo=''.join(lista[67:73])

 url="https://eu.api.blizzard.com/data/wow/token/index?namespace=dynamic-eu"

    
 x=requests.get(url,headers={"Authorization": f"Bearer {token_acceso}"})

 return(token_acceso,token_tipo)