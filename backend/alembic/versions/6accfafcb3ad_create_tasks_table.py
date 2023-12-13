"""create_tasks_table

Revision ID: 6accfafcb3ad
Revises: a65b02893e0d
Create Date: 2023-12-11 09:11:31.315247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '6accfafcb3ad'
down_revision: Union[str, None] = 'a65b02893e0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Uuid(), server_default=sa.text("gen_random_uuid()"), primary_key=True),
        sa.Column('user_id', sa.Uuid(), nullable=False, index=True),
        sa.Column('depends_on_id', sa.Uuid(), nullable=True, index=True),
        sa.Column('type', sa.Enum('UPLOAD', 'SEARCH', name='task_type'), nullable=False),
        sa.Column('status', sa.Enum('PENDING', 'RUNNING', 'FINISHED', name='task_status'), nullable=False),
        sa.Column('data', JSONB(), nullable=True),
        sa.Column('result', JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text("now()"), nullable=True)
    )

    op.create_foreign_key(
        None,
        "tasks",
        "users",
        ["user_id"],
        ["id"],
    )

    op.create_foreign_key(
        None,
        "tasks",
        "tasks",
        ["depends_on_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_table('tasks')
