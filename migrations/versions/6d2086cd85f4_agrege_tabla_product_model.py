"""agrege tabla product_model

Revision ID: 6d2086cd85f4
Revises: 
Create Date: 2024-11-29 19:59:14.270692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d2086cd85f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto_model',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('precio', sa.Float(precision=2), nullable=False),
    sa.Column('serie', sa.Text(), nullable=False),
    sa.Column('disponible', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serie')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('producto_model')
    # ### end Alembic commands ###
