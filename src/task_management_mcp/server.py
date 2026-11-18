
from mcp.server import MCPServer

# Create an MCP server instance
mcp = MCPServer("Task Management Server")


# Register our first MCP tool
@mcp.tool()
def create_task(title: str) -> str:
    """
    Create a new task.

    Args:
        title: The title of the task.
    """
    return f"Task created successfully: {title}"


if __name__ == "__main__":
    mcp.run()
