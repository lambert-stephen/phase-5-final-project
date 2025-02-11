"""edit password column in users

Revision ID: a3227727e7cc
Revises: f6bbfbc4ac60
Create Date: 2024-05-09 12:37:16.928051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3227727e7cc'
down_revision = 'f6bbfbc4ac60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.String(), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###
