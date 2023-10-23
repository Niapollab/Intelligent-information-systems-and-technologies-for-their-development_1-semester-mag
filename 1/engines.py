from experta import Fact, KnowledgeEngine, Rule
from facts import BloodDonorFact, BloodRecipientFact, BloodTransfusionFact, BloodType
from models import TransfusionResult
from typing import Optional


class BloodTransfusionEngine(KnowledgeEngine):
    RULES = (
        # Universal donor
        BloodDonorFact(type=BloodType.O) & BloodRecipientFact() |

        # Donor for: A, AB
        BloodDonorFact(type=BloodType.A) & (BloodRecipientFact(type=BloodType.A)
                                            | BloodRecipientFact(type=BloodType.AB)) |

        # Donor for: B, AB
        BloodDonorFact(type=BloodType.B) & (BloodRecipientFact(type=BloodType.B)
                                            | BloodRecipientFact(type=BloodType.AB)) |

        # Donor for: AB
        BloodDonorFact(type=BloodType.AB) & BloodRecipientFact(type=BloodType.AB)
    )

    @Rule(RULES)
    def is_allowed(self) -> Optional[Fact]:
        return self.declare(BloodTransfusionFact(is_allowed=True))

    @Rule(~RULES)
    def is_not_allowed(self) -> Optional[Fact]:
        return self.declare(BloodTransfusionFact(is_allowed=False))

    @property
    def result(self) -> TransfusionResult:
        if len(self.facts) < 1:
            return TransfusionResult.UNDEFINED

        last_fact = self.facts[self.facts.last_index - 1]

        if not isinstance(last_fact, BloodTransfusionFact):
            return TransfusionResult.UNDEFINED

        return TransfusionResult.ALLOWED if last_fact['is_allowed'] else TransfusionResult.NOT_ALLOWED


    @staticmethod
    def build(donor: BloodType, recipient: BloodType) -> 'BloodTransfusionEngine':
        engine = BloodTransfusionEngine()
        engine.reset()

        engine.declare(BloodDonorFact(type=donor))
        engine.declare(BloodRecipientFact(type=recipient))

        return engine
