#!/usr/bin/env python3
"""Test Edgen AI API - check available models and rate limits."""

import json
import ssl
import urllib.request

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWQwOTE2YjMtZTM5Yy00Yzg4LTgwNmYtNzBkZDA0YjE5ODBlIiwidHlwZSI6ImFwaV90b2tlbiJ9.JSP4tN8jYGQowtOFAv99A3PdRA9_B9h_Y_SeovAApf0"

# Try multiple possible base URLs
BASE_URLS = [
    "https://api.edgen.ai/v1",
    "http://localhost:33322/v1",  # Edgen is a local AI runtime
]

BASE_URL = BASE_URLS[0]  # Start with cloud API

def get_models():
    """Get list of available models from Edgen AI."""
    print("=" * 80)
    print("Fetching available models from Edgen AI...")
    print("=" * 80)

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/models",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
    )

    try:
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read().decode())

        if "data" in data:
            models = data["data"]
            print(f"\n✅ Found {len(models)} models\n")

            print("📋 Available models:\n")
            for model in models:
                model_id = model.get("id", "")
                owned_by = model.get("owned_by", "")
                context = model.get("context_window", model.get("max_model_len", 0))

                print(f"  • {model_id}")
                if owned_by:
                    print(f"    Owner: {owned_by}")
                if context:
                    print(f"    Context: {context:,} tokens")
                print()

            return models
        elif isinstance(data, list):
            # Some APIs return a list directly
            models = data
            print(f"\n✅ Found {len(models)} models\n")

            print("📋 Available models:\n")
            for model in models:
                if isinstance(model, dict):
                    model_id = model.get("id", model.get("name", ""))
                    print(f"  • {model_id}")
                    print()
                else:
                    print(f"  • {model}")
                    print()

            return models
        else:
            print("❌ Unexpected response format")
            print(json.dumps(data, indent=2))
            return []

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}")
        error_body = e.read().decode()
        print(f"Error: {error_body}")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def test_completion(model_id):
    """Test a simple completion to check rate limits."""
    print("=" * 80)
    print(f"Testing completion with model: {model_id}")
    print("=" * 80)

    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "user", "content": "Write 1 sentence about binary search trees."}
        ],
        "max_tokens": 100,
        "temperature": 0.3,
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
    )

    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)

        # Check rate limit headers
        headers = resp.headers
        print("\n📊 Rate Limit Info:")
        for header in headers:
            if "limit" in header.lower() or "remaining" in header.lower() or "reset" in header.lower():
                print(f"  {header}: {headers[header]}")

        data = json.loads(resp.read().decode())
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")

        if content:
            print(f"\n✅ SUCCESS!")
            print(f"Response: {content}")

            # Check usage
            usage = data.get("usage", {})
            if usage:
                print(f"\n📈 Token Usage:")
                print(f"  Prompt: {usage.get('prompt_tokens', 0)}")
                print(f"  Completion: {usage.get('completion_tokens', 0)}")
                print(f"  Total: {usage.get('total_tokens', 0)}")

            return True
        else:
            print(f"\n❌ Empty response")
            print(json.dumps(data, indent=2))
            return False

    except urllib.error.HTTPError as e:
        print(f"\n❌ HTTP Error {e.code}")
        error_body = e.read().decode()
        print(f"Error: {error_body}")

        if e.code == 429:
            print("\n⚠️  RATE LIMIT EXCEEDED")
            # Try to get rate limit headers from error
            for header in e.headers:
                if "limit" in header.lower() or "remaining" in header.lower():
                    print(f"  {header}: {e.headers[header]}")

        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("\n" + "=" * 80)
    print("EDGEN AI API TEST")
    print("=" * 80)
    print(f"API Key: {API_KEY[:30]}...{API_KEY[-20:]}")
    print("=" * 80 + "\n")

    # Get available models
    models = get_models()

    # Test completions with different models if available
    if models:
        print("\n")
        # Try to find a good model
        test_models = []
        for model in models:
            if isinstance(model, dict):
                model_id = model.get("id", model.get("name", ""))
                if model_id and ("llama" in model_id.lower() or "qwen" in model_id.lower()):
                    test_models.append(model_id)
                    break

        # If no specific model found, just use the first one
        if not test_models and models:
            first_model = models[0]
            if isinstance(first_model, dict):
                test_models.append(first_model.get("id", first_model.get("name", "")))
            else:
                test_models.append(str(first_model))

        for model_id in test_models[:1]:  # Test just one
            if model_id:
                test_completion(model_id)
                print("\n")

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Check the rate limit headers above for daily/hourly limits.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
