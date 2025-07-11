# MCP Stdin Debug

A tool to debug MCP servers by piping stdin and stdout, while logging the entire session.

## Installation

To install the tool, clone the repository and then use `uvx` to install it in your environment:

```bash
git clone https://github.com/adrianlzt/mcp-stdin-debug.git
cd mcp-stdin-debug
uvx pip install -e .
```

## Usage

To use the tool, run it with the command of the MCP server you want to debug. For example:

```bash
mcp-stdin-debug your-mcp-server-command --with --args
```

Or, if you want to use `uvx` to run the `mcp-stdin-debug` command directly with another command, you can do:

```bash
uvx mcp-stdin-debug npx -y @modelcontextprotocol/server-everything
```

The tool will start the server and you will be able to interact with it through your terminal.

## Log File

All the communication between you and the server will be logged to a file named `mcp_session.log` in the directory where you run the tool.

## Example Traces

An example of a session log when connecting to `@modelcontextprotocol/server-everything` and listing the tools can be found [here](mcp_session-example.log).
