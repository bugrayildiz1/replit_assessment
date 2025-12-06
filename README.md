# XKCD Portal - Flask Web Application

A Flask web application that allows users to browse XKCD comics by entering a comic ID number. The application fetches comic data from the XKCD JSON API and displays the comic image, title, and alt text.

## Assessment Overview

This project was created as an assessment to demonstrate:
- Flask web application development
- Form handling and POST requests
- API integration with external services
- Error handling and user feedback
- HTML/CSS for user interface

### Requirements Met

✅ **Form Submission**: Users can submit an XKCD comic ID through a web form  
✅ **API Integration**: Fetches comic data from `https://xkcd.com/{id}/info.0.json`  
✅ **Success Handling**: Displays the comic image, title, and alt text when found  
✅ **Error Handling**: Shows an error message and fallback image when comic doesn't exist  
✅ **Flask Request Object**: Uses `request.form.get()` to retrieve form data  

## Features

- **Interactive Form**: Enter any XKCD comic ID (1-2752+) to view comics
- **Real-time Fetching**: Fetches comic data from the official XKCD JSON API
- **Error Handling**: Gracefully handles invalid IDs and network errors
- **Fallback Image**: Displays a random XKCD comic when requested comic is not found
- **Clean UI**: Modern, responsive design with styled interface
- **Comic Details**: Shows comic title, image, and alt text (hover text)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/bugrayildiz/Desktop/replit_assignment
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install Flask==2.3.3 requests==2.31.0
   ```

## Usage

### Starting the Application

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask application:**
   ```bash
   python main.py
   ```

3. **Open your web browser** and navigate to:
   ```
   http://localhost:8080
   ```
   or
   ```
   http://127.0.0.1:8080
   ```

### Using the Application

1. **Enter a Comic ID**: Type any XKCD comic ID number in the input field (e.g., 1, 100, 500, 936, 2000)

2. **Click "Get Comic"**: Submit the form to fetch and display the comic

3. **View the Comic**: The page will update with:
   - Comic title
   - Comic image
   - Alt text (hover text) displayed below the image

4. **Try Different IDs**: Enter different comic IDs to explore various XKCD comics

5. **Test Error Handling**: Try an invalid ID (e.g., 99999) to see the error message and fallback image

### Example Comic IDs to Try

- `1` - First XKCD comic
- `100` - Early XKCD comic
- `500` - Mid-range comic
- `936` - Password Strength (default)
- `2000` - Recent comic
- `99999` - Invalid ID (to test error handling)

## How It Works

### Application Flow

1. **Initial Load (GET request)**: 
   - User visits the homepage
   - Form is displayed with default ID (936)
   - No comic is shown initially

2. **Form Submission (POST request)**:
   - User enters a comic ID and clicks "Get Comic"
   - Flask receives the POST request
   - `request.form.get('comic_id')` retrieves the submitted ID

3. **API Request**:
   - Application constructs the API URL: `https://xkcd.com/{id}/info.0.json`
   - Sends HTTP GET request to XKCD API
   - Receives JSON response with comic metadata

4. **Response Handling**:
   - **Success (200)**: Parses JSON and displays comic data
   - **Error (404/other)**: Shows error message and fallback image

5. **Page Update**:
   - Jinja2 template renders the updated page
   - Comic image, title, and alt text are displayed
   - Form retains the submitted ID value

### Technical Details

- **Framework**: Flask 2.3.3
- **HTTP Client**: requests 2.31.0
- **Template Engine**: Jinja2 (built into Flask)
- **API Endpoint**: `https://xkcd.com/{id}/info.0.json`
- **Server**: Runs on `0.0.0.0:8080` (accessible from all network interfaces)

## Project Structure

```
replit_assignment/
├── main.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── venv/               # Virtual environment (created during setup)
```

## API Reference

### XKCD JSON API

The application uses the XKCD JSON API to fetch comic metadata:

**Endpoint**: `https://xkcd.com/{id}/info.0.json`

**Response Format** (example):
```json
{
  "month": "8",
  "num": 936,
  "link": "",
  "year": "2011",
  "news": "",
  "safe_title": "Password Strength",
  "transcript": "",
  "alt": "To anyone who understands information theory...",
  "img": "https://imgs.xkcd.com/comics/password_strength.png",
  "title": "Password Strength",
  "day": "10"
}
```

## Error Handling

The application handles several error scenarios:

1. **Invalid Comic ID**: Shows error message and fallback image
2. **Network Errors**: Catches `RequestException` and displays error message
3. **Missing Form Data**: Validates that comic ID is provided
4. **API Errors**: Handles non-200 HTTP status codes

## Testing

### Manual Testing

1. **Test Valid Comic**: Enter ID `936` and verify comic displays
2. **Test Invalid Comic**: Enter ID `99999` and verify error message appears
3. **Test Form Persistence**: Submit a form and verify ID remains in input field
4. **Test Network**: Disconnect internet and verify error handling

### Quick Test via Command Line

```bash
# Test GET request
curl http://localhost:8080

# Test POST request with valid ID
curl -X POST http://localhost:8080 -d "comic_id=936"

# Test POST request with invalid ID
curl -X POST http://localhost:8080 -d "comic_id=99999"
```



---

**Note**: The XKCD API is provided by XKCD (https://xkcd.com/). This application is for educational purposes only.

