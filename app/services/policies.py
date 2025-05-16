from typing import Annotated

from fastapi import Depends

from app.repositories.question import QuestionRepository


class PoliciesService:
    def __init__(self, question_repository: Annotated[QuestionRepository, Depends(QuestionRepository)]):
        self.question_repository = question_repository

    async def get_policies(self, answers: dict[str, str]) -> dict[str, any]:
        questions = await self.question_repository.get_questions_content()

        policies = []
        quiz_responses = {}
        for key in answers.keys():
            question_id, value = key.split("-")
            quiz_responses[int(question_id)] = value == "yes"

        for question in questions:
            if question.id not in quiz_responses.keys() or not quiz_responses[question.id]:
                policies.append(question.recommended_policy)

        return {
            "policies": policies,
            "percentage": 100 - 100 * len(policies) / len(questions)
        }
    #
