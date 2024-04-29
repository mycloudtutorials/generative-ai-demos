import boto3
import json

client = boto3.client(service_name = "bedrock-runtime")

model_id = "meta.llama2-13b-chat-v1"
#model_id = "meta.llama3-8b-instruct-v1:0"

user_message = "What is the capital of Norway?"
# user_message = "Write me a fairytale story in 500 words."

prompt = f"<s>[INST] {user_message} [/INST]"

request = {
    "prompt": prompt,
    # Optional inference parameters:
    "max_gen_len": 100,
    "temperature": 0.5,
    "top_p": 0.9,
}

response = client.invoke_model(body=json.dumps(request), modelId=model_id)

# Decode the native response body.
model_response = json.loads(response["body"].read())

print(model_response)

print("-------------")

# Extract and print the generated text.
response_text = model_response["generation"]
print(response_text)