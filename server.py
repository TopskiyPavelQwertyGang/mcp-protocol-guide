"""Minimal MCP server for the mcp-protocol-guide learning path."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "MCP Protocol Guide",
    instructions=(
        "Educational MCP server demonstrating one Tool, one Resource, "
        "and one Prompt. No shell access, database writes, or external API calls."
    ),
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.resource("package://{name}")
def package_info(name: str) -> str:
    """Return safe demo package information without accessing external systems."""
    return (
        f"Package: {name}\n"
        "Source: educational demo\n"
        "Status: no external lookup performed\n"
        "Next step: connect a trusted package or vulnerability data source."
    )


@mcp.prompt()
def analyze_package(name: str) -> str:
    """Create a reusable prompt for package-security analysis."""
    return (
        f"Analyze package '{name}'. "
        "Summarize known context, identify what additional vulnerability data is needed, "
        "and do not claim a CVE is applicable unless version evidence is available."
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
