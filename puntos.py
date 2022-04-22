import json
import random

def ganar(cantidad_buenas,nombre_guia):
    with open('usuario.json', 'r+') as f:
        data = json.load(f)
        
        adicion = cantidad_buenas/5
        if adicion <0.5:
            boost = random.randint(1,3)
        else:
            boost = random.randint(2,5)
        puntos_ganados = int(adicion*boost)
        if nombre_guia not in data["Guias terminadas"]:
            data['puntos'] += puntos_ganados
            data["Guias terminadas"].append(nombre_guia)
        else:
            print("Ya has ganado puntos en esta guia")
            
        f.seek(0)  # rewind
        json.dump(data, f)
        f.truncate()
        f.close()
        
        

        
def gastar(puntos_a_gastar):
    with open('usuario.json', 'r+') as f:
        data = json.load(f)
        if data['puntos'] < puntos_a_gastar:
           print("No tienes suficientes puntos")
        else:
            data['puntos'] -= puntos_a_gastar
            f.seek(0)  # rewind
            json.dump(data, f)
            f.truncate()
            f.close()
    
    
    


   