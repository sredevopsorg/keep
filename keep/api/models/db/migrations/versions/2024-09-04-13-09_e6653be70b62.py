"""mapping type

Revision ID: e6653be70b62
Revises: 1a5eb7069f9a
Create Date: 2024-09-04 13:09:14.958740

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "e6653be70b62"
down_revision = "1a5eb7069f9a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("mappingrule", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("mappingrule", schema=None) as batch_op:
        batch_op.drop_column("type")
    # ### end Alembic commands ###
