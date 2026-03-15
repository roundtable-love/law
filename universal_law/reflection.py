from ._base import Source, UniversalLaw


class Reflection(UniversalLaw):
    name = "Law of Reflection"
    code = "SYSTEM.state == ROOT.clarity"
    machine_ir = "ASSERT: TREATMENT_GIVEN == TREATMENT_RECEIVED; ASSERT: WHAT_IS_SOWN == WHAT_IS_REAPED"
    uid = "quotes-R"
    sources = (
        Source(
            quote="With the measure a man measures, it is measured to him.",
            source="Babylonian Talmud, Sotah 8b",
            ref="https://www.sefaria.org/Sotah.8b",
        ),
        Source(
            quote="One who spits at heaven only soils oneself.",
            source="Chinese proverb",
            ref="https://en.wikiquote.org/wiki/Chinese_proverbs",
        ),
        Source(
            quote="What you do not wish for yourself, do not do to others.",
            source="Confucius, Analects 15:23",
            ref="https://en.wikisource.org/wiki/The_Chinese_Classics/Volume_1/Confucian_Analects",
        ),
        Source(
            quote="If with an impure mind a person speaks or acts, suffering follows him. If with a pure mind a person speaks or acts, happiness follows him like his never-departing shadow.",
            source="Dhammapada 1-2",
            ref="https://en.wikisource.org/wiki/Dhammapada_(Muller)",
        ),
        Source(
            quote="For whatsoever a man soweth, that shall he also reap.",
            source="Galatians 6:7",
            ref="https://en.wikisource.org/wiki/Bible_(King_James)/Galatians#Chapter_6",
        ),
        Source(
            quote="As you sow, so shall you reap.",
            source="Guru Granth Sahib",
            ref="https://en.wikiquote.org/wiki/Guru_Granth_Sahib",
        ),
        Source(
            quote="What goes around, comes around.",
            source="Justin Timberlake, What Goes Around... Comes Around",
            ref="https://genius.com/Justin-timberlake-what-goes-around-comes-around-lyrics",
        ),
        Source(
            quote="Do unto others as you would have them do unto you.",
            source="Luke 6:31",
            ref="https://en.wikisource.org/wiki/Bible_(King_James)/Luke#Chapter_6",
        ),
        Source(
            quote="Now don't you understand, man, universal law? What you throw out comes back to you, star. Never underestimate those who you scar. Cause karma, karma, karma comes back to you hard.",
            source="Ms. Lauryn Hill, Lost Ones",
            ref="https://genius.com/Ms-lauryn-hill-lost-ones-lyrics",
        ),
        Source(
            quote="Whoever does an atom's weight of good will see it, and whoever does an atom's weight of evil will see it.",
            source="Qur'an 99:7-8",
            ref="https://en.wikisource.org/wiki/The_Holy_Qur%27an_(Maulana_Muhammad_Ali)/99._The_Quaking",
        ),
        Source(
            quote="Good thoughts, good words, good deeds.",
            source="Zoroastrian Scripture, Avesta",
            ref="https://en.wikisource.org/wiki/Zend_Avesta",
        ),
    )
