"""create_images_table

Revision ID: a65b02893e0d
Revises: bfc97be7e98f
Create Date: 2023-12-09 05:30:53.266199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = 'a65b02893e0d'
down_revision: Union[str, None] = 'bfc97be7e98f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'images',
        sa.Column('id', sa.Uuid(), server_default=text("gen_random_uuid()"), primary_key=True),
        sa.Column('user_id', sa.Uuid(), nullable=False, index=True),
        sa.Column('descriptor', JSONB()),
        sa.Column('hash', sa.String(), nullable=False, unique=True),
    )

    op.create_foreign_key(
        None,
        "images",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_table('images')
