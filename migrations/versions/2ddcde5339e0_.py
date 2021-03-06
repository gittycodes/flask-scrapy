"""empty message

Revision ID: 2ddcde5339e0
Revises: 
Create Date: 2020-12-29 12:41:20.564493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ddcde5339e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('acquirers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('tax_id', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_acquirers')),
    sa.UniqueConstraint('name', name=op.f('uq_acquirers_name')),
    sa.UniqueConstraint('tax_id', name=op.f('uq_acquirers_tax_id'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles')),
    sa.UniqueConstraint('name', name=op.f('uq_roles_name'))
    )
    op.create_table('merchants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('mid', sa.String(), nullable=True),
    sa.Column('acquirer_id', sa.Integer(), nullable=True),
    sa.Column('requisites_ok', sa.Boolean(), nullable=True),
    sa.Column('threat_ok', sa.Boolean(), nullable=True),
    sa.Column('scan_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['acquirer_id'], ['acquirers.id'], name=op.f('fk_merchants_acquirer_id_acquirers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_merchants')),
    sa.UniqueConstraint('website', name=op.f('uq_merchants_website'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('acquirer_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['acquirer_id'], ['acquirers.id'], name=op.f('fk_users_acquirer_id_acquirers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('roles_users',
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('roles_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roles_id'], ['roles.id'], name=op.f('fk_roles_users_roles_id_roles')),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name=op.f('fk_roles_users_users_id_users'))
    )
    op.create_table('scans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('merchant_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('requisites', sa.JSON(), nullable=False),
    sa.Column('threat', sa.JSON(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['merchant_id'], ['merchants.id'], name=op.f('fk_scans_merchant_id_merchants')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_scans_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_scans'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scans')
    op.drop_table('roles_users')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    op.drop_table('merchants')
    op.drop_table('roles')
    op.drop_table('acquirers')
    # ### end Alembic commands ###
