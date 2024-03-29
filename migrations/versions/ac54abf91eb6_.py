"""empty message

Revision ID: ac54abf91eb6
Revises: 1fb23dfc6934
Create Date: 2021-03-12 11:20:13.500654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac54abf91eb6'
down_revision = '1fb23dfc6934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'users', ['user'])
    op.drop_column('users', 'username')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('username', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'user')
    # ### end Alembic commands ###
