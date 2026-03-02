#!/usr/bin/env python3
"""Quick test to verify all APIs are working and returning content."""

import json
import os
import ssl
import urllib.request

APIS = {
    "nvidia": {
        "base_url": "https://integrate.api.nvidia.com/v1/chat/completions",
        "api_key": os.environ.get("NVIDIA_API_KEY", "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"),
        "model": "meta/llama-3.3-70b-instruct",
    },
    "chutes": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
        "model": "deepseek-ai/DeepSeek-R1-TEE",  # Original model that was working
    },
    "minimax": {
        "base_url": "https://api.minimax.io/v1/chat/completions",
        "api_key": "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg",
        "model": "MiniMax-M2.5",  # Try the larger model
    },
}

def test_api(api_name, api_config):
    """Test one API with a simple prompt."""
    print(f"\n{'='*80}")
    print(f"Testing {api_name.upper()}")
    print(f"{'='*80}")
    print(f"URL: {api_config['base_url']}")
    print(f"Model: {api_config['model']}")

    # Simple test prompt
    payload = json.dumps({
        "model": api_config["model"],
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a 2-sentence summary of what a binary search tree is."}
        ],
        "max_tokens": 200,
        "temperature": 0.3,
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        api_config["base_url"],
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_config['api_key']}",
        },
        method="POST"
    )

    try:
        print("Sending request...")
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        data = json.loads(resp.read().decode())

        # Extract response
        message = data.get("choices", [{}])[0].get("message", {})
        content = message.get("content", "")

        # Handle DeepSeek R1 format (reasoning in separate field)
        if not content:
            content = message.get("reasoning_content", "")

        if content:
            print(f"✅ SUCCESS!")
            print(f"Response ({len(content)} chars):")
            # Show first 500 chars (reasoning can be very long)
            if len(content) > 500:
                print(f"{content[:500]}...")
            else:
                print(f"{content}")
            return True
        else:
            print(f"❌ FAILED: Empty response")
            print(f"Full response: {json.dumps(data, indent=2)[:1000]}")
            return False

    except urllib.error.HTTPError as e:
        print(f"❌ FAILED: HTTP {e.code}")
        try:
            error_body = e.read().decode()
            print(f"Error body: {error_body}")
        except:
            pass
        return False
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {str(e)}")
        return False

def main():
    print("\n" + "="*80)
    print("API CONNECTION TEST")
    print("="*80)

    results = {}

    # Test each API (all keys are now hardcoded)
    for api_name, api_config in APIS.items():
        results[api_name] = "SUCCESS" if test_api(api_name, api_config) else "FAILED"

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for api_name, status in results.items():
        icon = "✅" if status == "SUCCESS" else ("⚠️" if status == "SKIPPED" else "❌")
        print(f"{icon} {api_name.upper()}: {status}")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
