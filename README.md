# Netflix Clone

This project is a Netflix clone built using Django. It replicates core features of Netflix, including user authentication, content browsing, and video streaming.

## Features

- User authentication (sign up, login, logout)
- Browse and search for movies and TV shows
- Watch trailers and stream content
- Responsive design for desktop and mobile

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/netflix-clone.git
    cd netflix-clone
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, django templates
- **Database**: PostgreSQL




## Acknowledgments

- Inspired by Netflix's UI/UX design.
- Thanks to the Django community for their excellent documentation and support.
- Icons and images are for educational purposes only.