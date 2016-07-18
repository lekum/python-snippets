import base64

original_text = input("Please enter some text:")
print("Encoded version:")
print(base64.b64encode(original_text.encode()).decode())
