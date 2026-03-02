#!/usr/bin/env python3
"""Test Google Gemini API - check available models and rate limits."""

import json
import ssl
import urllib.request

API_KEY = "AIzaSyAxGXc-PXnJG1pm0n5EwvhGfjfOfROiGOg"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

def get_models():
    """Get list of available models from Gemini."""
    print("=" * 80)
    print("Fetching available models from Gemini...")
    print("=" * 80)

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/models?key={API_KEY}",
        headers={
            "Content-Type": "application/json",
        },
    )

    try:
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read().decode())

        if "models" in data:
            models = data["models"]
            print(f"\n✅ Found {len(models)} models\n")

            print("📋 Available models:\n")
            for model in models:
                model_name = model.get("name", "").split("/")[-1]
                display_name = model.get("displayName", "")
                description = model.get("description", "")[:100]

                print(f"  • {model_name}")
                if display_name:
                    print(f"    Display: {display_name}")
                if description:
                    print(f"    Desc: {description}")
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

def test_completion(model_name="gemini-2.5-flash"):
    """Test a simple completion to check rate limits."""
    print("=" * 80)
    print(f"Testing completion with model: {model_name}")
    print("=" * 80)

    # Gemini uses a different API format
    payload = json.dumps({
        "contents": [{
            "parts": [{
                "text": "Write 1 sentence about binary search trees."
            }]
        }],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 100,
        }
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        f"{BASE_URL}/models/{model_name}:generateContent?key={API_KEY}",
        data=payload,
        headers={
            "Content-Type": "application/json",
        },
        method="POST"
    )

    try:
        start_time = __import__('time').time()
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        elapsed = __import__('time').time() - start_time

        # Check rate limit headers
        headers = resp.headers
        print("\n📊 Rate Limit Info:")
        for header in headers:
            if "limit" in header.lower() or "quota" in header.lower():
                print(f"  {header}: {headers[header]}")

        data = json.loads(resp.read().decode())

        # Extract content from Gemini format
        candidates = data.get("candidates", [])
        if candidates:
            content = candidates[0].get("content", {})
            parts = content.get("parts", [])
            if parts:
                text = parts[0].get("text", "")

                print(f"\n✅ SUCCESS! ({elapsed:.1f}s)")
                print(f"Response: {text}")

                # Check usage
                usage = data.get("usageMetadata", {})
                if usage:
                    print(f"\n📈 Token Usage:")
                    print(f"  Prompt: {usage.get('promptTokenCount', 0)}")
                    print(f"  Completion: {usage.get('candidatesTokenCount', 0)}")
                    print(f"  Total: {usage.get('totalTokenCount', 0)}")

                return True

        print(f"\n❌ Empty response")
        print(json.dumps(data, indent=2)[:500])
        return False

    except urllib.error.HTTPError as e:
        print(f"\n❌ HTTP Error {e.code}")
        error_body = e.read().decode()
        print(f"Error: {error_body[:500]}")

        if e.code == 429:
            print("\n⚠️  RATE LIMIT EXCEEDED")

        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("\n" + "=" * 80)
    print("GOOGLE GEMINI API TEST")
    print("=" * 80)
    print(f"API Key: {API_KEY[:20]}...{API_KEY[-10:]}")
    print("=" * 80 + "\n")

    # Get available models
    models = get_models()

    # Test completions
    if models:
        print("\n")
        # Try different Gemini models (use current stable models)
        test_models = [
            "gemini-2.5-flash",  # Latest stable Flash
            "gemini-2.0-flash",  # Stable 2.0
            "gemini-flash-latest",  # Always latest Flash
        ]

        for model_name in test_models:
            if test_completion(model_name):
                break
            print("\n")

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Gemini offers generous free tier:")
    print("- 2.0 Flash: 10 RPM, 1M TPM")
    print("- 1.5 Flash: 15 RPM, 1M TPM")
    print("- 1.5 Pro: 2 RPM, 32K TPM")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
