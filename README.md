# Login Application - Full Stack Project

A complete full-stack login application with a React frontend and Flask backend.

## Project Structure

```
learnwithabhi_1/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   └── index.html
│   └── package.json
├── .gitignore
└── README.md
```

## Backend Setup (Flask)

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

### Running the Backend

```bash
python app.py
```

The Flask server will start on `http://localhost:5000`

## Frontend Setup (React)

### Prerequisites
- Node.js (v14 or higher)
- npm (comes with Node.js)

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

### Running the Frontend

```bash
npm start
```

The React app will open in your browser at `http://localhost:3000`

## How to Use

1. **Start the Backend:**
   - Navigate to `backend/` folder
   - Activate virtual environment
   - Run `python app.py`

2. **Start the Frontend:**
   - In a new terminal, navigate to `frontend/` folder
   - Run `npm start`

3. **Login:**
   - Enter any username and password in the login form
   - Click the "Login" button
   - You'll see a success message if credentials are accepted

## Features

### Frontend
- ✅ Clean and responsive login form
- ✅ Username and password input fields
- ✅ Form validation
- ✅ Loading state during submission
- ✅ Error and success message display
- ✅ Modern gradient UI design
- ✅ Axios for HTTP requests

### Backend
- ✅ Flask REST API
- ✅ POST endpoint for login
- ✅ JSON request/response handling
- ✅ Environment variable configuration

## Technologies Used

### Backend
- **Flask** - Web framework for Python
- **Python-dotenv** - Environment variable management

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **CSS3** - Styling

## Next Steps to Enhance

1. **Add Database Integration:**
   - Add SQLAlchemy for database support
   - Create User model
   - Store and validate actual credentials

2. **Security Improvements:**
   - Hash passwords with bcrypt
   - Add JWT authentication
   - Implement rate limiting

3. **Frontend Enhancements:**
   - Add remember me functionality
   - Implement password reset
   - Add user registration page

4. **Testing:**
   - Add unit tests for backend
   - Add component tests for frontend
   - Add integration tests

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

**Author:** Anubhav Gulati  
**Date:** 2026-03-14 14:11:17