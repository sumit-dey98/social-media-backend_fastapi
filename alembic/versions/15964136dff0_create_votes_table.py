"""create votes table

Revision ID: 15964136dff0
Revises: 8507cc7e552e
Create Date: 2026-05-05 13:13:28.071439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15964136dff0'
down_revision: Union[str, Sequence[str], None] = '8507cc7e552e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'votes',
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('post_id', 'user_id'),
    )

def downgrade() -> None:
    op.drop_table('votes')
