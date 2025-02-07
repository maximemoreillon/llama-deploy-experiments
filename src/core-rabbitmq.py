# From https://www.llamaindex.ai/blog/introducing-llama-deploy-a-microservice-based-way-to-deploy-llamaindex-workflows
from llama_deploy import (
    deploy_core,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
    # RabbitMQMessageQueueConfig, # Does not exist
)
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_deploy.message_queues.rabbitmq import RabbitMQMessageQueue
from os import getenv

load_dotenv()

RABBITMQ_HOST=getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT=getenv("RABBITMQ_PORT", 5672)


message_queue = RabbitMQMessageQueue(host=RABBITMQ_HOST, port=RABBITMQ_PORT)  # uses the default url



async def main():
		# Deploy the workflow as a service
		await deploy_core(
		    control_plane_config=ControlPlaneConfig(),
		    #message_queue_config=SimpleMessageQueueConfig(),
        # message_queue=message_queue # deploy_core() got an unexpected keyword argument 'message_queue'
		)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())