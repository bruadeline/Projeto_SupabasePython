from supabase import create_client
import requests

url = "https://chlybsbaalwkpxkgputm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNobHlic2JhYWx3a3B4a2dwdXRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUwNDUwMjksImV4cCI6MjA3MDYyMTAyOX0.kjgpRbRUZ93RxISajxYyMP-1tgokPILQr-GPunR45xA"
supabase = create_client(url, key)

instance_id = "3E5AC49C59EE909FD4140E25EF347606"
token = "32D1FFC6023C70AE857F9844"

response = supabase.table("ListaContatos").select("*").execute()
contatos = response.data
print(contatos)

def enviar_mensagem(Celular, Nome):
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    payload = {
        "phone": Celular,
        "message": f"Olá {Nome}, tudo bem com você?"
    }
    r = requests.post(url, json=payload)
    print(Celular, r.status_code, r.text)

for contato in contatos:
    enviar_mensagem(contato["Celular"], contato["Nome"])




