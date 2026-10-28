from pydantic import BaseModel , Field

class Answer(BaseModel):
    answer: str = Field(
        description="The answer needed for the user question"
    )
    context: str = Field(
        description="Context used by the agent to answer"
    )

