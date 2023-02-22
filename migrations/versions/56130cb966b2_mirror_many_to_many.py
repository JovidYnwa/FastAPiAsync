"""mirror many to many

Revision ID: 56130cb966b2
Revises: c9080aa67289
Create Date: 2023-02-23 00:41:57.228431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56130cb966b2'
down_revision = 'c9080aa67289'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_books_reader_id', table_name='books')
    op.drop_constraint('books_reader_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'reader_id')
    op.add_column('readers_books', sa.Column('book_id', sa.Integer(), nullable=False))
    op.add_column('readers_books', sa.Column('reader_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'readers_books', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'readers_books', 'readers', ['reader_id'], ['id'])
    op.drop_column('readers_books', 'first_name')
    op.drop_column('readers_books', 'last_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('readers_books', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('readers_books', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'readers_books', type_='foreignkey')
    op.drop_constraint(None, 'readers_books', type_='foreignkey')
    op.drop_column('readers_books', 'reader_id')
    op.drop_column('readers_books', 'book_id')
    op.add_column('books', sa.Column('reader_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('books_reader_id_fkey', 'books', 'readers', ['reader_id'], ['id'])
    op.create_index('ix_books_reader_id', 'books', ['reader_id'], unique=False)
    # ### end Alembic commands ###
