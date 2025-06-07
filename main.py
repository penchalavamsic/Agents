from dotenv import load_dotenv
import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, FinalAnswerTool, Tool, tool, VisitWebpageTool

load_dotenv()
@tool
def suggest_menu(ocassion: str)->str:
    """"""
    Suggests a menu based on the occassion.
    Args: 
        occasion: The type of occasion for party.
    """"""
    if occasion=="casual":
        return "Pizza, snacks and drinks."
    elif ocassion=="formal":
        return"3-course dinner with wine"
    elif occasion=="superhero":
        return "Buffet with high energy"
    else:
        return " custom menu for butler"
@tool
def catering_service(query: str)->str:
    """"""
    this tool returns the highest-rated catering service in city.
    Args:
    query: A search term for finding the catering services.catering_service
    """"""
    service={
        "Gotham catering":4.9,
        "Wayne catering":4.8,
        "city events":4.5
    }
    best_service=max(service, key=service.get)
class Superhero(Tool):
        name="superhero party"
        description="This tool suggest the ceatuve superhero party ideas"
        inputs={
            "category":{
                "type":"string",
                "description":"the type of superhero"
            }
        }
        output_type="string"
        def forward(self, category:str):
            themes={
                "classic hero":"Justice league gala",
                "villan":"gotham rogues",
                "futuristic":"Neo-gotham"
            }
            return themes.get(category.lower())
        
agent=CodeAgent(
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebpageTool(),
        suggest_menu,
        catering_service,
        Superhero(),
        FinalAnswerTool()
    ],
    model=InferenceClientModel(),
    max_steps=10,

)
agent.run("give the best playlist for a party and idea is Villan theme")