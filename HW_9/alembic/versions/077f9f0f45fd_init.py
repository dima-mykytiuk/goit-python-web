"""Init

Revision ID: 077f9f0f45fd
Revises: 
Create Date: 2022-04-05 16:21:31.422450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077f9f0f45fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('note_m2m_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note', sa.Integer(), nullable=True),
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note'], ['notes.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['notes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('note_m2m_tag')
    op.drop_table('tags')
    op.drop_table('notes')
    op.drop_table('contacts')
    # ### end Alembic commands ###