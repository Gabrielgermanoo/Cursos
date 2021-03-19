"""empty message

Revision ID: 9051e98e1f68
Revises: 0b68e5d10617
Create Date: 2021-03-12 11:36:34.737121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9051e98e1f68'
down_revision = '0b68e5d10617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['user'])
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###