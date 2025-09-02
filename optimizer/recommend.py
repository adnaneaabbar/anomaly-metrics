from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

def recommend_actions(report: dict, anomalies_path: str) -> str:
    # Load anomalies if needed
    with open(anomalies_path, "r") as f:
        anomalies_csv = f.read()

    prompt = PromptTemplate(
        input_variables=["analysis", "anomalies"],
        template="""
        Given the following system analysis and detected anomalies, produce a structured report (JSON format) proposing concrete actions to optimize infrastructure performance (e.g., load balancing, resource adjustment, etc.).

        Analysis:
        {analysis}

        Anomalies (CSV):
        {anomalies}

        Recommendations:
        """
    )

    llm = ChatOpenAI(model="gpt-4o")

    chain = prompt | llm
    response = chain.invoke({"analysis": report, "anomalies": anomalies_csv})

    return response.content
