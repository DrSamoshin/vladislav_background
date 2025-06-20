import logging
from uuid import UUID
from sqlalchemy.orm import Session

from app.db.models import Supplier
from app.db.session import db_safe
from app.schemas.supplier import SupplierCreate, SupplierUpdate

@db_safe
def get_supplier(db: Session, supplier_id: UUID):
    logging.info(f"call method get_supplier")
    try:
        db_supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    except Exception as error:
        logging.error(error)
    else:
        logging.info(f"db_supplier: {db_supplier}")
        return db_supplier

@db_safe
def get_suppliers(db: Session):
    logging.info(f"call method get_suppliers")
    try:
        db_suppliers = db.query(Supplier).filter(Supplier.deactivated == False).all()
    except Exception as error:
        logging.error(error)
    else:
        logging.info(f"db_suppliers: {len(db_suppliers)}")
        return db_suppliers

@db_safe
def create_supplier(db: Session, supplier: SupplierCreate):
    logging.info(f"call method create_supplier")
    try:
        db_supplier = Supplier(name=supplier.name)
        db.add(db_supplier)
        db.commit()
        db.refresh(db_supplier)
    except Exception as error:
        logging.error(error)
    else:
        logging.info(f"db_supplier is created: {db_supplier}")
        return db_supplier

@db_safe
def update_supplier(db: Session, supplier_id: UUID, updates: SupplierUpdate):
    logging.info(f"call method update_supplier")
    try:
        db_supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
        for field, value in updates.model_dump(exclude_unset=True).items():
            setattr(db_supplier, field, value)
        db.commit()
        db.refresh(db_supplier)
    except Exception as error:
        logging.error(error)
    else:
        logging.info(f"db_supplier is updated: {db_supplier}")
        return db_supplier

