"""create user table

Revision ID: 2940fbe6a9e8
Revises: 
Create Date: 2023-12-08 20:04:12.811816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2940fbe6a9e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(25), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('admin', sa.Boolean, server_default=sa.false(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')
