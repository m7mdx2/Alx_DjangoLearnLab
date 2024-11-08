# Advanced API Project

## API Endpoints

### Books

- **List Books**

  - `GET /books/`
  - Retrieve a list of all books.

- **Create Book**

  - `POST /books/`
  - Create a new book. Requires `title`, `publication_year`, and `author` in the request body.

- **Retrieve Book**

  - `GET /books/<int:pk>/`
  - Retrieve details of a specific book.

- **Update Book**

  - `PUT /books/<int:pk>/`
  - Update details of a specific book. Requires `title`, `publication_year`, and `author` in the request body.

- **Delete Book**
  - `DELETE /books/<int:pk>/`
  - Remove a specific book.

## Permissions

- **List and Create Books**: Public access.
- **Retrieve, Update, Delete Books**: Restricted to authenticated users.

## Customizations

- **Custom Validation**: Ensures that `publication_year` is not in the future.

# Filtering: Use query parameters like /books/?title=SomeTitle to filter by title

# Searching: Use /books/?search=SomeAuthor to search by title or author

# Ordering: Use /books/?ordering=publication_year to order by publication year (asc)

# To order by descending, prefix the field with "-", e.g., /books/?ordering=-publication_year
