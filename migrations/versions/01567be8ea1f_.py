"""empty message

Revision ID: 01567be8ea1f
Revises: 83d50ce73d2e
Create Date: 2017-02-21 00:13:43.802774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01567be8ea1f'
down_revision = '83d50ce73d2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
