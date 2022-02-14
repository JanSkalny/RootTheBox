"""custom fields

Revision ID: 3e320db59081
Revises: cd4d09aa9c68
Create Date: 2022-02-14 15:03:05.546142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e320db59081'
down_revision = 'cd4d09aa9c68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column("profession", sa.String(128), nullable=True))
    op.add_column('user', sa.Column("gender", sa.String(128), nullable=True))
    op.add_column('user', sa.Column("communication_consent", sa.Boolean, nullable=True))
    op.add_column('user', sa.Column("public_consent", sa.Boolean, nullable=True))
    pass


def downgrade():
    op.drop_column('user', 'profession')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'communication_consent')
    op.drop_column('user', 'public_consent')
    pass
