# AI-Data-Enrichment-Agent


A Streamlit-based application that enriches data from Google Sheets or CSV files using AI and web search capabilities.

## Features

- Google Sheets Integration
- CSV File Support
- AI-powered data enrichment using Groq
- Web search integration using Google Serper API
- Rate limiting for API calls
- Export results to CSV

## Prerequisites

- Python 3.8+
- Google Cloud Project with Sheets API enabled
- Groq API key
- Serper API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pantShrey/AI-Data-Enrichment-Agent.git
cd ai-data-enrichment
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

5. Set up Google OAuth credentials:
   - Go to Google Cloud Console
   - Create a new project or select existing one
   - Enable Google Sheets and Drive APIs
   - Create OAuth 2.0 credentials
   - Download client secret file and place it in the project root

## Usage

1. Start the application:
```bash
streamlit run app/main.py
```

2. Select your data source (Google Sheets or CSV)
3. Authenticate with Google (if using Google Sheets)
4. Select the column to process
5. Enter your query template
6. Process the data and download results

## Configuration

The following environment variables are required:

- `GROQ_API_KEY`: Your Groq API key
- `SERPER_API_KEY`: Your Serper API key
- `CLIENT_SECRET_FILE`: Path to your Google OAuth client secret file

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Demonstration

https://www.loom.com/share/68f008635ae04c7ea52917147d1c5080

Don't know how to blur the code on loom sorry for that 