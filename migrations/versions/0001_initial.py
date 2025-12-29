from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "accounts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=False)
    )

    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("account_id", sa.Integer(), sa.ForeignKey("accounts.id")),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("description", sa.String()),
        sa.Column("timestamp", sa.DateTime())
    )


def downgrade():
    op.drop_table("transactions")
    op.drop_table("accounts")
