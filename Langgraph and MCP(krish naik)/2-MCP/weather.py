from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(city:str)->str:
    """This function get the weather of the city"""
    return f"The weather of city is sunny"


if __name__ == "__main__":
    mcp.run(transport="streamable-http",mount_path="/")

    