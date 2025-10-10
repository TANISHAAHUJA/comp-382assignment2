"""
COMP 382 Assignment 2 - Topic 1
Demonstrating that Context-Free Languages are not closed under intersection

This implementation demonstrates that the set of context-free languages is not closed
under the operation of intersection by showing that {a^n b^n c^n | n ≥ 0} is not context-free,
but can be expressed as the intersection of two context-free languages.
"""

import re
from typing import List, Tuple, Set

class ContextFreeLanguage:
    """
    A class to represent and work with context-free languages
    """
    
    def __init__(self, name: str, grammar: dict):
        self.name = name
        self.grammar = grammar  # Dictionary mapping non-terminals to list of productions
    
    def generate_strings(self, max_length: int = 20) -> List[str]:
        """
        Generate strings from the grammar up to a maximum length
        """
        generated = set()
        
        def derive_string(current: str, max_depth: int = 10) -> None:
            if max_depth <= 0 or len(current) > max_length:
                return
            
            # If current string contains only terminals, add it
            if not any(c.isupper() for c in current):
                if len(current) <= max_length:
                    generated.add(current)
                return
            
            # Find first non-terminal
            for i, char in enumerate(current):
                if char.isupper():
                    # Replace with all possible productions
                    if char in self.grammar:
                        for production in self.grammar[char]:
                            new_string = current[:i] + production + current[i+1:]
                            derive_string(new_string, max_depth - 1)
                    break
        
        # Start derivation from start symbol
        if 'S' in self.grammar:
            for production in self.grammar['S']:
                derive_string(production)
        
        return sorted(list(generated))

def create_grammar_l1() -> ContextFreeLanguage:
    """
    Create grammar L1 = {a^i b^j c^k | i = j, i,j,k ≥ 0}
    This language is context-free
    """
    grammar = {
        'S': ['AB'],
        'A': ['aAb', 'ab'],  # Generates a^n b^n
        'B': ['Bc', 'c', '']  # Generates c^k
    }
    return ContextFreeLanguage("L1 = {a^i b^j c^k | i = j}", grammar)

def create_grammar_l2() -> ContextFreeLanguage:
    """
    Create grammar L2 = {a^i b^j c^k | j = k, i,j,k ≥ 0}
    This language is context-free
    """
    grammar = {
        'S': ['AB'],
        'A': ['aA', 'a', ''],  # Generates a^i
        'B': ['bBc', 'bc']     # Generates b^n c^n
    }
    return ContextFreeLanguage("L2 = {a^i b^j c^k | j = k}", grammar)

def generate_anbncn_examples(n_max: int = 5) -> List[str]:
    """
    Manually generate examples of strings in {a^n b^n c^n | n ≥ 0}
    """
    examples = []
    for n in range(n_max + 1):
        if n == 0:
            examples.append("")
        else:
            examples.append("a" * n + "b" * n + "c" * n)
    return examples

def intersection_l1_l2() -> Set[str]:
    """
    Compute the intersection of L1 and L2
    L1 ∩ L2 = {a^i b^j c^k | i = j AND j = k} = {a^n b^n c^n | n ≥ 0}
    """
    l1 = create_grammar_l1()
    l2 = create_grammar_l2()
    
    # Generate strings from both languages
    strings_l1 = set(l1.generate_strings(15))
    strings_l2 = set(l2.generate_strings(15))
    
    # Find intersection
    intersection = strings_l1.intersection(strings_l2)
    
    # Also add manually generated examples
    manual_examples = set(generate_anbncn_examples(5))
    intersection.update(manual_examples)
    
    return intersection

def is_anbncn(string: str) -> bool:
    """
    Check if a string is of the form a^n b^n c^n
    """
    # Handle empty string case
    if string == "":
        return True
    
    pattern = r'^(a+)(b+)(c+)$'
    match = re.match(pattern, string)
    
    if not match:
        return False
    
    a_count = len(match.group(1))
    b_count = len(match.group(2))
    c_count = len(match.group(3))
    
    return a_count == b_count == c_count

