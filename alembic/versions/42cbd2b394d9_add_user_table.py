"""add user table

Revision ID: 42cbd2b394d9
Revises: c823a1320836
Create Date: 2023-02-26 12:02:03.900419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42cbd2b394d9'
down_revision = 'c823a1320836'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass




def downgrade():
    op.drop_table('users')
    pass
