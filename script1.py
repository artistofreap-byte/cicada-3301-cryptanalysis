
#!/usr/bin/env python3
"""
TENVIORA TECHNOLOGIES
Experimental Gematria Primus-Inspired Cryptanalysis Engine

Research disclaimer:
The default key is artificial, not a recovered Cicada 3301 key.
This program does not claim to solve Cicada 3301.
Ciphertext provenance and cipher methods require independent verification.
"""

import argparse
from pathlib import Path

# ============================================================
# 1. GEMATRIA PRIMUS ALPHABET
# ============================================================

GP_ALPHABET = [
    "F", "U", "TH", "O", "R", "C", "G", "W", "H", "N",
    "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M",
    "L", "NG", "D", "OE", "A", "AE", "Y", "IA", "EA"
]

MODULUS = len(GP_ALPHABET)

CHAR_TO_INDEX = {
    token: index
    for index, token in enumerate(GP_ALPHABET)
}

# Artificial demonstration key, NOT a recovered Cicada key.
TEST_KEY = list(range(MODULUS))

TARGET_LEXICON = [
    "SYNTHE", "THE", "WEB", "WELCOME",
    "WISDOM", "PILGRIM", "REASON", "KNOW"
]

IGNORED_CHARACTERS = set(" \t\r\n-.,;:!?_'\"")


# ============================================================
# 2. SAMPLE CIPHERTEXT
# ============================================================

DEFAULT_CIPHERTEXT = (
    "NGEOYPOHEEAWIRIHUHHYNXBJGJPUNEAFNIEDYBGRDBJYOMIFTJTHOERGPWNIESTBEMLNGDOEAEIAEREPNWO"
    "EMNGEPNEIBENCTHFLLMREAADNCWREAARAEORALBSGGBTHYDLWOCTHYDTHOEUTHDESPRRTHNOERGPWNIESTB"
    "EMLNGDOEAEIAEAFUTHORDHNEIJPXSTBEMLNGAEIAEAFUTHORKJIHGFDSAZXCVBNMTHOERGPWNIESTBEMLNG"
    "DOEAEIAEREPNWOEMNGEPNEIBENCTHFLLMREAADNCWREAARAEORALBSGGBTHYDLWOCTHYDTHOEUTHDESPRRT"
    "HNOERGPWNIESTBEMLNGDOEAEIAEAFUTHORDHNEIJPXSTBEMLNGAEIAEAFUTHORKJIHGFDSAZ"
)


# ============================================================
# 3. FIBONACCI STREAM
# ============================================================

def generate_fibonacci_stream(length, seed1=3, seed2=5):
    """Generate a Fibonacci-like stream modulo the alphabet size."""

    if length < 0:
        raise ValueError("Length cannot be negative.")

    if length == 0:
        return []

    fib = [seed1 % MODULUS]

    if length == 1:
        return fib

    fib.append(seed2 % MODULUS)

    while len(fib) < length:
        fib.append((fib[-1] + fib[-2]) % MODULUS)

    return fib


# ============================================================
# 4. TOKEN PARSING
# ============================================================

def parse_input_indices(content):
    """
    Convert text into alphabet indices using greedy two-character
    matching. Concatenated token labels can be ambiguous.
    """

    indices = []
    position = 0
    content = content.upper()

    while position < len(content):
        char = content[position]

        if char in IGNORED_CHARACTERS:
            position += 1
            continue

        pair = content[position:position + 2]

        if pair in CHAR_TO_INDEX:
            indices.append(CHAR_TO_INDEX[pair])
            position += 2
        elif char in CHAR_TO_INDEX:
            indices.append(CHAR_TO_INDEX[char])
            position += 1
        else:
            position += 1

    return indices


def parse_custom_key(key_text):
    """Parse a comma-separated numerical key."""

    if key_text is None:
        return None

    try:
        values = [
            int(part.strip())
            for part in key_text.split(",")
            if part.strip()
        ]
    except ValueError as exc:
        raise ValueError(
            "Key must be comma-separated integers, e.g. 0,1,2,3,4"
        ) from exc

    if not values:
        raise ValueError("The custom key cannot be empty.")

    return values


