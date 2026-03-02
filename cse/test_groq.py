#!/usr/bin/env python3
"""Test Groq API - check available models and rate limits."""

import json
import ssl
import urllib.request

API_KEY = "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"
BASE_URL = "https://api.groq.com/openai/v1"

def get_models():
    """Get list of available models from Groq."""
    print("=" * 80)
    print("Fetching available models from Groq...")
    print("=" * 80)

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/models",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    req.add_header('User-Agent', 'Mozilla/5.0')

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
                context = model.get("context_window", 0)

                print(f"  • {model_id}")
                print(f"    Owner: {owned_by}")
                print(f"    Context: {context:,} tokens")
                print()

            return models
        else:
            print("❌ No models found in response")
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
    req.add_header('User-Agent', 'Mozilla/5.0')

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
    print("GROQ API TEST")
    print("=" * 80)
    print(f"API Key: {API_KEY[:20]}...{API_KEY[-10:]}")
    print("=" * 80 + "\n")

    # Get available models
    models = get_models()

    # Test completions with different models if available
    if models:
        print("\n")
        # Try to find a llama model first
        test_models = []
        for model in models:
            model_id = model.get("id", "")
            if "llama" in model_id.lower() and "70b" in model_id.lower():
                test_models.append(model_id)
                break

        # If no 70B llama found, just use the first model
        if not test_models and models:
            test_models.append(models[0].get("id"))

        for model_id in test_models[:1]:  # Test just one
            test_completion(model_id)
            print("\n")

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Groq is known for extremely fast inference speeds.")
    print("Check the rate limit headers above for daily/hourly limits.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
