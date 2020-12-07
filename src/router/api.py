from fastapi import APIRouter

router = APIRouter()

@router.post("/test")
def test():
    return "Clever Voca"
