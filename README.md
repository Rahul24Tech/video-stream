# Video Streaming Application using Django

This project is a video streaming application developed using Django framework. It allows users to sign up, create an account, manage their video content, and stream videos seamlessly. The application also provides RESTful APIs for various functionalities including authentication, video management, searching, and profile management.

## Requirements

- Python (>=3.6)
- Django (>=3.2)
- djangorestframework
- djangorestframework-simplejwt
- opencv-python

You can install the dependencies using the following command:

pip install -r requirements.txt


## Project Structure

video_streaming/
├── manage.py
├── video_streaming/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── videos/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
└── requirements.txt


## Getting Started

1. Clone the repository:

git clone <repository_url>
cd video_streaming


2. Install dependencies:

pip install -r requirements.txt


3. Apply database migrations:

python manage.py migrate


4. Create a superuser:

python manage.py createsuperuser


5. Run the development server:

python manage.py runserver


6. Access the application at http://localhost:8000/

## API Endpoints

- `/api/videos` - GET and POST endpoints for creating and retrieving videos.
- `/api/videos/<id>` - GET, PUT, and DELETE endpoints for retrieving, updating, and deleting a specific video.
- `/api/register` - POST endpoint for user registration.
- `/api/login` - POST endpoint for user login.

## Testing

You can run the tests using the following command:

python manage.py test


## Evaluation Criteria

1. Correctness: Ensure that the application meets the specified requirements.
2. Code Quality: Maintain well-structured and readable code.
3. Video Streaming: Verify that the site successfully streams videos using OpenCV with multithreading.
4. API Design: Ensure that the API is well-designed and easy to use.
5. Testing: Include enough tests to ensure the functionality of the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
