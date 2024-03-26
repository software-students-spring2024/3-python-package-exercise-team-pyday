# PyWeath

## Setup

### Getting an API Key

1. Sign up for the free version of an OpenWeatherMap account and obtain an API key.
2. Set an environment variable on your system to store this key:

   - On Linux/macOS: `export OPENWEATHERMAP_API_KEY='your_api_key_here'`
   - On Windows: Set `OPENWEATHERMAP_API_KEY` as a system environment variable through the System Properties.

### Configuring the Project

1. Clone the repository and navigate to the project directory.
2. (If using a `.env` file for local development) Create a `.env` file in the root directory and add `OPENWEATHERMAP_API_KEY=your_api_key_here`. Make sure `.env` is listed in your `.gitignore` file to prevent it from being committed.
