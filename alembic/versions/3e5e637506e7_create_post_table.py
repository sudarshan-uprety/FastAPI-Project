"""create post table

Revision ID: 3e5e637506e7
Revises: 
Create Date: 2023-02-26 08:40:21.341355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e5e637506e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
