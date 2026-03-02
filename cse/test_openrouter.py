#!/usr/bin/env python3
"""Test OpenRouter API - check available models and rate limits."""

import json
import ssl
import urllib.request

API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1"

def get_models():
    """Get list of available models from OpenRouter."""
    print("=" * 80)
    print("Fetching available models from OpenRouter...")
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

            # Filter for free/cheap models good for our use case
            print("📋 Recommended models (70B-200B range, good for education):\n")

            for model in models:
                model_id = model.get("id", "")
                name = model.get("name", model_id)
                context = model.get("context_length", 0)
                pricing = model.get("pricing", {})

                # Look for models in our range (70B-200B equivalent)
                if any(x in model_id.lower() for x in ["70b", "72b", "qwen", "deepseek", "llama"]):
                    prompt_price = float(pricing.get("prompt", "0"))
                    completion_price = float(pricing.get("completion", "0"))

                    if prompt_price == 0:
                        price_str = "FREE"
                    else:
                        price_str = f"${prompt_price*1000:.4f}/1K tokens"

                    print(f"  • {model_id}")
                    print(f"    Name: {name}")
                    print(f"    Context: {context:,} tokens")
                    print(f"    Price: {price_str}")
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

def test_completion(model_id="meta-llama/llama-3.3-70b-instruct"):
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
            "HTTP-Referer": "https://github.com/your-repo",  # Optional
            "X-Title": "VTU Content Generator",  # Optional
        },
    )

    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)

        # Check rate limit headers
        headers = resp.headers
        print("\n📊 Rate Limit Info:")
        for header in ["x-ratelimit-limit-requests", "x-ratelimit-remaining-requests",
                      "x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens",
                      "x-ratelimit-reset-requests"]:
            if header in headers:
                print(f"  {header}: {headers[header]}")

        data = json.loads(resp.read().decode())
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")

        if content:
            print(f"\n✅ SUCCESS!")
            print(f"Response: {content}")
            return True
        else:
            print(f"\n❌ Empty response")
            print(json.dumps(data, indent=2))
            return False

    except urllib.error.HTTPError as e:
        print(f"\n❌ HTTP Error {e.code}")
        error_body = e.read().decode()
        print(f"Error: {error_body}")

        # Check if it's a rate limit error
        if e.code == 429:
            print("\n⚠️  RATE LIMIT EXCEEDED")

        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("\n" + "=" * 80)
    print("OPENROUTER API TEST")
    print("=" * 80)
    print(f"API Key: {API_KEY[:20]}...{API_KEY[-10:]}")
    print("=" * 80 + "\n")

    # Get available models
    models = get_models()

    # Test a completion
    if models:
        print("\n")
        test_completion("meta-llama/llama-3.3-70b-instruct")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Check the rate limit info above to see your daily limits.")
    print("OpenRouter typically shows limits in the response headers.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
