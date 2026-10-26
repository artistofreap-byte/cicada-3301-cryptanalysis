# Research Methodology

## 1. Research Objective

Develop and evaluate an experimental Python engine inspired by Gematria Primus character mappings and cryptanalysis concepts.

The project explores configurable parameters and repeatable testing. It does not claim to have solved Cicada 3301.

## 2. Alphabet Representation

The program defines a `GP_ALPHABET` list containing character groups, including entries such as `TH`, `EO`, `NG`, `OE`, and `AE`.

These entries should be validated against the intended alphabet specification before drawing conclusions from any transformation.

## 3. Configurable Parameters

The program exposes the following command-line options:

- `--columns`: Number of transposition columns.
- `--seed1`: First Fibonacci starting value.
- `--seed2`: Second Fibonacci starting value.
- `--key`: Optional comma-separated numerical key.
- `--report`: Output path for a report.
- `--test`: Run the built-in self-tests.

Refer to `python script1.py --help` for the available options.

## 4. Experimental Procedure

1. Configure the experiment parameters.
2. Run the program using the selected options.
3. Record the inputs and generated outputs.
4. Run the built-in self-tests.
5. Review the results for consistency and reproducibility.
6. Independently verify any proposed cryptographic interpretation.

## 5. Testing and Validation

The author reports that the built-in self-tests passed.

These tests demonstrate only that the implemented checks passed. They do not independently establish the correctness of the cryptographic approach or demonstrate recovery of an authentic Cicada 3301 plaintext.

## 6. Limitations

- The default key is artificial.
- The authenticity and provenance of any test ciphertext must be established separately.
- The implemented transformations require independent review and validation.
- A plausible-looking output is not sufficient evidence of successful decryption.

## 7. Reproducibility

Record the script version, Python version, input data, parameter values, test results, and output files for each experiment.

## 8. Research Integrity

Document unsuccessful as well as successful experiments. Distinguish verified findings from hypotheses, assumptions, and exploratory results.