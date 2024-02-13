"""create round table

Revision ID: 42daedc4a0e0
Revises: 3d624a49ae9a
Create Date: 2024-02-09 14:36:56.104400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42daedc4a0e0'
down_revision: Union[str, None] = '3d624a49ae9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'round',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(20), nullable=False),
        sa.Column('course_id', sa.String(50), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
    )

def downgrade() -> None:
    pass
