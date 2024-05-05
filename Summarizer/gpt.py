import openai
import time
def process_text(input_text):
    # Do something with the input_text
    processed_text = f"Processed: {input_text}"
    return processed_text

openai.api_key = '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'

operands = """
1+1
"""
prompt = f"do the arithmetic operation:\n{operands}\nSteps:"

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    operands = response['choices'][0]['text'].strip()
    print(operands)

except openai.error.RateLimitError as e:
    # Handle rate limit error by waiting for a minute and then retrying
    print(f"Rate limited. Waiting for a minute. Error: {e}")
    time.sleep(60)  # Wait for a minute    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    operands = response['choices'][0]['text'].strip()
    print(operands)

