from openai import OpenAI
import requests
import base64
import json

client = OpenAI(
  api_key='Enter you api key here',
)
github_token = 'Enter your github token here '
github_headers = {
    'Authorization': f'token {github_token}',
    'Content-Type': 'application/json'
}

# Fetch the code from a specified GitHub repository
repo_owner = 'IAMNISHANTSHUKLA'
repo_name = 'XCCC'
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents'
response = requests.get(url, headers=github_headers)
repo_contents = response.json()

# print(completion.choices[0].message)

for content in repo_contents:
    if content['type'] == 'file':
        file_name = content['name']
        file_content = requests.get(content['download_url']).text

        # Send the code to ChatGPT for analysis
        prompt = f"Analyze the code of the '{file_name}' file in the GitHub repository '{repo_owner}/{repo_name}'.code is '{file_content}' Find code improvement suggestions in a user-friendly format."

    
        # data = json.dumps({"prompt": prompt, "max_tokens": 50})
        completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)
        print(completion.choices[0].message)
        print("/n")
        print(completion)

        # response = requests.post('https://api.openai.com/v1/engines/gpt-3.5-turbo/completions', headers=chatgpt_headers, data=data)
        # Check for the quota error
        # if 'error' in response.json() and response.json()['error']['code'] == 'insufficient_quota':
        #     print(f"Error: {response.json()['error']['message']}")
        #     print("Please check your OpenAI subscription plan and billing details.")
        #     break  # Exit the loop if there's a quota error
        # else:
        #     # Parse the JSON response from ChatGPT
        #     result_data = json.loads(response.text)
        #     # Display the output from ChatGPT
        #     print(f"Code Analysis Results for '{file_name}':")
        #     print(result_data)
