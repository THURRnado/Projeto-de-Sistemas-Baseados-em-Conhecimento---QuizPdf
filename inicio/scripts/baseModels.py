from pydantic import BaseModel
from typing import List

class Alternative(BaseModel):
    """Representa uma alternativa de uma questão."""
    text: str
    is_correct: bool
    explanation: str


class Question(BaseModel):
    """Representa uma questão com suas alternativas e explicação."""
    question_text: str
    alternatives: List[Alternative]


class QuestionSet(BaseModel):
    """Representa um conjunto de questões."""
    questions: List[Question]