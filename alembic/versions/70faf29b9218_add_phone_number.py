"""add phone number

Revision ID: 70faf29b9218
Revises: e66e4863cb50
Create Date: 2023-02-26 12:23:13.442933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70faf29b9218'
down_revision = 'e66e4863cb50'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###