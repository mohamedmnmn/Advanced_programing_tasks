import re
emails = ["user@example.com", "bad-email", "test@domain.org"]
pattern = r'^[A-Za-z0-9_.]+@[A-Za-z0-9]+\.[A-Za-z]+$'
for email in emails:
    if re.match(pattern, email):
        print(f" {email} is valid")
    else:
        print(f"{email} is invalid")
# ---------------------------------------------
txt = "I love #Python and #AI"
pattern2=r'#\w+'
htags = re.findall(pattern2, txt)
print(htags)
# ---------------------------------------------
nums = ["+1-555-1234", "123-456-7890", "5551234"]
pattern3 = r'^(\+\d{1,3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
for n in nums:
    if re.match(pattern3, n):
        print(f"{n} is valid")
    else:
        print(f"{n} is invalid")
# ----------------------------------------------

text = "Python, Python! AI is great; Python AI."
words = re.findall(r'\b\w+\b', text.lower())
frequency = {}
for w in words:
    frequency[w] = frequency.get(w, 0) + 1
print(frequency)
# -----------------------------------------------
pattern4 = r'\b(\w+)\s+\1\b'
text = "This is is a test test"
matche = re.findall(r'(\b\w+\b)\s+\1', text) 
for match in re.finditer(r'\b(\w+)\s+\1\b', text):
    print(match.group()) 
# ----------------------------------------------
text = "The events are on 2023-05-12 and 2024-01-01."
pattern5 = r'\b\d{4}-\d{2}-\d{2}\b'
dates = re.findall(pattern5, text)
print(dates)
# --------------------------------------------
text = "Card: 1234-5678-9012-3456"
pattern6 = r'(\d{4})-(\d{4})-(\d{4})-(\d{4})'
def mask_card(match):
    groups = match.groups()
    masked = f"****-****-****-{groups[3]}"
    return masked
masked_text = re.sub(pattern, mask_card, text)
print(masked_text)
# ---------------------------------------------
text = "I know Python, Java, and C++ but not Ruby."
pattern8 = r'[A-Za-z][A-Za-z+#]*'
words = re.findall(pattern8, text)
programming_lang=['python','java','c++','ruby','c','c#']
filtered_words=[]
for s in words:
    if s.lower() in programming_lang:
        filtered_words.append(s) 
print(filtered_words)