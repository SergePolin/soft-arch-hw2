import argparse
from app.pipeline import process_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video processing with filters")
    parser.add_argument("--source", default=0, help="Path to video file or camera index (default: 0)")
    parser.add_argument("--filters", nargs='+', choices=['grayscale', 'mirror', 'resize', 'edge'],
                        help="Filters to apply (default: all)")
    args = parser.parse_args()

    process_video(args.source, args.filters)
