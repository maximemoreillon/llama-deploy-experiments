# Taken from https://www.llamaindex.ai/blog/introducing-llama-deploy-a-microservice-based-way-to-deploy-llamaindex-workflows

from llama_deploy import (
    deploy_workflow,
    WorkflowServiceConfig,
    ControlPlaneConfig,
)
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step

# Define a sample workflow
class MyWorkflow(Workflow):
    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        arg1 = str(ev.get("arg1", ""))
        result = arg1 + "_result"
        return StopEvent(result=result)

async def main():
		# Deploy the workflow as a service
		await deploy_workflow(
		    MyWorkflow(),
		    WorkflowServiceConfig(
		        host="127.0.0.1", port=8002, service_name="my_workflow"
		    ),
		    ControlPlaneConfig(),
		)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())