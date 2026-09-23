from fastapi import APIRouter

from . import analysis, experiments, health, mutations, orfs, sequences

router = APIRouter()
router.include_router(health.router)
router.include_router(sequences.router)
router.include_router(analysis.router)
router.include_router(mutations.router)
router.include_router(orfs.router)
router.include_router(experiments.router)
