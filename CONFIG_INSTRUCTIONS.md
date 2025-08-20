# 🚀 Agent2 Project - Complete Setup Instructions

This document provides comprehensive instructions for setting up and running the Agent2 project, which is an AI-powered e-commerce platform with a customer service chatbot built using Google's Agent Development Kit (ADK).

## 📋 Project Overview

**Agent2** is a complete e-commerce application featuring:

- **Flask Web Application** (main website) - Port 5000
- **FastAPI WebSocket Server** (AI chatbot backend) - Port 8001
- **Customer Service AI Agent** powered by Google Gemini via Vertex AI
- **Product Catalog** with search and recommendations
- **Shopping Cart** with real-time updates
- **Interactive Chatbot** for customer support

## 🛠️ System Requirements

### Prerequisites

- **Python 3.11+** (recommended)
- **Windows/macOS/Linux** (tested on Windows)
- **Google Cloud Account** (for Vertex AI)
- **Internet Connection** (for API calls)

### Hardware Requirements

- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **CPU**: Modern multi-core processor

## 📁 Project Structure

```
agent2/
├── app.py                              # Main Flask application (Port 5000)
├── requirements.txt                    # Python dependencies
├── .env                               # Main configuration (CREATE THIS)
├── .env.example                       # Template for main config
├── ecommerce.db                       # SQLite database
├── sample_data_importer.py            # Database initialization
├──
├── agents/
│   └── customer-service/
│       ├── streaming_server.py        # AI WebSocket server (Port 8001)
│       ├── .env                       # Agent config (CREATE THIS)
│       ├── .env.example               # Template for agent config
│       └── customer_service/
│           ├── agent.py               # AI agent logic
│           ├── config.py              # Agent configuration
│           └── tools/                 # AI tools and functions
│
└── cymbal_home_garden_backend/
    ├── static/                        # CSS, JS, Images
    └── templates/                     # HTML templates
```

## 🔐 Security & Credentials Setup

### Step 1: Google Cloud Setup

#### Option A: Vertex AI (Recommended for Production)

1. **Create Google Cloud Project**:

   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project or select existing
   - Note your Project ID (format: `my-project-123456`)

2. **Enable Required APIs**:

   ```bash
   # Enable these APIs in Google Cloud Console:
   - Vertex AI API
   - Generative Language API
   - Cloud Speech-to-Text API (optional)
   - Retail API (for recommendations)
   ```

3. **Create Service Account**:
   - Go to IAM & Admin > Service Accounts
   - Create new service account
   - Assign roles: `Vertex AI User`, `AI Platform Developer`
   - Generate JSON key file
   - **IMPORTANT**: Save the key file to a secure location outside the project
   - Recommended path: `C:\Users\[USERNAME]\gcp-credentials\` (Windows)

#### Option B: Google AI Studio (Simpler for Development)

1. **Get API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Sign in with Google account
   - Click "Get API key"
   - Generate new API key
   - Copy the key (starts with `AIza...`)

### Step 2: Create Configuration Files

#### Main Project Configuration

**Create**: `agent2/.env`

```bash
# Google Cloud Project Configuration
GCP_PROJECT_ID=elemental-day-467117-h4
RETAIL_API_LOCATION=global
RETAIL_CATALOG_ID=default_catalog
RETAIL_SERVING_CONFIG_ID=default_search

# Google API Keys
GEMINI_API_KEY=AIzaSyBwzIzkJELZMTijb-R_Kcea2x0rteeJ3F8

# Google Cloud Authentication (for Vertex AI)
GOOGLE_APPLICATION_CREDENTIALS=C:\Users\[USERNAME]\gcp-credentials\[YOUR-KEY-FILE].json
GOOGLE_GENAI_USE_VERTEXAI=1

# Application URLs (default for local development)
BACKEND_API_BASE_URL=http://127.0.0.1:5000/api
WEBSOCKET_URL=ws://localhost:8001
FRONTEND_URL=http://localhost:5000

# Database configuration
DATABASE=ecommerce.db
```

#### Customer Service Agent Configuration

**Create**: `agent2/agents/customer-service/.env`

```bash
# Choose authentication method: 1 for Vertex AI, 0 for Developer API
GOOGLE_GENAI_USE_VERTEXAI=1

# Google API Keys (use same as main config)
GOOGLE_API_KEY=AIzaSyBwzIzkJELZMTijb-R_Kcea2x0rteeJ3F8
GEMINI_API_KEY=AIzaSyBwzIzkJELZMTijb-R_Kcea2x0rteeJ3F8

# Google Cloud Configuration (required if GOOGLE_GENAI_USE_VERTEXAI=1)
GOOGLE_CLOUD_PROJECT=elemental-day-467117-h4
GOOGLE_CLOUD_LOCATION=us-central1

