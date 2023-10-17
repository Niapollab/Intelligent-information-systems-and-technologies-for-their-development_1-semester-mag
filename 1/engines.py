from experta import Fact, KnowledgeEngine, Rule
from facts import BloodDonorFact, BloodRecipientFact, BloodTransfusionFact, BloodType
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

    @staticmethod
    def build(donor: BloodType, recipient: BloodType) -> 'BloodTransfusionEngine':
        engine = BloodTransfusionEngine()
        engine.reset()

        engine.declare(BloodDonorFact(type=donor))
        engine.declare(BloodRecipientFact(type=recipient))

        return engine
