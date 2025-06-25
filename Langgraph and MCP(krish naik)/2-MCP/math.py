from mcp.server.fastmcp import FastMCP
mcp = FastMCP("math")

@mcp.tool()
def add(a:int,b:int):
    """This function add two no 
    args:
    a:int
    b:int
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """This function multiply two no """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")

    
#You're telling the MCP app to:
# Read requests from standard input (e.g., stdin)
# Write responses to standard output (e.g., stdout)