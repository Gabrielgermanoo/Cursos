"""empty message

Revision ID: 2df32268d6e0
Revises: 9051e98e1f68
Create Date: 2021-03-12 11:50:42.024582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2df32268d6e0'
down_revision = '9051e98e1f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('user', sa.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###
