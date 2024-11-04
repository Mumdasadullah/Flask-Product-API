from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Integer, 
    text,
    Text,
    Boolean,
    DateTime,
    Float,
    DECIMAL    
)
from core import database as db
from sqlalchemy.dialects.postgresql import UUID
import uuid



class Category(db.Model):
    __tablename__ = "category"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    slug = Column(String(length=50), nullable=False, unique=True)
    is_active = Column(Boolean(), default=False)
    
    parentId = Column(Integer(), ForeignKey("category.id"))
    
class SeasonalEvent(db.Model):
    __tablename__ = "seasonal_events"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    startDate = Column(DateTime())
    endDate = Column(DateTime())
    name = Column(String(length=100), unique=True)

class Product(db.Model):
    __tablename__ = "products"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    pid = Column(UUID(as_uuid=True), nullable=False, unique=True, server_default=text("uuid_generate_v4()"))
    name = Column(String(length=100), nullable=False, unique=True)
    slug = Column(String(length=50), nullable=False, unique=True)
    description = Column(Text)
    is_digital = Column(Boolean(), default=False)
    created_at = Column(DateTime(), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(), server_default=text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    is_active = Column(Boolean(), default=False)
    stock_status = Column(String(length=100), default="OUT_OF_STOCK")
    category_id = Column(Integer(), ForeignKey("category.id"))
    seasonal_event_id = Column(Integer(), ForeignKey("seasonal_events.id"), nullable=False)
    
class ProductLine(db.Model):
    __tablename__ = "product_lines"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    price = Column(DECIMAL(5, 2))
    sku = Column(UUID(as_uuid=True), default=uuid.uuid4)
    stock_qty = Column(Integer(), default=0)
    is_active = Column(Boolean(), default=False)
    order = Column(Integer())
    weight = Column(Float())
    created_at = Column(DateTime(), server_default=db.text("CURRENT_TIMESTAMP"))
    product_id = Column(Integer(), ForeignKey("products.id"))
    
class ProductImage(db.Model):
    __tablename__ = "product_images"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    alternative_text = Column(String(length=100))
    url = Column(String())
    order = Column(Integer())
    product_line_id = Column(Integer(), ForeignKey("product_lines.id"))

class Attribute(db.Model):
    __tablename__ = "attributes"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    description = Column(Text)
    
class AttributeValue(db.Model):
    __tablename__ = "attribute_values"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    attribute_value = Column(String(length=200))
    attribute_id = Column(Integer(), ForeignKey("attributes.id"))
    
class ProductType(db.Model):
    __tablename__ = "product_types"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=100))
    parent_id = Column(Integer(), ForeignKey("product_types.id"))
    
class Product_ProductType(db.Model):
    __tablename__ = "product_product_types"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    product_id = Column(Integer(), ForeignKey("products.id"))
    product_type_id = Column(Integer(), ForeignKey("product_types.id"))
    
class ProductLineAttributeValue(db.Model):
    __tablename__ = "product_line_attribute_values"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    attribute_value_id = Column(Integer(), ForeignKey("attribute_values.id"))
    product_line_id = Column(Integer(), ForeignKey("product_lines.id"))