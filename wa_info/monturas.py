from conexion import conexion
import requests


def monturas(personaje,servidor):
 token_acceso,token_tipo=conexion()
 url=f"https://eu.api.blizzard.com/profile/wow/character/{servidor}/{personaje}/collections/mounts?namespace=profile-eu"
 
 respuesta=requests.get(url,headers={"Authorization": f"Bearer {token_acceso}"})
 
 print(respuesta.json)