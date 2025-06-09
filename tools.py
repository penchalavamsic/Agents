from smolagents import CodeAgent, InferenceClientModel, tool
@tool
def Catering_tool(query: str)->str:
    ""This tool gives the highest rating catering service""
    Args
    query:
            a search term for finding catering service
          """"""
    service={
      "gotham":5.0,
      "bruce":4.9
    }    
    best=max(service, key=service.get)
    return(best)
agent=CodeAgent(tools=[Catering_tool], model=InferenceClientModel())
result=agent.run("give higest rating catering service")
print(result)