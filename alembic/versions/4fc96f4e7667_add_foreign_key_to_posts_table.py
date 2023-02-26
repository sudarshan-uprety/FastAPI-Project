"""add foreign key to posts table

Revision ID: 4fc96f4e7667
Revises: 42cbd2b394d9
Create Date: 2023-02-26 12:06:50.552929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fc96f4e7667'
down_revision = '42cbd2b394d9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
