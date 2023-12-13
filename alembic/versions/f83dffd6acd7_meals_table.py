"""meals table

Revision ID: f83dffd6acd7
Revises: 664063701f32
Create Date: 2023-12-13 10:39:50.631916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f83dffd6acd7'
down_revision = '664063701f32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'meals',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('day', sa.String()),
        sa.Column('meals', sa.String()),
        sa.Column('drinks', sa.String())
    )

def downgrade() -> None:
    op.drop_table('meals')