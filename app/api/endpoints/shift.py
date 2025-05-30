from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.schemas.shift import ShiftCreate, ShiftOut, ShiftUpdate
from app.crud import shift as crud_shift
from app.core.responses import response
from app.services.authentication import get_user_id_from_token

router = APIRouter(prefix='/shifts', tags=['shifts'])

@router.post("/", response_model=ShiftOut)
async def create_shift(shift: ShiftCreate, db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_token)):
    return crud_shift.create_shift(db, shift)

@router.get("/", response_model=list[ShiftOut])
async def read_shifts(db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_token)):
    shifts = crud_shift.get_shifts(db)
    return shifts

@router.get("/active-shifts/", response_model=list[ShiftOut])
async def read_active_shifts(db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_token)):
    shifts = crud_shift.get_active_shifts(db)
    return shifts

@router.get("/{shift_id}/", response_model=ShiftOut)
async def read_shift(shift_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_token)):
    shift = crud_shift.get_shift(db, UUID(shift_id))
    if not shift:
        return response("shift not found", 404, "error")
    return shift

@router.put("/{shift_id}/", response_model=ShiftOut)
async def update_shift(shift_id: str, shift_update: ShiftUpdate, db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_token)):
    shift = crud_shift.get_shift(db, UUID(shift_id))
    if not shift:
        return response("shift not found", 404, "error")
    shift = crud_shift.update_shift(db, shift, shift_update)
    return shift