# Google Cloud Service Account Key (for Vertex AI authentication)
GOOGLE_APPLICATION_CREDENTIALS=C:\Users\[USERNAME]\gcp-credentials\[YOUR-KEY-FILE].json
```

## 💻 Installation Instructions

### Step 1: Clone and Navigate

```bash
# Navigate to project directory
cd agent2
```

### Step 2: Python Environment Setup

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Database Setup

```bash
# Initialize the database with sample data
python sample_data_importer.py
```

### Step 4: Configuration Verification

```bash
# Verify your .env files contain all required variables
# Check that GOOGLE_APPLICATION_CREDENTIALS points to existing file
# Ensure API keys are valid (start with AIza...)
```

## 🚀 Running the Application

### Method 1: Manual Startup (Recommended for Development)

**Terminal 1 - Main Flask Application**:

```bash
cd agent2
.venv\Scripts\activate  # Windows
# or: source .venv/bin/activate  # macOS/Linux
python app.py
```

Server will start on: http://127.0.0.1:5000

**Terminal 2 - AI Agent WebSocket Server**:

```bash
cd agent2/agents/customer-service
..\..\venv\Scripts\activate  # Windows
# or: source ../../.venv/bin/activate  # macOS/Linux
python streaming_server.py
```

Server will start on: http://0.0.0.0:8001

### Method 2: Using VS Code

1. Open project in VS Code
2. Select Python interpreter from `.venv`
3. Run `app.py` in one terminal
4. Run `streaming_server.py` in another terminal

## 🌐 Accessing the Application

1. **Main Website**: http://127.0.0.1:5000

   - Browse products
   - Add items to cart
   - Use search functionality

2. **AI Customer Service**:
   - Chat widget appears on the main website
   - WebSocket connection to port 8001
   - Powered by Google Gemini AI

## ✅ Verification Checklist

### Server Status

- [ ] Flask app running on port 5000
- [ ] Streaming server running on port 8001
- [ ] No error messages in console logs
- [ ] Database file `ecommerce.db` exists

### Website Functionality

- [ ] Homepage loads correctly
- [ ] Product catalog displays
- [ ] Search functionality works
- [ ] Cart can add/remove items
- [ ] Chat widget appears

### AI Chatbot

- [ ] Chat widget connects (no connection errors)
- [ ] Can send messages to bot
- [ ] Bot responds with AI-generated answers
- [ ] Bot can search products and answer questions

## 🔧 Troubleshooting

### Common Issues

#### Authentication Errors

```
Error: File [credential-path] was not found
```

**Solution**:

- Verify `GOOGLE_APPLICATION_CREDENTIALS` path is correct
- Ensure service account key file exists
- Check Windows environment variables aren't overriding .env

#### WebSocket Connection Failed

```
WebSocket connection to 'ws://localhost:8001' failed
```

**Solution**:

- Ensure streaming_server.py is running on port 8001
- Check firewall settings
- Verify no other service is using port 8001

#### API Key Issues

```
Error: GEMINI_API_KEY not found
```

**Solution**:

- Verify .env files exist and contain valid API keys
- Check API key format (should start with AIza...)
- Ensure Google Cloud APIs are enabled

#### Database Errors

```
Error: Database not found
```

**Solution**:

- Run `python sample_data_importer.py`
- Check `ecommerce.db` file exists in project root

#### Port Already in Use

```
Error: Address already in use: Port 5000
```

**Solution**:

- Kill existing processes: `taskkill /f /im python.exe` (Windows)
- Or change ports in configuration files

### Debug Mode

Enable detailed logging by adding to your .env:

```bash
DEBUG=True
FLASK_DEBUG=True
```

## 📊 Performance Optimization

### For Better Performance

- Use Python 3.11+ for better performance
- Increase system RAM if possible
- Close unnecessary applications
- Use SSD storage for faster database access

### For Production Deployment

- Set `DEBUG=False` in production
- Use production WSGI server (gunicorn, uwsgi)
- Configure proper CORS settings
- Set up HTTPS certificates
- Use environment-specific configuration files

## 🆘 Support

### Getting Help

1. Check this documentation first
2. Review console logs for specific error messages
3. Verify all configuration files are properly set up
4. Ensure all dependencies are installed correctly

### Common Commands Reference

```bash
# Check Python version
python --version

# List installed packages
pip list

# Check if ports are in use
netstat -an | find "5000"
netstat -an | find "8001"

# Kill Python processes (Windows)
taskkill /f /im python.exe

# Restart with clean environment
deactivate
.venv\Scripts\activate
```

summary to run agent2 system

---

steps for agent2:

1. git clone
2. open agent2 directory in git bash
3. python -m venv .venv
4. .\.venv\Scripts\activate
5. pip install -r requirements.txt
6. on one cmd run "python app.py" 7. on the other cmd run "python localdirectory..\agent2\agents\customer-service\streaming_server.py"
   **************\*\*\*\***************\*\***************\*\*\*\***************

## 🎉 Success!

If everything is set up correctly, you should have:

- ✅ A fully functional e-commerce website
- ✅ AI-powered customer service chatbot
- ✅ Real-time cart updates
- ✅ Product search and recommendations
- ✅ Interactive chat interface with Google Gemini AI

**Ready to explore?** Visit http://127.0.0.1:5000 and start chatting with your AI assistant!