# ============================================================
# 5. COLUMN TRANSPOSITION
# ============================================================

def transpose_indices(indices, num_cols):
    """Read a complete rectangular grid column by column."""

    if num_cols <= 0:
        raise ValueError("Number of columns must be positive.")

    if not indices or len(indices) % num_cols != 0:
        return indices.copy()

    num_rows = len(indices) // num_cols

    grid = [
        indices[row * num_cols:(row + 1) * num_cols]
        for row in range(num_rows)
    ]

    return [
        grid[row][col]
        for col in range(num_cols)
        for row in range(num_rows)
    ]


# ============================================================
# 6. DECODING AND WORD MATCHES
# ============================================================

def decode_indices(indices):
    """Convert numerical indices back into alphabet tokens."""

    return "".join(
        GP_ALPHABET[index % MODULUS]
        for index in indices
    )


def find_lexicon_matches(candidate):
    """Find configured target strings appearing in a candidate."""

    return [
        word for word in TARGET_LEXICON
        if word in candidate
    ]


# ============================================================
# 7. EXPERIMENTAL DECRYPTION METHODS
# ============================================================

def decrypt_candidates(tokens, key, fib_stream, num_cols=5):
    """Run two experimental methods and a repeating-key baseline."""

    if not key:
        raise ValueError("The key cannot be empty.")

    if any(not isinstance(value, int) for value in key):
        raise ValueError("All key values must be integers.")

    working_tokens = transpose_indices(tokens, num_cols)

    if len(fib_stream) < len(working_tokens):
        raise ValueError("Fibonacci stream is too short.")

    candidates = {}

    # METHOD 1: INTERLOCKING FIBONACCI KEY INDEX
    result_mode1 = []

    for index, cipher_value in enumerate(working_tokens):
        fib_offset = fib_stream[index]
        key_index = (index + fib_offset) % len(key)
        key_shift = key[key_index] % MODULUS
        total_shift = (key_shift - fib_offset) % MODULUS
        result_mode1.append((cipher_value - total_shift) % MODULUS)

    candidates["Interlocking Fibonacci Key Index"] = (
        decode_indices(result_mode1)
    )

    # METHOD 2: CIPHERTEXT FEEDBACK PROGRESSION
    result_mode2 = []
    running_modifier = 0

    for index, cipher_value in enumerate(working_tokens):
        fib_offset = fib_stream[index]
        key_index = (index + running_modifier) % len(key)
        key_shift = key[key_index] % MODULUS
        total_shift = (key_shift - fib_offset) % MODULUS
        result_mode2.append((cipher_value - total_shift) % MODULUS)

        running_modifier = (
            running_modifier + cipher_value
        ) % len(key)

    candidates["Value-Based Ciphertext Feedback Progression"] = (
        decode_indices(result_mode2)
    )

    # BASELINE: REPEATING KEY SEQUENCE
    result_baseline = []

    for index, cipher_value in enumerate(working_tokens):
        key_shift = key[index % len(key)] % MODULUS
        fib_offset = fib_stream[index]
        total_shift = (key_shift - fib_offset) % MODULUS
        result_baseline.append((cipher_value - total_shift) % MODULUS)

    candidates["Repeating-Key Baseline"] = (
        decode_indices(result_baseline)
    )

    return candidates


# ============================================================
# 8. MASTER RESEARCH ENGINE
# ============================================================

