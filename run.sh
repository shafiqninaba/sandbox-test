#!/bin/bash

echo "========================================="
echo "   Python Data Analysis Tool Runner     "
echo "========================================="
echo ""

echo "📦 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "✅ Found Python version: $PYTHON_VERSION"
echo ""

echo "📥 Installing dependencies from requirements.txt..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi

echo ""
echo "========================================="
echo "🚀 Running the application..."
echo "========================================="
echo ""

python3 main.py "$@"

EXIT_CODE=$?

echo ""
echo "========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Application completed successfully"
else
    echo "❌ Application exited with error code: $EXIT_CODE"
fi
echo "========================================="

deactivate 2>/dev/null

exit $EXIT_CODE
