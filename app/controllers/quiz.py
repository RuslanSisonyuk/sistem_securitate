from typing import Annotated
#
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from app.repositories.question import QuestionRepository
from fastapi import APIRouter, Depends

from app.services.policies import PoliciesService

templates = Jinja2Templates(directory="app/templates/")
router = APIRouter()


@router.get("/")
async def root(request: Request, question_repository: Annotated[
    QuestionRepository, Depends(QuestionRepository)]) -> templates.TemplateResponse:
    questions = await question_repository.get_questions_content()

    return templates.TemplateResponse(
        request=request,
        name="pages/homepage.html", context={
            "questions": questions,
        }
    )


@router.post("/submit")
async def submit(
        request: Request, policies_service: Annotated[
            PoliciesService, Depends(PoliciesService)]
) -> templates.TemplateResponse:  # type: ignore

    answers = await request.form()
    result = await policies_service.get_policies(answers)

    return templates.TemplateResponse(
        request=request, name="pages/recommendations.html", context=result
    )
