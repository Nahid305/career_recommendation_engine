#!/bin/bash
# Deployment setup script for CareerCraft AI

echo "🚀 Setting up CareerCraft AI for deployment..."

# Create .streamlit directory if it doesn't exist
mkdir -p ~/.streamlit/

# Copy configuration files
echo "📁 Setting up Streamlit configuration..."
cp -r .streamlit/* ~/.streamlit/ 2>/dev/null || :

# Set environment variables for deployment
echo "🔧 Setting environment variables..."
echo "[server]
headless = true
port = \$PORT
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml

echo "✅ Deployment setup complete!"
echo "🌐 Run 'streamlit run app.py' to start the application"
