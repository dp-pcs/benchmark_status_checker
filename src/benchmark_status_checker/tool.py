from crewai.tools import BaseTool
import requests

class BenchmarkStatusChecker(BaseTool):
    name: str = "BenchmarkStatusChecker"
    description: str = "Fetches the current status and final results of a benchmark test by kickoff ID."

    def _run(self, kickoff_id: str) -> str:
        try:
            url = f"https://evaluating-agentic-frameworks-for-crew-auto-8a97fceb.crewai.com/status/{kickoff_id}"
            headers = {
                "Authorization": "Bearer f754b06c7dd4"
            }

            response = requests.get(url, headers=headers, timeout=60)

            if response.ok:
                return response.text
            else:
                return f"Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"Failed to retrieve benchmark status: {str(e)}"
