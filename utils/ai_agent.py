from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.prompts import PromptTemplate
from utils.rate_limiting import limits, sleep_and_retry
from config import GROQ_API_KEY, SERPER_API_KEY

class AIAgent:
    def __init__(self):
        self.llm = ChatGroq(api_key=GROQ_API_KEY)
        self.search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

    @sleep_and_retry
    @limits(calls=30, period=60)
    def process_with_llm(self, query: str, search_results: str) -> str:
        prompt = PromptTemplate(
            template="""Extract key information about {query} following these rules:
            1. Focus only on the most relevant facts
            2. Format as bullet points
            3. Maximum 5 key points
            4. Exclude unnecessary details
            5. Be objective and precise
            6. If not found, mention NOT FOUND
            Search Results: {results}
            Key Information:""",
            input_variables=["query", "results"]
        )
        return self.llm.predict(prompt.format(query=query, results=search_results))

    @sleep_and_retry
    @limits(calls=50, period=60)
    def search_web(self, query: str) -> str:
        return self.search.run(query)
