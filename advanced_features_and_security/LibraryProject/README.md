# LibraryProject

## Objective

The goal of this project is to gain familiarity with Django by setting up a Django development environment and creating a basic Django project. This project serves as the foundation for developing Django applications.

## Prerequisites

- Python installed on your system.
- Django installed via pip.

## Installation and Setup

### 1. Install Django

To install Django, run the following command in your terminal:

```bash
pip install django
```

# Permissions and Groups Setup

## Custom Permissions

Permissions have been added to the `Book` model:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups

Groups and their assigned permissions:

- **Editors:** `can_edit`, `can_create`
- **Viewers:** `can_view`
- **Admins:** `can_edit`, `can_create`, `can_view`, `can_delete`

## Views

- **View Book:** Requires `can_view` permission.
- **Create Book:** Requires `can_create` permission.
- **Edit Book:** Requires `can_edit` permission.
- **Delete Book:** Requires `can_delete` permission.
