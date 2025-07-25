# Sumcheck Protocol - Python Implementation

A Python implementation of the sumcheck protocol, a fundamental interactive proof system used in cryptography and computational complexity theory.

1. Prover sends the evaluation of the polynomial ✅
2. Verifier evaluates over the boolean hypercube
3. Verifier chooses a random field element and sends to prover, which then "fixes" variable a
4. Iteratvely, the prover and verifier go through this until all of the variables are
   "bound". 
5. Lastly, the verifier performs one evaluation of the full polynomial


## Overview

The sumcheck protocol is an interactive proof between a **Prover** and a **Verifier** that allows the Prover to convince the Verifier that a claimed sum over a Boolean hypercube is correct. Specifically, given a multivariate polynomial `g(x₁, x₂, ..., xₙ)` over a finite field, the protocol verifies:

```
S = Σ g(x₁, x₂, ..., xₙ)
```

where the sum is taken over all points `(x₁, x₂, ..., xₙ) ∈ {0,1}ⁿ`.

## How It Works

The protocol proceeds in rounds:

1. **Initial Claim**: Prover sends the claimed sum `S` to the Verifier
2. **Iterative Reduction**: For each variable `xᵢ`:
   - Prover sends a univariate polynomial obtained by fixing previous variables and summing over remaining Boolean assignments
   - Verifier checks consistency and sends back a random field element
   - Prover "fixes" the current variable to this random value
3. **Final Verification**: After all variables are bound, the Verifier performs one final polynomial evaluation to verify correctness

## Project Structure

```
sumcheck/
├── field_element/          # Finite field arithmetic implementation
│   ├── __init__.py
│   └── field_element.py
├── polynomial/             # Multivariate polynomial operations
│   ├── __init__.py
│   └── polynomial.py
├── term/                   # Individual polynomial terms
│   ├── __init__.py
│   └── term.py
├── prover/                 # Prover implementation
│   ├── __init__.py
│   └── prover.py
├── verifier/               # Verifier implementation
│   └── verifier.py
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_field_element.py
│   ├── test_polynomial.py
│   ├── test_prover.py
│   └── test_term.py
├── main.py                 # Example usage (currently commented out)
├── LICENSE
└── README.md
```

## Core Components

### FieldElement
Implements arithmetic operations over finite fields (modular arithmetic).

### Polynomial
Represents multivariate polynomials with support for:
- Evaluation at specific points
- Variable binding and reduction
- Boolean hypercube operations

### Term
Individual polynomial terms with coefficients, variable numbers, and exponents.

### Prover
Implements the Prover's role in the sumcheck protocol:
- Generates Boolean hypercube points
- Computes sums over hypercubes
- Creates univariate polynomials for each round

### Verifier
Implements the Verifier's role (currently in development).

## Current Status

⚠️ **Work in Progress** ⚠️

This implementation is currently under active development. Key areas being worked on:

- [ ] Complete Verifier implementation
- [ ] Interactive protocol execution
- [ ] Error handling and edge cases
- [ ] Performance optimizations
- [ ] Comprehensive documentation
- [ ] Additional test coverage

## Usage

Currently, the main execution is commented out in `main.py`. The individual components can be imported and used separately:

```python
from field_element import FieldElement
from polynomial import Polynomial
from term import Term
from prover import Prover

# Example usage (when fully implemented)
```

## Running Tests

```bash
python -m pytest tests/
```

## Mathematical Background

The sumcheck protocol is notable for:
- **Efficiency**: Reduces verification of exponentially large sums to polynomial-time operations
- **Generality**: Works for any low-degree multivariate polynomial
- **Applications**: Used in probabilistically checkable proofs (PCPs), succinct arguments, and zero-knowledge proofs

## Contributing

This is an educational/research implementation. Contributions and improvements are welcome, particularly in:
- Completing the Verifier implementation
- Adding more comprehensive tests
- Performance optimizations
- Documentation improvements

## License

See LICENSE file for details.

---

*This implementation is intended for educational and research purposes. The sumcheck protocol is a foundational building block in modern cryptographic proof systems.*
