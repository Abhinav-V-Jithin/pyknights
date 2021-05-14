from logic import *


AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = And(AKnight, AKnave)

knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence1_a = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentence1_b = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # TODO
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, sentence1_a),
    Implication(AKnave, Not(sentence1_a)),
    Implication(BKnight, sentence1_b),
    Implication(BKnave, Not(sentence1_b))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

sentence_a = Or(AKnight, AKnave)
sentence_b = And(AKnight, CKnave)
sentence_c = AKnight


knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, sentence_a),
    Implication(AKnave, Not(sentence_a)),
    Implication(BKnight, sentence_b),
    Implication(BKnave, Not(sentence_b)),
    Implication(CKnight, sentence_c),
    Implication(CKnave, Not(sentence_c))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
