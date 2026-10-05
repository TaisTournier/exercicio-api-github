import requests

API_USUARIOS = "https://api.github.com/users"
def buscar_usuarios(quantidade=10):
    try:
        resposta = requests.get(API_USUARIOS, params={"per_page": quantidade}, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return []
def exibir_usuarios(usuarios):
    print(f"{'Nº':<4}{'Login':<20}{'ID':<10}Perfil")
    print("-" * 70)
    for numero, usuario in enumerate(usuarios, start=1):
        login = usuario.get("login", "-")
        identificador = usuario.get("id", "-")
        perfil = usuario.get("html_url", "-")
        print(f"{numero:<4}{login:<20}{identificador:<10}{perfil}")
if __name__ == "__main__":
    lista = buscar_usuarios(15)
    exibir_usuarios(lista)
    print(f"\nTotal de usuários listados: {len(lista)}")
