"""add content to posts table

Revision ID: 96a92abb4c73
Revises: 9e90ff33385c
Create Date: 2024-11-26 22:41:34.319224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96a92abb4c73'
down_revision: Union[str, None] = '9e90ff33385c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable =  False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
