# 🏏 Cricket Slot Booking System

A complete Django web application for booking cricket slots with support for both Box Cricket and Normal Cricket.

## Features

### User Features
- **User Registration**: Create account with username, email, and password
- **User Authentication**: Secure login and logout functionality
- **Dashboard**: View available cricket slots filtered by type and date
- **Slot Booking**: Book available cricket slots with duplicate prevention
- **Booking Management**: View, manage, and cancel bookings
- **Booking History**: Complete record of all bookings (active and cancelled)

### Admin Features
- **Django Admin Panel**: Full admin interface to manage slots and bookings
- **Slot Management**: Add, edit, and delete cricket slots
- **Booking Management**: View all bookings, filter by status and date
- **Admin Actions**: Quick actions to mark bookings as confirmed or cancelled

### Technical Features
- Bootstrap 5 responsive UI
- CSRF Protection
- Django Messages Framework for notifications
- Role-based access control
- Data validation and error handling
- SQLite database
- Optimized database queries

## Project Structure

```
cricket_booking/
├── cricket_project/          # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL configuration
│   └── wsgi.py              # WSGI application
├── slots/                    # Main Django app
│   ├── migrations/          # Database migrations
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Custom Bootstrap 5 styles
│   │   └── js/
│   │       └── main.js      # Custom JavaScript
│   ├── templates/slots/     # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── home.html        # Home page
│   │   ├── register.html    # Registration
│   │   ├── login.html       # Login
│   │   ├── dashboard.html   # Main dashboard
│   │   ├── book_slot.html   # Booking confirmation
│   │   ├── my_bookings.html # User's bookings
│   │   └── booking_history.html  # Full history
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Django forms
│   ├── models.py            # Database models
│   ├── urls.py              # App URL configuration
│   └── views.py             # View logic
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── db.sqlite3              # SQLite database (generated)
```

## Database Models

### Slot Model
```
- date: Date field
- time_slot: Time period (6-7 AM, 7-8 AM, etc.)
- cricket_type: Box Cricket or Normal Cricket
- price: Price per slot
- max_players: Maximum number of players
- is_available: Property to check availability
```

### Booking Model
```
- user: Foreign key to Django User
- slot: Foreign key to Slot
- status: confirmed, pending, or cancelled
- unique_together: (user, slot) - prevents double booking
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 6. Add Sample Data (Optional)
Create a Django management command or use the admin panel to add cricket slots:

```bash
python manage.py shell
```

```python
from slots.models import Slot
from datetime import datetime, timedelta

# Add sample slots
today = datetime.now().date()
Slot.objects.create(
    date=today + timedelta(days=1),
    time_slot='6-7',
    cricket_type='box',
    price=500,
    max_players=11
)
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Access the application at: `http://127.0.0.1:8000/`

## Usage

### User Workflow
1. **Register**: Create a new account at `/register/`
2. **Login**: Login with credentials at `/login/`
3. **Browse Slots**: View available slots on dashboard
4. **Book Slot**: Select a slot and confirm booking
5. **Manage Bookings**: View and cancel bookings
6. **View History**: Check complete booking history

### Admin Workflow
1. **Access Admin Panel**: Go to `/admin/`
2. **Login**: Use superuser credentials
3. **Manage Slots**: Add, edit, delete cricket slots
4. **View Bookings**: See all user bookings
5. **Manage Bookings**: Update booking status or delete

## API/URLs

### Public URLs
- `/` - Home page
- `/register/` - User registration
- `/login/` - User login

### Protected URLs (Login Required)
- `/dashboard/` - View available slots
- `/book/<slot_id>/` - Book a slot
- `/my-bookings/` - View user's bookings
- `/cancel-booking/<booking_id>/` - Cancel a booking
- `/booking-history/` - Complete booking history
- `/logout/` - Logout

### Admin URLs
- `/admin/` - Django admin panel

## Security Features

1. **CSRF Protection**: All forms include CSRF tokens
2. **Password Hashing**: User passwords are hashed using Django's authentication system
3. **SQL Injection Prevention**: ORM prevents SQL injection
4. **Authentication Required**: Protected views require login
5. **Unique Constraints**: Database constraints prevent double booking
6. **Input Validation**: Form and model validation

## Styling

The project uses:
- **Bootstrap 5** for responsive grid and components
- **Font Awesome** for icons
- **Custom CSS** with gradient backgrounds and smooth transitions
- **Responsive Design**: Mobile-friendly layout

## Django Admin Customization

The admin panel includes:
- Custom list displays
- Filtering options
- Search functionality
- Read-only fields for timestamps
- Bulk actions for managing bookings
- Custom site header and branding

## Messages Framework

The app uses Django's messages framework for user feedback:
- **Success**: Booking confirmed, logout successful
- **Error**: Validation errors, booking conflicts
- **Warning**: Double booking attempts
- **Info**: General information

## Debugging Tips

### Enable Django Debug Toolbar
Add to `requirements.txt`:
```
django-debug-toolbar==4.1.0
```

Update `settings.py`:
```python
INSTALLED_APPS = [
    'debug_toolbar',
    ...
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

INTERNAL_IPS = ['127.0.0.1']
```

### Check Logs
Monitor the development server console for error messages and debugging information.

## Future Enhancements

- Payment integration (Razorpay, Stripe)
- Email notifications for bookings
- SMS alerts
- Advanced filtering and search
- User profile management
- Waitlist functionality
- Reviews and ratings
- API endpoints (DRF)

## Troubleshooting

### Issue: Database errors
**Solution**: Run migrations again
```bash
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic
```

### Issue: Can't login to admin
**Solution**: Create new superuser
```bash
python manage.py createsuperuser
```

## License

This project is open-source and available for educational purposes.

## Support

For issues and questions, please check the code comments and Django documentation at https://docs.djangoproject.com/

---

**Happy Cricket Booking! 🏏**
