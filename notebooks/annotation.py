import csv
from openai import AzureOpenAI

model_name = "gpt-4o-mini"

system_prompt = 'You are an expert in categorizing TikTok videos from now on. You need to categorize TikTok videos based on their description, hashtags and author, choose from the following categories: "Beauty & fashion", "Culture & entertainment", "Education", "Health & lifestyle", "News, politics & society", "Other", "Relationship". 1 category per element. Additionally you will label content based on whether it is an ad/sponsored content/promotion (output 1 or 0). The output format should be "<category>, <1 or 0 for advertisement>"'

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

input_fp = 'data/csv/bramssjan 2nd scroll - processed.csv'
output_fp = 'data/csv/bramssjan 2nd scroll - annotated.csv'

with open(input_fp, newline='', encoding='utf8') as csvfile:
    with open(output_fp, newline='', encoding='utf8', mode='w') as new_file:

        reader = csv.DictReader(csvfile)

        fieldnames = list(reader.fieldnames)
        fieldnames.append('llm_raw_content')
        fieldnames.append('llm_category')
        fieldnames.append('llm_ad')

        writer = csv.DictWriter(new_file,fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            description = str(row['body']) + str(row['stickers'])
            author = "author: " + str(row['author_full'])
            print(f"tag: {description}")
            if description == "":
                row['llm_raw_content'] = ""
                row['llm_category'] = ""
                row['llm_ad'] = ""
                writer.writerow(row)
                continue

            try:
                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": description + " " + author,
                        }
                    ],
                    max_tokens=4096,
                    temperature=1.0,
                    top_p=1.0,
                    model=deployment
                )
            except Exception as e:
                print(f'Error during annotation {e}')
                row['llm_raw_content'] = e
                row['llm_category'] = ""
                row['llm_ad'] = ""
                writer.writerow(row)
                continue

            try:
                content: str = response.choices[0].message.content.split(",")
                print(f"annotation {content}")
                category = content[0]
                ad = content[1]
            except Exception as e:
                print(f'Unable to parse response {e}')
                row['llm_raw_content'] = e
                row['llm_category'] = ""
                row['llm_ad'] = ""
                writer.writerow(row)
                continue


            row['llm_raw_content'] = content
            row['llm_category'] = category
            row['llm_ad'] = ad
            writer.writerow(row)
