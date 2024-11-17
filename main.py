import streamlit as st
import pandas as pd
import logging
from utils.auth import authenticate_user
from utils.google_sheets import list_user_sheets, read_google_sheet
from utils.ai_agent import AIAgent
from config import CLIENT_SECRET_FILE, SCOPES

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    st.title("AI Data Enrichment Tool")
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose Data Source", ["Google Sheets", "Upload CSV"])

    # Step 1: Data Source Selection
    if option == "Google Sheets":
        credentials = authenticate_user(CLIENT_SECRET_FILE, SCOPES)
        if credentials:
            sheets = list_user_sheets(credentials)
            if sheets:
                sheet_options = {sheet['name']: sheet['id'] for sheet in sheets}
                selected_sheet_name = st.selectbox("Select a Google Sheet", list(sheet_options.keys()))
                selected_sheet_id = sheet_options[selected_sheet_name]
                range_name = st.text_input("Enter the range (e.g., Sheet1!A1:Z)", "Sheet1!A1:Z")

                if st.button("Load Data"):
                    data = read_google_sheet(credentials, selected_sheet_id, range_name)
                    if not data.empty:
                        st.session_state['input_data'] = data
            else:
                st.warning("No Google Sheets found.")
    else:
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            st.session_state['input_data'] = data

    # Step 2: Process Data
    if 'input_data' in st.session_state:
        st.header("Data Preview")
        st.dataframe(st.session_state['input_data'])

        selected_column = st.selectbox("Select column to process", st.session_state['input_data'].columns)
        st.write(f"Entities in '{selected_column}' column will be used for queries.")
        
        prompt_instruction = st.text_input("Enter your question or instruction", "e.g., Find the name of the CEO")
        query_template = f"{prompt_instruction} for {{entity}}"

        if st.button("Process"):
            agent = AIAgent()
            results = []
            progress_bar = st.progress(0)
            num_entities = len(st.session_state['input_data'][selected_column])

            for i, entity in enumerate(st.session_state['input_data'][selected_column]):
                query = query_template.replace("{entity}", str(entity))
                search_results = agent.search_web(query)
                response = agent.process_with_llm(query, search_results)
                results.append(response)
                
                # Update progress bar
                progress_bar.progress((i + 1) / num_entities)

            st.session_state['input_data']['AI Results'] = results
            st.dataframe(st.session_state['input_data'])

            # Export Processed Data
            st.header("Export Processed Data")
            csv = st.session_state['input_data'].to_csv(index=False).encode('utf-8')
            st.download_button(
                "Download CSV",
                data=csv,
                file_name="processed_data.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
