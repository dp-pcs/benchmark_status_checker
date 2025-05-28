from crewai.tools import BaseTool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CREW_API_URL = os.getenv("CREW_API_URL")
CREW_BEARER_TOKEN = os.getenv("CREW_BEARER_TOKEN")

class BenchmarkStatusChecker(BaseTool):
    name: str = "BenchmarkStatusChecker"
    description: str = "Fetches the current status and final results of a benchmark test by kickoff ID."

    def _run(self, kickoff_id: str) -> str:
        try:
            url = f"{CREW_API_URL}/status/{kickoff_id}"
            headers = {
                "Authorization": f"Bearer {CREW_BEARER_TOKEN}"
            }

            response = requests.get(url, headers=headers, timeout=60)

            if response.ok:
                return response.text
            else:
                return f"Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"Failed to retrieve benchmark status: {str(e)}"
