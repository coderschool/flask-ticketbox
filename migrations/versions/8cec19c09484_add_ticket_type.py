"""add ticket type

Revision ID: 8cec19c09484
Revises: 1c151d7050f5
Create Date: 2019-04-20 16:35:23.658739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8cec19c09484'
down_revision = '1c151d7050f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('event_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['event_id'], ['events.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('events', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.alter_column('events', 'description',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('events', 'name',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.create_foreign_key(None, 'events', 'user', ['owner_id'], ['id'])
    op.drop_column('events', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('price', sa.INTEGER(),
                                      autoincrement=False, nullable=True))
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.alter_column('events', 'name',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('events', 'description',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.drop_column('events', 'owner_id')
    op.drop_table('types')
    # ### end Alembic commands ###
