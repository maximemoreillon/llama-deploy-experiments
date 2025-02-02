import asyncio
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step, Event


class TestEvent1 (Event):
    result: str

class TestEvent2 (Event):
    result: str

class TestWorkflow(Workflow):
    """A test workflow"""

    @step()
    async def startStep(self, ev: StartEvent) -> TestEvent1:
        message = ev.message
        return TestEvent1(result=f"Message received: {message}")
    
    @step()
    async def intermediateEvent(self, ev: TestEvent1) -> TestEvent2:
        event1Result = ev.result
        return TestEvent2(result=f"Event 1 result: {event1Result}")

    @step()
    async def stopStep(self, ev: TestEvent2) -> StopEvent:
        event2Result = ev.result
        return StopEvent(result=f"Event 2 result: {event2Result}")


# `echo_workflow` will be imported by LlamaDeploy
testWorkflow = TestWorkflow()


async def main():
    result = await testWorkflow.run(message="Hello!")
    print(result)


# Make this script runnable from the shell so we can test the workflow execution
if __name__ == "__main__":
    asyncio.run(main())