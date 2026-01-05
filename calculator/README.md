
#Info
https://github.com/modelcontextprotocol/python-sdk

Instalar UV

Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

agregar Path:

$env:Path = "C:\Users\\.local\bin;$env:Path"

validar con uv --version

uv init calculator

cd calculator

uv venv

iactivar el entorno con: .venv\Scripts\activate

una vez activado podremos recien agregar nuestro cliente MCP

uv add "mcp[cli]"


Se crea archivo server.py donde se definen las funciones o tools

se setea puertos sobre clientes $env:CLIENT_PORT="6286"; $env:SERVER_PORT="6297"

mcp dev server.py para interactuar con el cliente (MCP Inspector.)
