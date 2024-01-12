from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    # Retrieve the API key from the environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    # Check if the API key is present
    if not api_key:
        raise ValueError("API key not found in the .env file")
    
    return api_key

def initialize_openai_client(api_key):
    # Initialize the OpenAI client
    return OpenAI(api_key=api_key)

def ingest_data(client, file_location):
    # Data Ingestion
    with open(file_location, 'rb') as file:
        response = client.files.create(file=file, purpose='assistants')
    
    return response.id

def create_assistant(client, file_id):
    # Create Assistant
    # assistant = client.beta.assistants.create(
    #     instructions="You are a knowledge assistant. Use your knowledge base to best respond to user queries.",
    #     model="gpt-4-1106-preview",
    #     tools=[{"type": "code"}],
    #     file_ids=[file_id]
    # )

    assistant = client.beta.assistants.create(
    instructions="You are a personal AI bot specializing in cryptocurrency. When presented with a user's query, utilize the provided dataset to assist in formulating a response to the question. Additionally, incorporate visualizations to enhance the presentation of information.",
    model="gpt-4-1106-preview",
    tools=[{"type": "code_interpreter"}],
    file_ids=[file_id]
    )
        
    return assistant.id

def initiate_thread(client, prompt):
    # Create Thread
    messages = [{"role": "user", "content": prompt}]
    thread = client.beta.threads.create(messages=messages)
    
    return thread.id

def run_assistance(client, thread_id, assistant_id):
    # Run Assistance
    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)
    return run.id

def check_run_status(client, thread_id, run_id):
    # Check Run Status
    run = client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)
    
    return run.status

def retrieve_thread(client, thread_id):
    # Retrieve Message from specified thread_id
    thread_message = client.beta.threads.messages.list(thread_id=thread_id)
    assistance_message = thread_message.data[0]
    reference = assistance_message.content[0].text.annotations[0].file_citation.quote
    message_text = assistance_message.content[0].text.value
    
    return message_text, reference

def addMessageToThread(client, thread_id,prompt):
    thread_message = client.beta.threads.create(thread_id,role="user",content=prompt)

def display_message(client,thread_id):
    messages = client.beta.threads.messages.list(
    thread_id=thread_id
    )

    for message in reversed(messages.data):
        print(message.role +":"+message.content[0].text.value)

# Main program flow
if __name__ == '__main__':
    api_key = get_api_key()
    openai_client = initialize_openai_client(api_key)
        # Base directory
    base_dir = os.getcwd()

    # File LOCATION
    additional_location = "data/BTC-USD.csv"

    # Combine paths using os.path.join()
    loc = os.path.join(base_dir, additional_location)

    file_id = ingest_data(openai_client,loc)
    print(file_id)
    assistant_id = create_assistant(openai_client, file_id)
    print(assistant_id)
    prompt = input("Enter your question: ")
    thread_id = initiate_thread(openai_client, prompt)
    print(thread_id)
    run_id = run_assistance(openai_client, thread_id, assistant_id)
    print(run_id)

    status = check_run_status(openai_client, thread_id, run_id)
    while True:
        status = check_run_status(openai_client,thread_id, run_id)
        if status == "completed":
            message_text, reference = retrieve_thread(openai_client,thread_id)
            print("Answer:", message_text)
            print("Reference:", reference)
            display_message(openai_client,thread_id)
            break
        elif status == "failed":
            print("Assistance run failed.")
            break
        else:
            import time
            print("Assistance run still in progress. Waiting...")
            time.sleep(5)  

    