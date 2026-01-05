from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run()    