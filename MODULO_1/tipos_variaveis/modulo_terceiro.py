print("\nImportaçao e uso de um modulo de terceiros")
import requests
url ="https://www.exemple.com"
response = requests.get(url)
print(f"Solicitaçao HTTP para {url} retornou o status {response.status_code}")