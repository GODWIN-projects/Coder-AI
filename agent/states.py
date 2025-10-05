from pydantic import BaseModel,Field, ConfigDict

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(description="The purpose of the file ")


class Plan(BaseModel):
    name: str = Field(description="The name of app to be built")
    description: str = Field(description="A oneline description of the app to be built")
    techstack: str = Field(description="The tech stack to be used for the app")
    features: list[str] = Field(description="A list of features that the app should have")
    files: list[File] = Field(description="A list of files to be created")