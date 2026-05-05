"""create user table

Revision ID: 8507cc7e552e
Revises: 933f37d9dd83
Create Date: 2026-05-05 13:12:54.973727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8507cc7e552e'
down_revision: Union[str, Sequence[str], None] = '933f37d9dd83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.add_column('posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'posts_owner_id_fkey',
        'posts', 'users',
        ['owner_id'], ['id'],
        ondelete='CASCADE'
    )

def downgrade() -> None:
    op.drop_constraint('posts_owner_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    op.drop_table('users')
