import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

body = {
	"input": """<s>[INST] <<SYS>>
You are a marketing consultant. 
<</SYS>>

Please generate a promotional email to visit the following attractions in Washington, DC:
1. The National Mall
2. The Smithsonian Museums
3. The White House
4. The U.S. Capitol 
5. The National Gallery of Art
[/INST]
""",
	"parameters": {
		"decoding_method": "sample",
		"max_new_tokens": 500,
		"temperature": 0.7,
		"top_k": 50,
		"top_p": 1,
		"repetition_penalty": 1
	},
	"model_id": "meta-llama/llama-2-13b-chat",
	"project_id": "17a44346-5bda-463e-a247-de1e63f4e572",
	"moderations": {
		"hap": {
			"input": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			},
			"output": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			}
		},
		"pii": {
			"input": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			},
			"output": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			}
		}
	}
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()