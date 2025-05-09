import requests

# API URL
url = "http://127.0.0.1:8000/recommend"

# Sample query
payload = {
    "query": "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript. Need an assessment package that can test all skills with max duration of 60 minutes."
}

# Make POST request
response = requests.post(url, json=payload)

# Display results
if response.status_code == 200:
    results = response.json().get("results", [])
    print("✅ Top Recommendations:\n")
    for r in results:
        print(f"🔹 {r['name']}")
        print(f"   URL: {r['url']}")
        print(f"   Remote: {r['remote']}, Adaptive: {r['adaptive']}")
        print(f"   Duration: {r['duration']} mins, Type: {r['test_type']}\n")
else:
    print("❌ Request failed:", response.text)
