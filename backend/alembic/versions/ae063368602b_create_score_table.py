"""create score table

Revision ID: ae063368602b
Revises: 42daedc4a0e0
Create Date: 2024-02-09 14:39:35.791650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae063368602b'
down_revision: Union[str, None] = '42daedc4a0e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'score',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('round_id', sa.Integer, nullable=False),
        sa.Column('hole_number', sa.Integer, nullable=False),
        sa.Column('score', sa.Integer, nullable=False),
    )

def downgrade() -> None:
    pass
