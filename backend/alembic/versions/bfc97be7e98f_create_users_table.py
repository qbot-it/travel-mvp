"""create_user_table

Revision ID: bfc97be7e98f
Revises: 
Create Date: 2023-12-09 05:29:33.516896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text, insert
from passlib.hash import bcrypt

# revision identifiers, used by Alembic.
revision: str = 'bfc97be7e98f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table = op.create_table(
        'users',
        sa.Column('id', sa.Uuid(), server_default=text("gen_random_uuid()"), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
    )

    # test data
    stmt = (
        insert(table).
        values(email='test@test.com', password=bcrypt.hash('test'), name='John Connor')
    )

    op.execute(stmt)


def downgrade() -> None:
    op.drop_table('users')
