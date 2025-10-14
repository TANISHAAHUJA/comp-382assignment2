# COMP 382 Assignment 2 - Topic 1

## Context-Free Languages are not closed under intersection

### Group Members
- Ritu Randhawa, Liam Maarhuis, Tanisha Ahuja, Natasha, Maundu

### Overview
This project demonstrates that the set of context-free languages is not closed under the operation of intersection. We prove this by showing that the language {a^n b^n c^n | n ≥ 0} is not context-free, but can be expressed as the intersection of two context-free languages.

### Mathematical Proof

The complete mathematical proof is provided in `proof.tex` (LaTeX format). The proof includes:

1. **Construction of two context-free languages L1 and L2**
2. **Demonstration that L1 ∩ L2 = {a^n b^n c^n | n ≥ 0}**
3. **Proof using pumping lemma that {a^n b^n c^n | n ≥ 0} is not context-free**

To compile the LaTeX document:
```bash
pdflatex proof.tex
```

### Implementation

The Python implementation (`assignment2_topic1.py`) includes:

1. **ContextFreeLanguage class**: Represents and generates strings from CFGs
2. **Grammar definitions**: Implements L1 and L2 as described above
3. **Intersection computation**: Finds common strings between L1 and L2
4. **Pumping lemma demonstration**: Shows the mathematical proof
5. **Verification**: Confirms intersection strings are of form a^n b^n c^n

### Running the Code

```bash
python assignment2_topic1.py
```

### Key Results

The program demonstrates:
- L1 and L2 are both context-free languages
- Their intersection contains strings like: "", "abc", "aabbcc", "aaabbbccc", etc.
- All intersection strings follow the pattern a^n b^n c^n
- This pattern is not context-free (proven by pumping lemma)
- Therefore, CFLs are not closed under intersection

### Conclusion

We have successfully demonstrated that:
1. Two context-free languages can have a non-context-free intersection
2. The specific example {a^n b^n c^n | n ≥ 0} serves as a counterexample
3. This proves that the set of context-free languages is not closed under intersection

### References

- Hopcroft, Motwani, Ullman: "Introduction to Automata Theory, Languages, and Computation"
- Sipser: "Introduction to the Theory of Computation"
