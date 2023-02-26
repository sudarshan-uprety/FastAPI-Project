"""add content column to post table

Revision ID: c823a1320836
Revises: 3e5e637506e7
Create Date: 2023-02-26 08:59:41.251843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c823a1320836'
down_revision = '3e5e637506e7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
