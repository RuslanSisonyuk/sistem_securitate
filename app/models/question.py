from sqlmodel import Field, SQLModel

from app.core.models import BaseModel


class QuestionBase(SQLModel):
    question_content: str
    recommended_policy: str
    answer: bool


class Question(QuestionBase, BaseModel, table=True):
    pass