def run_master_engine(
    ciphertext=DEFAULT_CIPHERTEXT,
    key=None,
    num_cols=5,
    seed1=3,
    seed2=5,
    report_path="master_report.txt"
):
    """Run analysis, print candidate outputs, and save a report."""

    using_test_key = key is None
    active_key = TEST_KEY.copy() if using_test_key else key.copy()

    if not active_key:
        raise ValueError("The key cannot be empty.")

    tokens = parse_input_indices(ciphertext)

    fib_stream = generate_fibonacci_stream(
        len(tokens),
        seed1=seed1,
        seed2=seed2
    )

    candidates = decrypt_candidates(
        tokens,
        active_key,
        fib_stream,
        num_cols=num_cols
    )

    lines = [
        "=" * 72,
        "TENVIORA TECHNOLOGIES",
        "EXPERIMENTAL GEMATRIA PRIMUS CRYPTANALYSIS REPORT",
        "=" * 72,
        f"Input characters: {len(ciphertext)}",
        f"Parsed tokens: {len(tokens)}",
        f"Transposition columns: {num_cols}",
        f"Fibonacci seed 1: {seed1}",
        f"Fibonacci seed 2: {seed2}",
        f"Key length: {len(active_key)}",
        (
            "Key type: ARTIFICIAL TEST KEY"
            if using_test_key
            else "Key type: USER-SUPPLIED NUMERICAL KEY"
        ),
        "",
        "IMPORTANT RESEARCH LIMITATIONS:",
        "This output is NOT verified Cicada 3301 plaintext.",
        "The ciphertext source and key have not been independently verified.",
        "Greedy multi-character token parsing may be ambiguous.",
        "The tested formulas are experimental hypotheses.",
        "",
    ]

    for method, candidate in candidates.items():
        matches = find_lexicon_matches(candidate)

        lines.extend([
            "-" * 72,
            f"METHOD: {method}",
            f"Target-word matches: {len(matches)}",
            (
                "Matched words: " + ", ".join(matches)
                if matches else "Matched words: None"
            ),
            "",
            "CANDIDATE OUTPUT:",
            candidate,
            "",
        ])

    lines.extend([
        "-" * 72,
        "VALIDATION NOTES",
        "Word matches alone do not prove a successful decryption.",
        "Independent plaintext evidence and a documented cipher",
        "hypothesis are required to verify any result.",
        "=" * 72,
    ])

    report = "\n".join(lines)
    print(report)

    if report_path:
        output_path = Path(report_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"\nReport saved to: {output_path.resolve()}")

    return report


# ============================================================
# 9. BUILT-IN SELF-TESTS
# ============================================================

def run_self_tests():
    """Verify core functions against expected results."""

    assert len(GP_ALPHABET) == 29
    assert generate_fibonacci_stream(0) == []
    assert generate_fibonacci_stream(1) == [3]
    assert generate_fibonacci_stream(5) == [3, 5, 8, 13, 21]

    assert parse_input_indices("F U TH") == [
        CHAR_TO_INDEX["F"],
        CHAR_TO_INDEX["U"],
        CHAR_TO_INDEX["TH"]
    ]

    assert transpose_indices(
        [0, 1, 2, 3, 4, 5], 2
    ) == [0, 2, 4, 1, 3, 5]

    assert transpose_indices(
        [0, 1, 2], 2
    ) == [0, 1, 2]

    assert decode_indices([0, 1, 2]) == "FUTH"
    assert parse_custom_key("0,1,2") == [0, 1, 2]
    assert parse_custom_key(None) is None

    print("All self-tests passed.")


# ============================================================
# 10. COMMAND-LINE INTERFACE
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Experimental Gematria Primus-inspired cryptanalysis"
    )

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run self-tests and exit."
    )

    parser.add_argument(
        "--report",
        default="master_report.txt",
        help="Path to save the report."
    )

    parser.add_argument(
        "--columns",
        type=int,
        default=5,
        help="Number of transposition columns."
    )

    parser.add_argument(
        "--seed1",
        type=int,
        default=3,
        help="First Fibonacci starting value."
    )

    parser.add_argument(
        "--seed2",
        type=int,
        default=5,
        help="Second Fibonacci starting value."
    )

    parser.add_argument(
        "--key",
        type=str,
        default=None,
        help="Optional comma-separated numerical key, e.g. 0,1,2,3,4."
    )

    args = parser.parse_args()

    if args.test:
        run_self_tests()
        return

    if args.columns <= 0:
        parser.error("--columns must be a positive integer.")

    try:
        custom_key = parse_custom_key(args.key)

        run_master_engine(
            key=custom_key,
            num_cols=args.columns,
            seed1=args.seed1,
            seed2=args.seed2,
            report_path=args.report
        )
    except (ValueError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
