"""reviews table

Revision ID: 664063701f32
Revises: f8c34f879bab
Create Date: 2023-12-13 10:38:53.235649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664063701f32'
down_revision = 'f8c34f879bab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('customer_name', sa.String()),
        sa.Column('rating', sa.Integer()),
        sa.Column('comment', sa.String()),
      
    )

def downgrade() -> None:
    op.drop_table('reviews')
