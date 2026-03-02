#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def topic_iter(topics_obj):
    if isinstance(topics_obj, dict):
        return topics_obj.values()
    if isinstance(topics_obj, list):
        return topics_obj
    return []


def has_rating_at_or_below(topic, threshold):
    ratings_by_api = topic.get('ratings')
    if not isinstance(ratings_by_api, dict):
        return False

    for api_payload in ratings_by_api.values():
        if not isinstance(api_payload, dict):
            continue
        rating = api_payload.get('rating')
        if not isinstance(rating, dict):
            continue

        for key in ('coverage_rating', 'content_quality_rating'):
            value = rating.get(key)
            if isinstance(value, (int, float)) and value <= threshold:
                return True

    return False


def build_low_rated_paths(data, threshold):
    topics = data.get('topics') if isinstance(data, dict) else None
    paths = []

    for topic in topic_iter(topics):
        if not isinstance(topic, dict):
            continue
        topic_path = topic.get('topic_path')
        if not isinstance(topic_path, str) or not topic_path.strip():
            continue
        if has_rating_at_or_below(topic, threshold):
            paths.append(topic_path)

    return sorted(set(paths))


def main():
    parser = argparse.ArgumentParser(
        description='Extract topic full paths where any rating is less than or equal to a threshold.'
    )
    parser.add_argument('input_json', help='Path to topic ratings JSON file')
    parser.add_argument(
        '-t',
        '--threshold',
        type=float,
        default=5,
        help='Include topics with rating <= threshold (default: 5)',
    )
    parser.add_argument(
        '-o',
        '--output',
        help='Output .txt file path. Defaults next to input as <stem>_rating_le_<threshold>_paths.txt',
    )
    args = parser.parse_args()

    input_path = Path(args.input_json).expanduser().resolve()
    data = json.loads(input_path.read_text(encoding='utf-8'))

    low_rated_paths = build_low_rated_paths(data, args.threshold)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        threshold_label = str(int(args.threshold)) if args.threshold.is_integer() else str(args.threshold)
        output_path = input_path.with_name(
            f'{input_path.stem}_rating_le_{threshold_label}_paths.txt'
        )

    output_path.write_text('\n'.join(low_rated_paths) + ('\n' if low_rated_paths else ''), encoding='utf-8')

    print(f'Input: {input_path}')
    print(f'Threshold: <= {args.threshold}')
    print(f'Topics matched: {len(low_rated_paths)}')
    print(f'Output: {output_path}')


if __name__ == '__main__':
    main()
