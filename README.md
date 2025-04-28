# Instagram Media Downloader API

API para baixar posts do Instagram via URL ou shortcode e gerar um arquivo `.zip`.

## Requisitos

- Python 3.10+
- Git Bash / WSL / Terminal Bash
- Conta pública no Instagram (posts privados não são suportados)

## Setup

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/instagram-media-downloader.git
cd instagram-media-downloader
```

2. Crie o ambiente virtual:

```bash
python -m venv venv
source venv/Scripts/activate
```

3. Atualize o pip:

```bash
pip install --upgrade pip setuptools wheel
```

4. Instale as dependências:

```bash
pip install fastapi uvicorn instaloader
```

## Executando a API

```bash
python -m uvicorn main:app --reload
```

Acesse:

- Documentação Swagger: http://127.0.0.1:8000/docs

## Endpoints

`POST /download-instagram-post`
Descrição: Faz o download de um post do Instagram e gera um .zip.

Body Exemplo:

```json
{
  "url": "https://www.instagram.com/p/shortcode/"
}
```

Ou

```json
{
  "shortcode": "shortcode"
}
```

Resposta: Arquivo `.zip` com as mídias.

## Observações

- Funciona apenas para contas e posts públicos.
- Certifique-se de não violar os termos de uso do Instagram.
