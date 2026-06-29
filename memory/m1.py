from dotenv import load_dotenv

load_dotenv()

from hello_agents import HelloAgentsLLM, SimpleAgent, ToolRegistry
from hello_agents.tools import RAGTool, MemoryTool

llm = HelloAgentsLLM(
    provider="auto",
    model="deepseek-v4-flash",  # 或 kimi-k2.6、glm-5.2 等
)


# 创建Agent
agent = SimpleAgent(
    name="智能助手",
    llm=llm,
    system_prompt="你是一个有记忆和知识检索能力的AI助手"
)


tool_registry = ToolRegistry()



memory_tool = MemoryTool(user_id="user_123")
tool_registry.register_tool(memory_tool)

# 创建RAG工具
rag_tool = RAGTool(knowledge_base_path="./knowledge_base")
tool_registry.register_tool(rag_tool)


agent.tool_registry = tool_registry


response = agent.run("你好，我想了解一下你能做什么？")
print("Agent Response:", response)