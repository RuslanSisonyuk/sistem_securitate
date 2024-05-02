from sqlmodel import select

from app.core.repository import Repository
from app.models.question import Question


class QuestionRepository(Repository):

    async def get_questions_content(self) -> list[Question]:
        statement = select(Question)
        result = await self._db_session.execute(statement)

        return result.scalars().all()
