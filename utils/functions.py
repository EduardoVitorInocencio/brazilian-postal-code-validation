import requests
import json
import glob

from time import sleep

# Function to seach by CEP with cache
def find_cep(cep, cache):
    if cep in cache:
        return cache[cep]
    
    else:
    # URL_VIA_CEP = f'https://viacep.com.br/ws/{cep}/json/'
        URL_VIA_CEP = f'https://opencep.com/v1/{cep}'
        try:
            answer = requests.get(URL_VIA_CEP, timeout=5)
            if answer.ok:
                address = answer.json()
                if "erro" in address:
                    cache[cep] = {
                        "cep":"",
                        "logradouro":"",
                        "complemento":"",
                        "bairro":"",
                        "localidade": "",
                        "uf":"",
                        "ibge":"",
                        "erro":"INVALID CEP",
                    }
                else:
                    cache[cep]={
                        "cep": address.get("cep",""),
                        "logradouro":address.get("logradouro",""),
                        "complemento":address.get("complemento",""),
                        "bairro":address.get("bairro",""),
                        "localidade":address.get("localidade",""),
                        "uf":address.get("uf",""),
                        "ibge":address.get("ibge",""),
                        "erro":"",
                    }
            else:
                cache[cep] = {
                        "cep":"",
                        "logradouro":"",
                        "complemento":"",
                        "bairro":"",
                        "localidade": "",
                        "uf":"",
                        "ibge":"",
                        "erro":f"Erro HTTP {answer.status_code}",
                    }
        except Exception as e:
            cache[cep] = {
                "cep":"",
                        "logradouro":"",
                        "complemento":"",
                        "bairro":"",
                        "localidade": "",
                        "uf":"",
                        "ibge":"",
                "erro": "Erro de conexão",
            }
        
        # Aguardar para evitar sobrecarregar a API
        return address
        sleep(0.4) #900 ms          

