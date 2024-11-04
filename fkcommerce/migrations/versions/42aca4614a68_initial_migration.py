"""Initial Migration

Revision ID: 42aca4614a68
Revises: 
Create Date: 2024-11-03 12:25:57.742130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42aca4614a68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attributes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('parentId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parentId'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('product_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['product_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seasonal_events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=True),
    sa.Column('endDate', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('attribute_values',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('attribute_value', sa.String(length=200), nullable=True),
    sa.Column('attribute_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['attribute_id'], ['attributes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pid', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_digital', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('stock_status', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('seasonal_event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['seasonal_event_id'], ['seasonal_events.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('pid'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('product_lines',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('sku', sa.UUID(), nullable=True),
    sa.Column('stock_qty', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_product_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_images',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('alternative_text', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('product_line_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_line_id'], ['product_lines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_line_attribute_values',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('attribute_value_id', sa.Integer(), nullable=True),
    sa.Column('product_line_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['attribute_value_id'], ['attribute_values.id'], ),
    sa.ForeignKeyConstraint(['product_line_id'], ['product_lines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_line_attribute_values')
    op.drop_table('product_images')
    op.drop_table('product_product_types')
    op.drop_table('product_lines')
    op.drop_table('products')
    op.drop_table('attribute_values')
    op.drop_table('seasonal_events')
    op.drop_table('product_types')
    op.drop_table('category')
    op.drop_table('attributes')
    # ### end Alembic commands ###
