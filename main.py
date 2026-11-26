#!/usr/bin/env python3
"""Generate an honest out-of-office auto-reply for Make.fun challenge."""

import os


def generate_out_of_office():
    """Create a painfully honest but polite single-sentence out-of-office message."""
    return (
        "Currently out of office with zero inbox & depleted energy, so please be patient as I'll return refreshed soon."
    )


def main():
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # Generate the message
    message = generate_out_of_office()
    
    # Write to file
    output_path = "output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(message)
    
    print(f"Out-of-office message written to {output_path}")
    print(f"Character count: {len(message)}")


if __name__ == "__main__":
    main()