"""create course table

Revision ID: 3d624a49ae9a
Revises: 7426b1956f84
Create Date: 2024-02-09 14:34:28.033669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d624a49ae9a'
down_revision: Union[str, None] = '7426b1956f84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        'course',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(20), nullable=False),
        sa.Column('city', sa.String(50), nullable=False),
        sa.Column('state', sa.String(50), nullable=False),
        sa.Column('par', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    pass
