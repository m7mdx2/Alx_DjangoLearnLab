# Authentication System Documentation

## 1. User Registration

**Process:**

- Users can register for a new account by filling out a registration form, which includes fields for username, password, and email.
- On form submission, the system creates a new user in the database.

**Implementation:**

- **View:** `register_view` (custom view)
- **Template:** `register.html` - Contains the registration form.
- **Form:** Uses a form based on `UserCreationForm`, extended to include an email field.
- **URL Pattern:** `/register/`

**Testing:**

1. Navigate to `/register/`.
2. Fill out the registration form and submit.
3. Verify that the new user is created and redirected appropriately.

## 2. User Login

**Process:**

- Users can log in using their username and password through a login form.
- Upon successful authentication, they are redirected to their profile or the homepage.

**Implementation:**

- **View:** `auth_views.LoginView` (Django's built-in view)
- **Template:** `login.html` - Contains the login form.
- **URL Pattern:** `/login/`

**Testing:**

1. Navigate to `/login/`.
2. Enter valid credentials to log in.
3. Verify that the user is redirected to the specified page.
4. Test with invalid credentials to ensure error handling.

## 3. User Logout

**Process:**

- Users can log out by clicking the logout link.
- The session is terminated, and the user is redirected to a specified page.

**Implementation:**

- **View:** `auth_views.LogoutView` (Django's built-in view)
- **URL Pattern:** `/logout/`

**Testing:**

1. While logged in, click the logout link.
2. Verify that the user is logged out and redirected.
3. Check that protected pages now redirect to the login page.

## 4. User Profile Management

**Process:**

- Authenticated users can view and edit their profile details.
- Users can update their email and other profile information.

**Implementation:**

- **View:** `profile_view` (custom view)
- **Template:** `profile.html` - Displays and allows editing of user information.
- **Form Handling:** The profile view handles POST requests to update user information.
- **URL Pattern:** `/profile/`

**Testing:**

1. Log in and navigate to `/profile/`.
2. Verify that user details are displayed.
3. Edit the profile information and submit.
4. Ensure the changes are saved and reflected in the user profile.

## 5. CSRF Protection

**Description:**

- All forms in the authentication system are protected against Cross-Site Request Forgery (CSRF) attacks using Django’s built-in CSRF protection.

**Implementation:**

- CSRF tokens are automatically included in forms via `{% csrf_token %}` in the templates.

**Testing:**

1. Inspect the HTML of the login, registration, and profile forms to ensure the presence of the CSRF token.
2. Attempt form submissions without the token (e.g., via a tool like Postman) to verify that the system rejects such requests.

## 6. Additional Security Measures

**Password Storage:**

- User passwords are hashed using Django's built-in hashing algorithms.

**Login Redirects:**

- Redirect URLs after login and logout are configured to enhance user experience and security.

**Session Management:**

- Sessions are managed to ensure users can log in on different devices securely.

## How to Test the Authentication System

**User Registration:**

1. Navigate to the registration page (`/register/`).
2. Submit a registration form with valid data.
3. Check that the new user is added to the database.

**User Login:**

1. Go to the login page (`/login/`).
2. Enter correct credentials to log in.
3. Ensure you are redirected to the profile or home page.
4. Try logging in with incorrect credentials to see the error handling.

**User Logout:**

1. After logging in, click the logout link.
2. Confirm that you are logged out and redirected.

**Profile Management:**

1. Log in and navigate to the profile page (`/profile/`).
2. Edit your profile information and save.
3. Verify that changes are updated in the user profile.

**CSRF Protection:**

1. Inspect forms for the presence of CSRF tokens.
2. Attempt to submit a form without a CSRF token to ensure it's blocked.