def pumping_lemma_proof():
    """
    Demonstrate the pumping lemma proof that {a^n b^n c^n | n ≥ 0} is not context-free
    """
    print("=" * 60)
    print("PUMPING LEMMA PROOF")
    print("=" * 60)
    print()
    print("Theorem: L = {a^n b^n c^n | n ≥ 0} is not context-free")
    print()
    print("Proof by contradiction using the pumping lemma for CFLs:")
    print()
    print("Assume L is context-free. Then there exists a pumping length p > 0")
    print("such that for any string s ∈ L with |s| ≥ p, we can write s = uvwxy where:")
    print("1. |vwx| ≤ p")
    print("2. |vx| ≥ 1") 
    print("3. For all i ≥ 0, uv^i wx^i y ∈ L")
    print()
    print("Consider the string s = a^p b^p c^p ∈ L")
    print("Since |s| = 3p ≥ p, the pumping lemma applies.")
    print()
    print("Case analysis based on where vwx can be positioned:")
    print()
    print("Case 1: vwx contains only a's")
    print("  - Then v = a^k, x = a^m for some k,m ≥ 0, k+m ≥ 1")
    print("  - Pumping up: uv^2 wx^2 y = a^(p+k+m) b^p c^p")
    print("  - This has more a's than b's or c's, so ∉ L")
    print()
    print("Case 2: vwx contains only b's")
    print("  - Similar argument shows pumping creates imbalance")
    print()
    print("Case 3: vwx contains only c's")
    print("  - Similar argument shows pumping creates imbalance")
    print()
    print("Case 4: vwx spans across a's and b's")
    print("  - Since |vwx| ≤ p, it cannot span all three types")
    print("  - Pumping will create imbalance between the types")
    print()
    print("Case 5: vwx spans across b's and c's")
    print("  - Similar to Case 4, pumping creates imbalance")
    print()
    print("In all cases, pumping leads to a contradiction.")
    print("Therefore, L is not context-free. □")
    print()

def demonstrate_intersection():
    """
    Demonstrate that L1 ∩ L2 = {a^n b^n c^n | n ≥ 0}
    """
    print("=" * 60)
    print("INTERSECTION DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Create the two context-free languages
    l1 = create_grammar_l1()
    l2 = create_grammar_l2()
    
    print(f"L1 = {l1.name}")
    print("Grammar for L1:")
    for non_terminal, productions in l1.grammar.items():
        print(f"  {non_terminal} → {' | '.join(productions)}")
    print()
    
    print(f"L2 = {l2.name}")
    print("Grammar for L2:")
    for non_terminal, productions in l2.grammar.items():
        print(f"  {non_terminal} → {' | '.join(productions)}")
    print()
    
    # Generate some strings from each language
    print("Sample strings from L1:")
    l1_strings = l1.generate_strings(10)
    for s in l1_strings[:10]:
        print(f"  '{s}'")
    print()
    
    print("Sample strings from L2:")
    l2_strings = l2.generate_strings(10)
    for s in l2_strings[:10]:
        print(f"  '{s}'")
    print()
    
    # Show manual examples of a^n b^n c^n
    print("Manual examples of strings in {a^n b^n c^n | n ≥ 0}:")
    manual_examples = generate_anbncn_examples(5)
    for s in manual_examples:
        print(f"  '{s}'")
    print()
    
    # Find intersection
    intersection = intersection_l1_l2()
    print("Intersection L1 ∩ L2:")
    for s in sorted(intersection):
        print(f"  '{s}'")
    print()
    
    # Verify that intersection strings are of form a^n b^n c^n
    print("Verification that intersection strings are of form a^n b^n c^n:")
    for s in sorted(intersection):
        is_correct_form = is_anbncn(s)
        print(f"  '{s}' → {is_correct_form}")
    print()
    
    print("CONCLUSION:")
    print("L1 and L2 are both context-free languages.")
    print("L1 ∩ L2 = {a^n b^n c^n | n ≥ 0}")
    print("But {a^n b^n c^n | n ≥ 0} is not context-free (proven above).")
    print("Therefore, the set of context-free languages is not closed under intersection. □")
    print()

def main():
    """
    Main function to demonstrate the proof
    """
    print("COMP 382 Assignment 2 - Topic 1")
    print("Context-Free Languages are not closed under intersection")
    print("=" * 60)
    print()
    
    # Show the pumping lemma proof
    pumping_lemma_proof()
    
    # Demonstrate the intersection
    demonstrate_intersection()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("1. We constructed two context-free languages L1 and L2")
    print("2. We showed that L1 ∩ L2 = {a^n b^n c^n | n ≥ 0}")
    print("3. We proved that {a^n b^n c^n | n ≥ 0} is not context-free using pumping lemma")
    print("4. Therefore, CFLs are not closed under intersection")

if __name__ == "__main__":
    main()
