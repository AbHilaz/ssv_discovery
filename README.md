# SSV Discovery

A modern and elegant talent discovery platform that helps recruiters find students based on natural language queries and advanced filters. The platform connects recruiters with talented students and fresh graduates from SSV College.

## Features

- **Natural Language Search**: Find talent using conversational queries
- **Advanced Filtering**: Refine results by skills, experience level, and location
- **Student Profile Management**: Complete profile creation with skills, experience, and projects
- **Modern UI/UX**: Clean, responsive design optimized for all devices
- **Admin Dashboard**: Platform analytics and user management
- **Secure Authentication**: User-friendly registration and login process

## Technology Stack

- **Backend**: Django 5.0.2
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **NLP**: spaCy for natural language processing
- **Styling**: Bootstrap 5 with custom CSS

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- MySQL
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SSV_Discovery
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the spaCy model:
```bash
python -m spacy download en_core_web_sm
```

5. Configure MySQL:
   - Create a database named `ssv_discovery`
   - Create a `.env` file in the project root with the following content:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DB_NAME=ssv_discovery
   DB_USER=your-db-username
   DB_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=3306
   STATIC_URL=/static/
   STATIC_ROOT=staticfiles
   ```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Collect static files:
```bash
python manage.py collectstatic
```

9. Run the development server:
```bash
python manage.py runserver
```

### Accessing the Application

- **Main Application**: Visit http://127.0.0.1:8000/
- **Admin Interface**: Visit http://127.0.0.1:8000/admin

## Usage Guide

### For Recruiters

1. Visit the Discover page to search for talent
2. Use natural language queries like "Python developers with ML experience"
3. Apply filters to refine your search results
4. View student profiles and contact them directly

### For Students

1. Register for an account
2. Complete your profile with skills, experience, and projects
3. Upload your resume and profile picture
4. Your profile will be discoverable by recruiters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.