#!/usr/bin/env python3
"""Test Hyperbolic AI API - check available models and rate limits."""

import json
import ssl
import urllib.request

API_KEY = "sk_live_t_CLneoZt0WDaPpU8zNLKQrAo5Zx0TA_Yw7dAAU6WBncAS__f0KGSkUT5YKUephew"
BASE_URL = "https://api.hyperbolic.xyz/v1"

def get_models():
    """Get list of available models from Hyperbolic."""
    print("=" * 80)
    print("Fetching available models from Hyperbolic...")
    print("=" * 80)

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/models",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
    )
    req.add_header('User-Agent', 'Mozilla/5.0')

    try:
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read().decode())

        if "data" in data:
            models = data["data"]
            print(f"\n✅ Found {len(models)} models\n")

            print("📋 Available models (showing 70B+ models):\n")
            count = 0
            for model in models:
                model_id = model.get("id", "")
                owned_by = model.get("owned_by", "")

                # Filter for larger models
                if any(x in model_id.lower() for x in ["70b", "72b", "405b", "qwen"]):
                    print(f"  • {model_id}")
                    if owned_by:
                        print(f"    Owner: {owned_by}")
                    print()
                    count += 1

            if count == 0:
                print("  Showing all models:")
                for model in models[:15]:
                    print(f"  • {model.get('id', '')}")
                print()

            return models
        else:
            print("❌ No models found in response")
            print(json.dumps(data, indent=2)[:1000])
            return []

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}")
        error_body = e.read().decode()
        print(f"Error: {error_body}")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def test_completion(model_id="meta-llama/Llama-3.3-70B-Instruct"):
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
        start_time = __import__('time').time()
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        elapsed = __import__('time').time() - start_time

        # Check rate limit headers
        headers = resp.headers
        print("\n📊 Rate Limit Info:")
        for header in headers:
            if "limit" in header.lower() or "remaining" in header.lower() or "reset" in header.lower():
                print(f"  {header}: {headers[header]}")

        data = json.loads(resp.read().decode())
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")

        if content:
            print(f"\n✅ SUCCESS! ({elapsed:.1f}s)")
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

        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("\n" + "=" * 80)
    print("HYPERBOLIC AI API TEST")
    print("=" * 80)
    print(f"API Key: {API_KEY[:30]}...{API_KEY[-15:]}")
    print("=" * 80 + "\n")

    # Get available models
    models = get_models()

    # Test completions
    if models:
        print("\n")
        # Try different model names
        test_models = [
            "meta-llama/Llama-3.3-70B-Instruct",
            "meta-llama/Meta-Llama-3.1-70B-Instruct",
            "Qwen/Qwen2.5-72B-Instruct",
        ]

        for model_id in test_models:
            if test_completion(model_id):
                break
            print("\n")

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Hyperbolic offers free tier for testing")
    print("Supports Llama 3.1 70B/405B and Qwen models")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
