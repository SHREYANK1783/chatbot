import json
import pickle
from pathlib import Path

p = Path(__file__).parent

with open(p / 'intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

print(f"Loaded {len(intents.get('intents', []))} intents (placeholder).")

# Create simple placeholder model/vectorizer objects
model = {"type": "placeholder"}
vectorizer = {"type": "placeholder"}

with open(p / 'model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open(p / 'vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print('Wrote placeholder model.pkl and vectorizer.pkl')
