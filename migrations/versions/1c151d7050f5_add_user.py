"""add user

Revision ID: 1c151d7050f5
Revises: b86e6526fc48
Create Date: 2019-04-19 15:11:41.966095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c151d7050f5'
down_revision = 'b86e6526fc48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=128), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=True),
                    sa.Column('avatar', sa.String(length=200), nullable=True),
                    sa.Column('tokens', sa.Text(), nullable=True),
                    sa.Column('create_at', sa.DateTime(), nullable=True),
                    sa.Column('role', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
