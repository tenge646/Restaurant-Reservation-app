"""staffs table

Revision ID: f8c34f879bab
Revises: 
Create Date: 2023-12-13 10:38:03.714361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c34f879bab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'staffs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('day', sa.String()),
        sa.Column('chef', sa.String()),
        sa.Column('waiter', sa.String())
    )

def downgrade() -> None:
    op.drop_table('staffs')
