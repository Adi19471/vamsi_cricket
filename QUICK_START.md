# 🚀 Quick Start Guide - Cricket Slot Booking System

Follow these steps to set up and run the application on your local machine.

## Step-by-Step Installation

### Step 1: Open Terminal/Command Prompt
Navigate to the project directory:
```bash
cd cricket_booking
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Database & Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin/Superuser Account
```bash
python manage.py createsuperuser
```
Follow the prompts:
- Username: admin
- Email: admin@example.com
- Password: (enter your password)

### Step 6: Create Sample Cricket Slots
```bash
python manage.py create_sample_slots
```
This will create 30 days worth of cricket slots for testing.

### Step 7: Run Development Server
```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Accessing the Application

### Main Application
- **URL**: http://127.0.0.1:8000/
- **Features**: Register, Login, Book slots

### Admin Panel
- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin (or your superuser username)
- **Password**: (your superuser password)

## First Time Usage

### For New Users:
1. Go to http://127.0.0.1:8000/
2. Click "Register" and create a new account
3. Login with your credentials
4. You'll be redirected to Dashboard
5. Browse available cricket slots
6. Click "Book Now" on any slot
7. Confirm your booking
8. View your bookings in "My Bookings"

### For Admin:
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. You can:
   - Add/edit/delete cricket slots
   - View all user bookings
   - Cancel bookings
   - Manage users

## Database Schema

The application uses SQLite with two main tables:

**Slot Table:**
- id, date, time_slot, cricket_type, price, max_players, created_at, updated_at

**Booking Table:**
- id, user_id, slot_id, status, created_at, updated_at

**Unique Constraint:** A user cannot book the same slot twice

## Common Commands

### Stop the Server
Press `CTRL + C` in terminal

### Access Python Shell
```bash
python manage.py shell
```

### Create New Admin User
```bash
python manage.py createsuperuser
```

### Reset Database (⚠️ Deletes all data)
```bash
python manage.py migrate zero slots
python manage.py migrate
```

### Deactivate Virtual Environment
```bash
deactivate
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'django'"
**Solution**: Make sure virtual environment is activated and requirements are installed
```bash
pip install -r requirements.txt
```

### Error: "No such table: slots_slot"
**Solution**: Apply migrations
```bash
python manage.py migrate
```

### Port 8000 Already in Use
**Solution**: Use a different port
```bash
python manage.py runserver 8001
```

### Can't Access Admin Panel
**Solution**: 
1. Make sure you created a superuser
2. Use correct admin URL: http://127.0.0.1:8000/admin/

## Project Features Checklist

✅ User Registration & Login
✅ Dashboard with slot filtering
✅ Slot booking with duplicate prevention
✅ Booking management (view, cancel)
✅ Booking history
✅ Admin panel
✅ Bootstrap 5 responsive UI
✅ CSRF protection
✅ Django messages framework
✅ SQLite database
✅ Sample data generation

## Next Steps

After setup, you can:
1. Add more cricket slots using admin panel
2. Create test bookings
3. Explore the admin features
4. Customize styling in `slots/static/css/style.css`
5. Modify fields or add new features

## Need Help?

- Check the README.md for detailed documentation
- Review code comments in views.py and models.py
- Check Django documentation: https://docs.djangoproject.com/

---

**Enjoy your Cricket Booking System! 🏏**
