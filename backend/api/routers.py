from fastapi import APIRouter
from .endpoints import ComponentAPI, UserAPI, FeedbackAPI, ModuleAPI

router = APIRouter()
router.include_router(UserAPI.router, tags=["User API"])
router.include_router(ModuleAPI.router, tags=["Module API"])
router.include_router(FeedbackAPI.router, tags=["Feedback API"])
router.include_router(ComponentAPI.router, tags=["Component API"])
