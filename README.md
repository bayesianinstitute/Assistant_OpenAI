# Assistant OpenAI

This Python script utilizes the OpenAI API to create an assistant, ingest data, and provide assistance in a conversation. The script is designed to interact with OpenAI's GPT models to respond to user queries based on a knowledge base.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed (version X.X.X)
- OpenAI API key
- A .env file with the OpenAI API key (refer to the provided sample.env)

## Getting Started

Follow these steps to set up the environment and run the OpenAI Assistant Python script:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/OpenAI-Assistant-Script.git
```

### 2. Navigate to the Project Directory

```bash
cd OpenAI-Assistant-Script
```

### 3. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

On Windows:

```bash
.\venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a .env file in the project directory:

```bash
touch .env
```

Open the .env file and add your OpenAI API key:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

Save and close the .env file.

### 6. Run the Script

```bash
python main.py
```

### 7. Enter Your Question

Follow the prompts and enter your question when prompted.

### 8. View Results

The script will communicate with the OpenAI API to provide a response based on the knowledge base.

## Script Components

- **get_api_key():** Retrieves the OpenAI API key from the environment variables.

- **initialize_openai_client(api_key):** Initializes the OpenAI client with the provided API key.

- **ingest_data(client, file_location):** Ingests data by uploading a file to OpenAI.

- **create_assistant(client, file_id):** Creates an OpenAI assistant using the specified knowledge base.

- **initiate_thread(client, prompt):** Initiates a conversation thread with a user prompt.

- **run_assistance(client, thread_id, assistant_id):** Runs the assistance based on the initialized thread and assistant.

- **check_run_status(client, thread_id, run_id):** Checks the status of the assistance run.

- **retrieve_thread(client, thread_id):** Retrieves the response and reference from the specified thread.

- **addMessageToThread(client, thread_id, prompt):** Adds a user message to the conversation thread.

- **display_message(client, thread_id):** Displays the conversation thread messages.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the powerful GPT models.

Feel free to customize the README according to your project's specific details and requirements.