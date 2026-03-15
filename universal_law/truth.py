from ._base import Source, UniversalLaw


class Truth(UniversalLaw):
    name = "Law of Truth"
    code = "TRUTH.persistence == INF"
    machine_ir = "ASSERT: TRUTH.persistence == INFINITE; ASSERT: FALSEHOOD.persistence == TRANSIENT; ASSERT: TRUTH.triumph == TRUE"
    uid = "quotes-T"
    sources = (
        Source(
            quote="The truth is like a lion; you don't have to defend it. Let it loose; it will defend itself.",
            source="Augustine of Hippo (attributed)",
            ref="https://en.wikiquote.org/wiki/Augustine_of_Hippo",
        ),
        Source(
            quote="Truth stands, falsehood does not endure.",
            source="Babylonian Talmud, Shabbat 104a",
            ref="https://www.sefaria.org/Shabbat.104a",
        ),
        Source(
            quote="Truth is everybody's truth.",
            source="Fela Kuti, Teacher Don't Teach Me Nonsense",
            ref="https://genius.com/Fela-kuti-teacher-dont-teach-me-nonsense-lyrics",
        ),
        Source(
            quote="For nothing is secret that shall not be made manifest; neither any thing hid, that shall not be known and come abroad.",
            source="Luke 8:17",
            ref="https://en.wikisource.org/wiki/Bible_(King_James)/Luke#Chapter_8",
        ),
        Source(
            quote="Truth alone triumphs; not falsehood.",
            source="Mundaka Upanishad 3.1.6",
            ref="https://en.wikisource.org/wiki/The_Ten_Principal_Upanishads/Mundaka_Upanishad",
        ),
        Source(
            quote="Satyameva Jayate. (Truth alone triumphs.)",
            source="Muṇḍaka Upaniṣad 3.1.6 (Sanskrit motto of India)",
            ref="https://en.wikisource.org/wiki/The_Ten_Principal_Upanishads/Mundaka_Upanishad",
        ),
        Source(
            quote="Truth has come and falsehood has vanished. Indeed falsehood is bound to vanish.",
            source="Qur'an 17:81",
            ref="https://en.wikisource.org/wiki/The_Holy_Qur%27an_(Maulana_Muhammad_Ali)/17._The_Israelites",
        ),
        Source(
            quote="Three things cannot long remain hidden; the sun, the moon, and the truth.",
            source="the Buddha",
            ref="https://en.wikiquote.org/wiki/Gautama_Buddha",
        ),
    )
