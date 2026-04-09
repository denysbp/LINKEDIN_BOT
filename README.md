# bot_linkedin

Projeto simples para buscar vagas no LinkedIn, filtrar e notificar por Telegram.

Instalação

1. Crie um virtualenv e ative-o (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

Configuração

- Crie um arquivo `.env` com as variáveis:

```
TELEGRAM_TOKEN=seu_token_aqui
CHAT_ID=seu_chat_id
```

- `KEYWORDS` e `LOCATION` podem ser customizados via variáveis de ambiente ou alterando `config.py`.

Inicializar DB

```bash
python -c "from database import init_db; init_db()"
```

Rodar aplicação web (simples):

```bash
python app.py
```

Rodar o bot como script:

```bash
python bot.py
```

Testes

```bash
python tests/test_parser_filters.py
```

Docker

```bash
docker-compose up --build
```

Para rodar apenas o web (Flask):

```bash
docker-compose up --build web
```

Observações

- `config.py` foi tornado tolerante à ausência de `python-dotenv` para facilitar execuções de teste rápidas.
- Para envio ao Telegram, chame `ensure_telegram_configured()` antes de usar notificadores para garantir que as variáveis estão definidas.
