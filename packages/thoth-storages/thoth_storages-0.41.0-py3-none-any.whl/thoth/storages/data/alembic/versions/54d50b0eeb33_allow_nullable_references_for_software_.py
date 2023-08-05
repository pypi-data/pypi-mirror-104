"""Allow nullable references for software environments

Revision ID: 54d50b0eeb33
Revises: e05d6d95ea95
Create Date: 2019-10-21 11:54:17.054303+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "54d50b0eeb33"
down_revision = "e05d6d95ea95"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("has_symbol_pkey", "has_symbol", type_="primary")
    op.create_primary_key(
        "has_symbol_pkey",
        "has_symbol",
        [
            "id",
        ],
    )
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("has_symbol", "external_software_environment_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column("has_symbol", "software_environment_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column("has_symbol", "versioned_symbol_id", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###


def downgrade():
    op.drop_constraint("has_symbol_pkey", "has_symbol", type_="primary")
    op.create_primary_key("has_symbol_pkey", "has_symbol", ["id", "software_environment_id"])
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("has_symbol", "versioned_symbol_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("has_symbol", "software_environment_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("has_symbol", "external_software_environment_id", existing_type=sa.INTEGER(), nullable=False)
    # ### end Alembic commands ###
