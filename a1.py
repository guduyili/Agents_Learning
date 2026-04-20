# from hello_agents import SimpleAgent, HelloAgentsLLM
# from dotenv import load_dotenv 



# load_dotenv()

# llm = HelloAgentsLLM()



# agent = SimpleAgent(
#     name="AI助手",
#     llm=llm,
#     system_prompt="你是一个AI助手，你会根据用户的问题进行回答"
# )


# response = agent.run("你好，介绍一下你自己")
# print(response)


# #   添加工具功能
# from hello_agents.tools import CalculatorTool
# calculator = CalculatorTool()


# response = agent.run("帮我计算java中的integer的最大数值是多少，是2的几次方")
# print(response)


# print(f"历史消息数：{len(agent.get_history())}")


from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM

load_dotenv()

# 无需传入 provider，框架会自动检测
llm = HelloAgentsLLM() 
# 框架内部日志会显示检测到 provider 为 'ollama'

# 后续调用方式完全不变
messages = [{"role": "user", "content": "你好！"}]
for chunk in llm.think(messages):
    print(chunk, end="")
