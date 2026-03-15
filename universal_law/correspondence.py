from ._base import Source, UniversalLaw


class Correspondence(UniversalLaw):
    name = "Law of Correspondence"
    code = "ROOT.macro == ROOT.micro"
    machine_ir = "ASSERT: PATTERN.above == PATTERN.below; ASSERT: PATTERN.within == PATTERN.without"
    uid = "quotes-CO"
    sources = (
        Source(
            quote="Tat tvam asi. (That art thou.)",
            source="Chandogya Upanishad 6.8.7",
            ref="https://en.wikisource.org/wiki/Chandogya_Upanishad",
        ),
        Source(
            quote="That which is above is like that which is below, and that which is below is like that which is above, to accomplish the miracle of the one thing.",
            source="Hermes Trismegistus, Emerald Tablet",
            ref="https://en.wikisource.org/wiki/The_Emerald_Tablet_of_Hermes",
        ),
        Source(
            quote="A single hair casts its shadow.",
            source="Japanese proverb",
            ref="https://en.wikiquote.org/wiki/Japanese_proverbs",
        ),
        Source(
            quote="The microcosm reflects the macrocosm.",
            source="Kabbalistic teaching (Adam Kadmon)",
            ref="https://en.wikipedia.org/wiki/Adam_Kadmon",
        ),
        Source(
            quote="As above, so below.",
            source="Kygo & Imagine Dragons, Born to Be Yours",
            ref="https://genius.com/Kygo-and-imagine-dragons-born-to-be-yours-lyrics",
        ),
        Source(
            quote="Man follows Earth. Earth follows Heaven. Heaven follows the Tao. The Tao follows what is natural.",
            source="Lao Tzu, Tao Te Ching 25",
            ref="https://en.wikisource.org/wiki/Tao_Te_Ching_(Legge)/Chapter_25",
        ),
        Source(
            quote="Thy will be done in earth, as it is in heaven.",
            source="Matthew 6:10",
            ref="https://en.wikisource.org/wiki/Bible_(King_James)/Matthew#Chapter_6",
        ),
        Source(
            quote="For as he thinketh in his heart, so is he.",
            source="Proverbs 23:7",
            ref="https://en.wikisource.org/wiki/Bible_(King_James)/Proverbs#Chapter_23",
        ),
        Source(
            quote="We will show them Our signs in the horizons and within themselves until it becomes clear to them that it is the truth.",
            source="Qur'an 41:53",
            ref="https://en.wikisource.org/wiki/The_Holy_Qur%27an_(Maulana_Muhammad_Ali)/41._Ha_Mim",
        ),
    )
