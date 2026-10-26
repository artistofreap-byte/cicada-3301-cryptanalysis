# Test Documentation

## 1. Purpose

This document records the testing procedures for the Tenviora Technologies experimental Gematria Primus-inspired cryptanalysis engine.

## 2. Test Environment

- Operating system: Windows
- Development environment: PyCharm
- Python interpreter: Python 3.14, as shown in the development environment

## 3. Command-Line Help Test

Command:

```powershell
python script1.py --help
```

Observed result: The program displayed its command-line usage and available options.

Status: Passed, based on observed output.

## 4. Built-In Self-Tests

Command:

```powershell
python script1.py --test
```

Observed result: The author reported that all built-in self-tests passed.

Status: Passed, as reported by the author.

## 5. Scope of Testing

These checks confirm that the help output is available and that the built-in tests reportedly pass. They do not independently prove that every algorithmic component is correct.

## 6. Recommended Additional Tests

- Verify character mappings against a trusted alphabet specification.
- Test empty, malformed, and unexpected inputs.
- Test numerical key parsing and invalid key values.
- Test transposition behavior across different column counts.
- Test Fibonacci parameter boundaries.
- Confirm that report files are generated correctly.
- Compare transformations against independently calculated test vectors.

## 7. Research Limitations

The default key is artificial. Passing these tests does not establish that the engine decrypts authentic Cicada 3301 ciphertext or recovers a verified plaintext.

## 8. Updating This Record

Record the date, code version, exact command, expected result, actual result, and any failures when additional tests are performed.