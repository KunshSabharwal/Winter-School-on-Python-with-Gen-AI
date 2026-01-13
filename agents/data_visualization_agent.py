from .base_agent import BaseAgent, AgentResult
from typing import Dict, Any, List
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64


class DataVisualizationAgent(BaseAgent):
    """
    Agent responsible for generating visualizations from tabular data.
    """

    def __init__(self, api_key: str):
        super().__init__(name="DataVisualizer", api_key=api_key)

    def get_capabilities(self) -> List[str]:
        return [
            "Create visualizations (line, bar, scatter plots)",
            "Visualize CSV or previously analyzed data",
            "Return plots as base64-encoded images",
        ]

    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        print("data visualizer was called")
        """
        Expected input:
        - files: CSV files OR
        - context: codeinterpreter_data containing tabular data
        """

        files = input_data.get("files", {})
        context = input_data.get("context", {})
        plot_type = input_data.get("plot_type", "line")

        df = None

        # Try to load CSV if provided
        if files:
            try:
                csv_path = list(files.values())[0]
                df = pd.read_csv(csv_path)
            except Exception as e:
                return AgentResult(
                    success=False,
                    data={},
                    message=f"Failed to load CSV file: {str(e)}",
                    agent_name=self.name,
                )

        # try to get data from CodeInterpreter context
        elif "codeinterpreter_data" in context:
            data = context["codeinterpreter_data"]
            if isinstance(data, dict) and "dataframe" in data:
                df = pd.DataFrame(data["dataframe"])

        if df is None or df.shape[1] < 2:
            return AgentResult(
                success=False,
                data={},
                message="No valid tabular data found for visualization",
                agent_name=self.name,
            )

        x_col = df.columns[0]
        y_col = df.columns[1]

        # Generate plot
        try:
            plt.figure(figsize=(8, 5))

            if plot_type == "line":
                plt.plot(df[x_col], df[y_col])
            elif plot_type == "bar":
                plt.bar(df[x_col], df[y_col])
            elif plot_type == "scatter":
                plt.scatter(df[x_col], df[y_col])
            else:
                return AgentResult(
                    success=False,
                    data={},
                    message=f"Unsupported plot type: {plot_type}",
                    agent_name=self.name,
                    next_agent="AnswerSynthesizer",
                )

            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f"{plot_type.capitalize()} plot of {y_col} vs {x_col}")

            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            plt.close()
            buffer.seek(0)

            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

            return AgentResult(
                success=True,
                data={"plot_base64": image_base64},
                message="Visualization created successfully",
                agent_name=self.name,
                next_agent="AnswerSynthesiser",  # chain to explanation
            )

        except Exception as e:
            return AgentResult(
                success=False,
                data={},
                message=f"Visualization error: {str(e)}",
                agent_name=self.name,
            )
