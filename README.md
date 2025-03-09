# ProBlog API - RESTful-API-for-Blog-Application

ProBlog API is a production-grade RESTful API backend designed to efficiently manage professional blogging platforms. It includes user management, dynamic content management, and robust commenting and moderation capabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Features](#features)
- [Environment Variables](#environment-variables)
- [Further Improvements](#further-improvements)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HassanNazmul/RESTful-API-for-Blog-Application.git
    cd RESTful-API-for-Blog-Application
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```sh
    cp .env.example .env
    # Edit the .env file to include your own settings
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

To use the API, you can use tools like `curl`, `Postman`, or any HTTP client to interact with the endpoints.

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Obtain JWT token
- `POST /api/auth/logout/` - Logout user
- `POST /api/auth/password-reset/` - Request password reset
- `POST /api/auth/password-reset-confirm/` - Confirm password reset

### User Management

- `GET /api/auth/users/me/` - Get current user profile
- `GET /api/auth/users/<id>/` - Get user details by ID

### Blog Post Management

- `GET /api/blog/posts/` - List all published posts
- `POST /api/blog/posts/` - Create a new post
- `GET /api/blog/posts/<slug>/` - Retrieve a post by slug
- `PUT /api/blog/posts/<slug>/` - Update a post by slug
- `DELETE /api/blog/posts/<slug>/` - Delete a post by slug

### Category Management

- `GET /api/blog/categories/` - List all categories
- `POST /api/blog/categories/` - Create a new category
- `GET /api/blog/categories/<slug>/` - Retrieve a category by slug
- `PUT /api/blog/categories/<slug>/` - Update a category by slug
- `DELETE /api/blog/categories/<slug>/` - Delete a category by slug

### Tag Management

- `GET /api/blog/tags/` - List all tags
- `POST /api/blog/tags/` - Create a new tag
- `GET /api/blog/tags/<slug>/` - Retrieve a tag by slug
- `PUT /api/blog/tags/<slug>/` - Update a tag by slug
- `DELETE /api/blog/tags/<slug>/` - Delete a tag by slug

## Features

- **User Authentication & Authorization**: JWT-based authentication, user registration, password reset, user roles & permissions.
- **Blog Post Management**: CRUD operations for posts, rich text support, image uploads, slug generation, post statuses, scheduled publishing.
- **Content Categorization & Tagging**: CRUD operations for categories and tags, many-to-many relationships between posts and tags.
- **Advanced Comment Management**: CRUD operations for comments, nested comments, moderation system, profanity filtering.
- **Analytics & Metrics**: Tracking post views, post analytics endpoint, integrating basic analytics tracking.
- **Rich Media Support**: Image & thumbnail upload, optional integration of cloud-based storage.
- **Pagination, Searching & Filtering**: DRF-based pagination, comprehensive search, filtering posts by author, date range, tags, status.
- **Notifications & Email Integration**: Notifications for new comments, posts, and subscription updates, email notifications for registered users.
- **Security & Deployment Considerations**: Environment variables handling, protection against common attacks, deploying the app using Docker & cloud platforms.

## Environment Variables

The following environment variables need to be set in the `.env` file:

- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `True` for development, `False` for production.
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts.

## Further Improvements

- Implement user email verification.
- Add support for scheduled publishing of posts.
- Integrate cloud-based storage for media files.
- Implement advanced analytics and reporting features.
- Add support for notifications and email integration.