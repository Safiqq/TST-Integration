"""create livestock product  table

Revision ID: 8b5b09cce7ea
Revises: 2940fbe6a9e8
Create Date: 2023-12-08 20:08:10.848636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b5b09cce7ea'
down_revision: Union[str, None] = '2940fbe6a9e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'livestock_product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('livestock_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('product_id', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('livestock_product')
