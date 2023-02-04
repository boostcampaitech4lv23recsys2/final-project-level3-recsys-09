"""empty message

Revision ID: ead8e87dcb7b
Revises: a8ced4675c21
Create Date: 2023-01-26 14:16:46.444050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ead8e87dcb7b'
down_revision = 'a8ced4675c21'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('required_ag', sa.String(), nullable=True))
    op.drop_column('game', 'required_age')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('required_age', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_column('game', 'required_ag')
    # ### end Alembic commands ###