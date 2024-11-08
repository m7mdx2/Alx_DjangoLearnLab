# Social Media API

This project is a Social Media API built using Django and Django REST Framework. It supports user registration, authentication, and profile management.

## Features

- User registration and login with token-based authentication.
- Custom user model with additional fields like `bio`, `profile_picture`, and `followers`.
- Token-based authentication using Django REST Framework’s Token Authentication.
- Post creation, editing, and deletion.
- User follow and feed functionality.
- Real-time notifications for user interactions (likes, follows, comments).

---

## Project Setup

### Prerequisites

- Django REST Framework
- Postman (for testing the API)
- Heroku (for deployment to production)

### Installation Steps

1. **Install the required packages**:

   ```
   pip install django djangorestframework
   django-admin startproject social_media_api
   python manage.py startapp accounts
   python manage.py startapp posts
   python manage.py startapp notifications
   ```

2. **Set up the Django project**:

   - Run migrations to set up the database:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

3. **Create a superuser** (for accessing the Django admin):

   ```
   python manage.py createsuperuser
   ```

4. **Start the development server**:
   ```
   python manage.py runserver
   ```

---

## User Authentication

The API uses token-based authentication to handle user login and registration. Below are the key endpoints to interact with the API.

### 1. **Register a New User**

- **Endpoint**: `/api/accounts/register/`
- **Method**: `POST`
- **Request Body**:

  ```json
  {
  	"username": "testuser",
  	"password": "testpassword123",
  	"email": "testuser@example.com",
  	"bio": "Just a test user"
  }
  ```

- **Response**:

  ```json
  {
  	"token": "<generated_token>"
  }
  ```

### 2. **User Login**

- **Endpoint**: `/api/accounts/login/`
- **Method**: `POST`
- **Request Body**:

  ```json
  {
  	"username": "testuser",
  	"password": "testpassword123"
  }
  ```

- **Response**:

  ```json
  {
  	"token": "<generated_token>"
  }
  ```

---

## User Model Overview

The custom user model extends Django’s `AbstractUser` to include additional fields for the social media functionality:

- **`bio`**: A brief description or biography of the user (TextField).
- **`profile_picture`**: An image field for uploading a profile picture.
- **`followers`**: A self-referential ManyToMany field to track followers. This field is non-symmetrical, meaning if User A follows User B, it doesn’t imply User B follows User A.

### Custom User Model Code:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
```

### AUTH_USER_MODEL

The `AUTH_USER_MODEL` setting in Django is configured to use the custom user model:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

---

## Testing the API

Use [Postman](https://www.postman.com/) or a similar API testing tool to test the API endpoints.

1. **Register a new user**:

   - Send a `POST` request to `/api/accounts/register/` with the user data.

2. **Login**:
   - Send a `POST` request to `/api/accounts/login/` with the username and password to retrieve an authentication token.

### Token Authentication

For requests that require authentication, include the token in the `Authorization` header:

```
Authorization: Token <your_token>
```

---

### Posts Functionality

The posts app allows users to create, edit, delete posts, and view feeds of posts from users they follow.

1. **Create a New Post**:
   **Endpoint**: `/api2/posts/create/`

   **Method**: `POST`

   **Request Body**:

   ```json
   {
   	"content": "This is my first post!",
   	"image": "optional_image_url"
   }
   ```

   **\*Response**:

   ```json
   {
   	"id": 1,
   	"content": "This is my first post!",
   	"image": "optional_image_url",
   	"author": "testuser",
   	"created_at": "2024-09-26T12:34:56Z"
   }
   ```

2. **View User Feed**

   **Endpoint**: `/api2/posts/feed/`
   **Method**: `GET`
   **Description**: `Displays posts from users the logged-in user follows, ordered by most recent.`

3. **Edit a Post**

   **Endpoint**: `/api2/posts/<post_id>/edit/`

   **Method**: `PATCH`

   **Request Body**:

   ```json
   {
   	"content": "Updated post content"
   }
   ```

   **Response**:

   ```json
   {
   	"id": 1,
   	"content": "Updated post content",
   	"image": "optional_image_url",
   	"author": "testuser",
   	"updated_at": "2024-09-26T12:40:00Z"
   }
   ```

4. **Delete a Post**

   **Endpoint**: `/api2/posts/<post_id>/delete/`
   **Method**: `DELETE`
   **Description**: `Deletes the specified post.`

### User Follows and Feed Functionality

1. **Follow a User:**
   URL: /accounts/follow/<user_id>/
   Method: POST
   Description: Follow a user by their ID.
2. **Unfollow a User:**
   URL: /accounts/unfollow/<user_id>/
   Method: POST
   Description: Unfollow a user by their ID.
3. **View User Feed:**
   URL: /posts/feed/
   Method: GET
   Description: View posts from users you follow, ordered by the most recent.

### Notifications Functionality

The notifications app tracks user interactions like follows, likes, and comments, and notifies users accordingly.

1. **Get All Notifications**

   **Endpoint**: `/api2/notifications/`
   **Method**: `GET`
   **Description**: `Returns a list of notifications for the logged-in user.`

   **Response**:

   ```json
   [
   	{
   		"id": 1,
   		"recipient": "testuser",
   		"message": "user1 liked your post.",
   		"timestamp": "2024-09-26T13:00:00Z",
   		"read": false
   	},
   	{
   		"id": 2,
   		"recipient": "testuser",
   		"message": "user2 followed you.",
   		"timestamp": "2024-09-26T13:05:00Z",
   		"read": false
   	}
   ]
   ```

2. **Mark Notification as Read**

   **Endpoint**: `/api2/notifications/<notification_id>/ read/`
   **Method**: `PATCH`

   **Description**: `Marks the specified notification as read.`

   **Response**:

   ```json
   {
   	"id": 1,
   	"recipient": "testuser",
   	"message": "user1 liked your post.",
   	"timestamp": "2024-09-26T13:00:00Z",
   	"read": true
   }
   ```
