"""
Astrological interpretations — no API keys, fully offline.
Rich, template-driven reading generator.
"""

# ─── Sun Sign Profiles ───────────────────────────────────────────────────────

SUN_PROFILES = {
    "Aries": {
        "keyword": "The Pioneer",
        "dates": "March 21 – April 19",
        "element": "Fire", "modality": "Cardinal", "ruler": "Mars",
        "traits": ["Bold", "Courageous", "Energetic", "Impulsive", "Independent"],
        "strengths": "You lead with unmatched courage and a pioneering spirit. When others hesitate, you dive headfirst into new challenges, armed with infectious enthusiasm and a fierce desire to be first.",
        "challenges": "Impatience and impulsiveness can create unnecessary friction. Learning to slow down and consider others' perspectives will turn your natural leadership into lasting impact.",
        "love": "In love you are passionate, direct, and crave excitement. You need a partner who matches your energy, appreciates your boldness, and gives you enough freedom to remain the independent soul you are.",
        "career": "You thrive in roles where you can lead, compete, and pioneer. Entrepreneurship, athletics, military, surgery, or any fast-paced field channels your drive perfectly.",
        "symbol": "♈", "color": "#FF4136", "stone": "Diamond"
    },
    "Taurus": {
        "keyword": "The Builder",
        "dates": "April 20 – May 20",
        "element": "Earth", "modality": "Fixed", "ruler": "Venus",
        "traits": ["Reliable", "Patient", "Sensual", "Stubborn", "Devoted"],
        "strengths": "Your patience and determination are legendary. You build with care, create beauty where others see only raw material, and possess an unshakeable loyalty that makes you one of the most trusted people in any circle.",
        "challenges": "Resistance to change and a tendency toward possessiveness can hold you back. Embracing flexibility and releasing control allows your natural abundance to grow even further.",
        "love": "You love deeply, sensually, and with enduring devotion. Romance for you is about comfort, beauty, and security — candlelit dinners, physical affection, and a partner who is genuinely there for the long haul.",
        "career": "Finance, real estate, culinary arts, music, architecture, and fashion suit you perfectly. You excel whenever patience, craftsmanship, and an eye for beauty are rewarded.",
        "symbol": "♉", "color": "#2ECC40", "stone": "Emerald"
    },
    "Gemini": {
        "keyword": "The Communicator",
        "dates": "May 21 – June 20",
        "element": "Air", "modality": "Mutable", "ruler": "Mercury",
        "traits": ["Versatile", "Witty", "Curious", "Restless", "Sociable"],
        "strengths": "Your mind is a kaleidoscope — quick, adaptive, and endlessly curious. You can talk to anyone, connect disparate ideas, and communicate complex thoughts with rare clarity and wit.",
        "challenges": "Scattered energy and inconsistency can undermine deep mastery. Committing fully — to a project, a person, a purpose — will unlock the true depth hidden beneath your brilliance.",
        "love": "Mental stimulation is your greatest aphrodisiac. You need a partner who can keep up with your quick mind, laugh freely, and evolve with you as both of you change over time.",
        "career": "Journalism, writing, teaching, public relations, sales, broadcasting, and technology are natural homes for your quick mind and expressive gifts.",
        "symbol": "♊", "color": "#FFDC00", "stone": "Agate"
    },
    "Cancer": {
        "keyword": "The Nurturer",
        "dates": "June 21 – July 22",
        "element": "Water", "modality": "Cardinal", "ruler": "Moon",
        "traits": ["Intuitive", "Nurturing", "Protective", "Moody", "Tenacious"],
        "strengths": "Your emotional intelligence runs deep. You feel the unspoken, remember every meaningful detail, and create sanctuaries of warmth and belonging wherever you go. Your loyalty is unmatched.",
        "challenges": "Moodiness and a tendency to cling to the past can create unnecessary suffering. Trusting the flow of change while honoring your feelings brings tremendous healing.",
        "love": "You love with your whole heart and soul. Emotional safety is non-negotiable — you need a partner who will create a genuine home with you, and meet your deep need for closeness and belonging.",
        "career": "Nursing, psychology, childcare, culinary arts, real estate, history, and social work all align beautifully with your natural empathy and desire to nurture and protect.",
        "symbol": "♋", "color": "#7FDBFF", "stone": "Pearl"
    },
    "Leo": {
        "keyword": "The Sovereign",
        "dates": "July 23 – August 22",
        "element": "Fire", "modality": "Fixed", "ruler": "Sun",
        "traits": ["Charismatic", "Generous", "Creative", "Proud", "Loyal"],
        "strengths": "You radiate solar warmth and a natural magnetism that draws others toward you. Your creativity is grand, your generosity genuine, and your ability to inspire others is truly regal.",
        "challenges": "Pride and a need for constant validation can dim your natural light. Your truest power emerges when you lead to uplift others rather than to receive applause.",
        "love": "You love dramatically, loyally, and with grand gestures. Romance should feel like a grand stage where both partners shine. You need admiration, playfulness, and a partner who celebrates your fire.",
        "career": "Performance, leadership, entertainment, fashion, politics, and the arts are your arenas. Anywhere your natural charisma and creative vision can command a stage is where you belong.",
        "symbol": "♌", "color": "#FF851B", "stone": "Ruby"
    },
    "Virgo": {
        "keyword": "The Analyst",
        "dates": "August 23 – September 22",
        "element": "Earth", "modality": "Mutable", "ruler": "Mercury",
        "traits": ["Analytical", "Precise", "Helpful", "Critical", "Diligent"],
        "strengths": "Your mind is a finely tuned instrument. You notice what others miss, improve what others accept as flawed, and serve with a dedication that quietly elevates everything around you.",
        "challenges": "Perfectionism and self-criticism can become prisons. Embracing 'good enough' and extending to yourself the same compassion you freely give others is transformative.",
        "love": "You show love through acts of service, attention to detail, and quiet devotion. A partner who appreciates your thoughtfulness and creates a safe, clean space for your mind to rest is ideal.",
        "career": "Healthcare, editing, data analysis, research, nutrition, accounting, and engineering reward your precision, reliability, and systematic thinking.",
        "symbol": "♍", "color": "#01FF70", "stone": "Sapphire"
    },
    "Libra": {
        "keyword": "The Diplomat",
        "dates": "September 23 – October 22",
        "element": "Air", "modality": "Cardinal", "ruler": "Venus",
        "traits": ["Charming", "Fair-minded", "Social", "Indecisive", "Idealistic"],
        "strengths": "You possess a rare gift: the ability to hold multiple perspectives simultaneously and find the most elegant path between extremes. Your diplomacy, aesthetic sense, and social grace make you magnetic.",
        "challenges": "Indecision and people-pleasing can erode your sense of self. Learning to honor your own desires as loudly as you honor others' is the key to your truest harmony.",
        "love": "You were born for partnership. You thrive in relationships built on mutual respect, intellectual connection, and shared beauty. A harmonious, beautiful life shared with an equal is your deepest vision.",
        "career": "Law, diplomacy, design, architecture, counseling, fashion, HR, and the arts all benefit from your balanced judgment, refined taste, and natural gift for mediation.",
        "symbol": "♎", "color": "#F012BE", "stone": "Opal"
    },
    "Scorpio": {
        "keyword": "The Transformer",
        "dates": "October 23 – November 21",
        "element": "Water", "modality": "Fixed", "ruler": "Pluto / Mars",
        "traits": ["Intense", "Perceptive", "Passionate", "Secretive", "Resilient"],
        "strengths": "You see through surfaces to the core of things with uncanny precision. Your intensity, emotional depth, and capacity for transformation make you one of the most powerful forces in the zodiac.",
        "challenges": "Jealousy, control, and a tendency to hold grudges can exhaust both you and those around you. Channeling your depth into healing rather than vengeance unleashes your most extraordinary power.",
        "love": "You love with total, all-consuming intensity. For you, love is a complete merger of souls — nothing superficial will do. Trust is sacred, and once given, your loyalty is absolute and forever.",
        "career": "Psychology, research, surgery, finance, forensics, investigation, occult sciences, and crisis management are natural domains for your penetrating mind and fearless nature.",
        "symbol": "♏", "color": "#85144b", "stone": "Topaz"
    },
    "Sagittarius": {
        "keyword": "The Explorer",
        "dates": "November 22 – December 21",
        "element": "Fire", "modality": "Mutable", "ruler": "Jupiter",
        "traits": ["Optimistic", "Adventurous", "Philosophical", "Blunt", "Freedom-loving"],
        "strengths": "Your optimism is a superpower. You carry an unquenchable thirst for truth, adventure, and meaning that expands every room you enter. You make life feel like a grand, worthwhile journey.",
        "challenges": "Bluntness, overcommitment, and a restless refusal to be tied down can burn bridges. Learning that depth can be found in stillness as much as movement transforms your journey.",
        "love": "You need a partner who is also a best friend and fellow adventurer. Freedom is non-negotiable — love must feel expansive, intellectually stimulating, and pointed toward shared growth and exploration.",
        "career": "Travel, academia, publishing, law, philosophy, religion, tourism, coaching, and international business all channel your love of knowledge, freedom, and big-picture thinking.",
        "symbol": "♐", "color": "#3D9970", "stone": "Turquoise"
    },
    "Capricorn": {
        "keyword": "The Achiever",
        "dates": "December 22 – January 19",
        "element": "Earth", "modality": "Cardinal", "ruler": "Saturn",
        "traits": ["Ambitious", "Disciplined", "Practical", "Reserved", "Strategic"],
        "strengths": "Your discipline and strategic patience are unrivaled. You set your eyes on the summit and climb, steadily, regardless of the weather. Your accomplishments are not luck — they are the result of deep respect for time and effort.",
        "challenges": "Workaholism and emotional rigidity can create a cold distance from those you love. Learning to play, to be vulnerable, and to enjoy the climb — not just the summit — brings profound fulfillment.",
        "love": "You take love seriously and offer unwavering loyalty and practical support. A partner who is equally ambitious, stable, and emotionally mature — who builds a real life alongside you — is your match.",
        "career": "Business, finance, engineering, government, management, law, and architecture suit your ambition, patience, and desire to build something that endures across generations.",
        "symbol": "♑", "color": "#AAAAAA", "stone": "Garnet"
    },
    "Aquarius": {
        "keyword": "The Visionary",
        "dates": "January 20 – February 18",
        "element": "Air", "modality": "Fixed", "ruler": "Uranus / Saturn",
        "traits": ["Innovative", "Humanitarian", "Independent", "Eccentric", "Intellectual"],
        "strengths": "You see the world as it could be, not merely as it is. Your intellectual originality, humanitarian ideals, and willingness to break convention make you a genuine agent of positive change.",
        "challenges": "Emotional detachment and a tendency to prioritize ideas over people can create loneliness. Learning to be as present in the heart as you are in the mind brings the connection you secretly crave.",
        "love": "You need a relationship that feels like a partnership between equals and fellow revolutionaries. Intellectual freedom, mutual respect, and shared values matter far more than conventional romance.",
        "career": "Technology, social activism, science, invention, non-profits, broadcasting, and progressive politics are where your visionary thinking and commitment to humanity finds its highest expression.",
        "symbol": "♒", "color": "#0074D9", "stone": "Amethyst"
    },
    "Pisces": {
        "keyword": "The Dreamer",
        "dates": "February 19 – March 20",
        "element": "Water", "modality": "Mutable", "ruler": "Neptune / Jupiter",
        "traits": ["Compassionate", "Artistic", "Intuitive", "Escapist", "Spiritual"],
        "strengths": "You carry the wisdom of all twelve signs in your soul. Your compassion, creativity, and spiritual sensitivity allow you to perceive beauty, pain, and meaning that most people simply cannot access.",
        "challenges": "Escapism and a tendency to dissolve boundaries can leave you vulnerable to being overwhelmed or misused. Grounding your gifts in structure and healthy boundaries allows your magic to truly manifest.",
        "love": "You love with a boundless, almost otherworldly tenderness. You seek a soul-deep connection — a love that feels transcendent, poetic, and spiritually meaningful. Practicality matters less than magic.",
        "career": "Art, music, film, healing arts, spirituality, social work, poetry, and photography all channel your profound empathy, creativity, and desire to dissolve suffering into beauty.",
        "symbol": "♓", "color": "#B10DC9", "stone": "Aquamarine"
    }
}

# ─── Moon Sign Interpretations ──────────────────────────────────────────────

MOON_INTERPRETATIONS = {
    "Aries": "Your emotional world is immediate and intense — you feel first and reflect later. You need outlets for your fiery feelings and crave the freedom to act on your instincts without explanation.",
    "Taurus": "Emotional security and sensory comfort are your deepest needs. You find peace in beautiful surroundings, regular routines, and relationships that feel stable and predictable.",
    "Gemini": "Your emotions are processed through your mind. You need to talk through your feelings, and your mood shifts rapidly with your thoughts. Boredom is your greatest emotional enemy.",
    "Cancer": "Deeply sensitive and powerfully intuitive, your emotions are your compass. Home, family, and emotional safety form the bedrock of your inner world. You feel everything profoundly.",
    "Leo": "You need to feel special, seen, and celebrated to feel emotionally whole. Warmth, creativity, and the genuine admiration of those you love nourish your heart at the deepest level.",
    "Virgo": "You process emotions analytically — sometimes to a fault. Helping others soothes your anxious mind, and your emotional wellbeing is directly tied to feeling useful and in control of your environment.",
    "Libra": "Harmony and connection are your emotional oxygen. Discord and conflict are genuinely distressing to you, and you flourish when you're in balanced, beautiful, and mutually supportive relationships.",
    "Scorpio": "Your emotional depths are vast and largely invisible to the outside world. You feel intensely, guard your inner world fiercely, and need complete trust before you allow anyone close to your true heart.",
    "Sagittarius": "Freedom and optimism are your emotional anchors. You need room to explore, grow, and seek meaning. When life feels expansive and purposeful, your spirit soars effortlessly.",
    "Capricorn": "You tend to keep your emotions private, controlled, and purposeful. You feel most secure when you have clear goals and visible progress. Vulnerability takes time to trust, but when given, it's genuine.",
    "Aquarius": "You process emotions intellectually and value your independence even in your inner world. You feel most alive when contributing to something larger than yourself and connecting with like-minded souls.",
    "Pisces": "Your emotional world is vast, fluid, and deeply empathic. You absorb the feelings of those around you like a sponge and need regular solitude to cleanse your psyche and reconnect with your own feelings."
}

# ─── Rising Sign Interpretations ─────────────────────────────────────────────

RISING_INTERPRETATIONS = {
    "Aries": "You project bold confidence and an immediate, assertive energy. People instantly sense your directness and initiative — you are often the first one others turn to when action is needed.",
    "Taurus": "You carry a calm, grounded presence that others find deeply reassuring. Your appearance tends toward classic beauty and natural elegance, and you make others feel immediately at ease.",
    "Gemini": "You appear quick, articulate, and perpetually curious. Your eyes are bright and expressive, and people are drawn in by your wit and your remarkable ability to connect with virtually anyone.",
    "Cancer": "You project a warm, gentle, and nurturing energy that makes others feel immediately cared for. Your face is expressive and your presence invites trust and emotional openness.",
    "Leo": "You make an entrance. Your presence is radiant, confident, and unmistakably magnetic. People notice you before you've said a single word, and your natural warmth keeps them drawn to you.",
    "Virgo": "You project an air of quiet competence and thoughtful precision. Understated and intelligent, you give the impression of someone who notices everything and can solve any problem put before them.",
    "Libra": "You are naturally charming, elegant, and socially graceful. You make everyone around you feel special, and your refined aesthetic — in appearance, manner, and environment — is immediately apparent.",
    "Scorpio": "Your gaze is penetrating and magnetic. You project an intense, mysterious quality that both intrigues and slightly unnerves others. People sense there is much more beneath your surface than you reveal.",
    "Sagittarius": "You project infectious optimism, adventure, and philosophical openness. You appear approachable, enthusiastic, and genuinely interested in the world and the people in it.",
    "Capricorn": "You project an aura of authority, composure, and quiet competence. You appear older and more serious than your age, and people naturally treat you as someone to be respected and relied upon.",
    "Aquarius": "You project an air of uniqueness and slight otherness. Unconventional in appearance or manner, you give the impression of someone who sees the world from a fascinatingly different angle.",
    "Pisces": "You project a dreamy, ethereal, and deeply compassionate energy. Your eyes seem to hold entire oceans, and people are often drawn to your gentleness and your aura of quiet spiritual depth."
}

# ─── Element & Modality Descriptions ─────────────────────────────────────────

ELEMENT_DESC = {
    "Fire": "Fire signs (Aries, Leo, Sagittarius) are driven by passion, inspiration, and the will to act. You are energized by new beginnings, creative vision, and the thrill of possibility.",
    "Earth": "Earth signs (Taurus, Virgo, Capricorn) are grounded in the tangible and the practical. You build things that last, trust what you can measure, and find security in stability and material mastery.",
    "Air": "Air signs (Gemini, Libra, Aquarius) live primarily in the realm of ideas and communication. You are energized by connection, concepts, and the free exchange of knowledge and perspective.",
    "Water": "Water signs (Cancer, Scorpio, Pisces) navigate life through emotion, intuition, and psychic sensitivity. You are deeply empathic, attuned to subtlety, and guided by your inner knowing."
}

MODALITY_DESC = {
    "Cardinal": "Cardinal energy is initiating and action-oriented. You are a natural starter — a visionary who sets things in motion and leads others toward new directions.",
    "Fixed": "Fixed energy is sustaining and determined. You are the builder who sees things through, the reliable force that holds the center when others waver.",
    "Mutable": "Mutable energy is adaptive and flexible. You are the bridge between worlds — a natural mediator who thrives in change and brings wisdom gathered from diverse experiences."
}

# ─── Planetary Meaning Snippets ───────────────────────────────────────────────

PLANET_IN_SIGN = {
    "Mercury": {
        "Aries": "Your mind is quick and decisive — you think in flashes of insight and communicate with direct, bold precision.",
        "Taurus": "Your thinking is methodical and deliberate — you process information slowly but arrive at deeply considered, practical conclusions.",
        "Gemini": "Your mind is razor-sharp and perpetually curious — you absorb, process, and connect information faster than almost anyone.",
        "Cancer": "Your thinking is intuitively colored by emotion — memory and feeling shape how you absorb and communicate.",
        "Leo": "You think and speak with dramatic flair — your ideas are bold, creative, and expressed with commanding confidence.",
        "Virgo": "Your analytical mind is exquisitely precise — a natural editor, researcher, and problem-solver who sees every flaw.",
        "Libra": "You deliberate carefully before speaking and have a gift for diplomatic, balanced communication that bridges divides.",
        "Scorpio": "Your mind operates like a precision instrument for detection — penetrating, probing, and relentlessly searching for truth.",
        "Sagittarius": "Your thinking is expansive and philosophical — you see the big picture and communicate with contagious enthusiasm.",
        "Capricorn": "Your mind is strategic, disciplined, and goal-oriented — you communicate with authority and careful precision.",
        "Aquarius": "Your thinking is strikingly original — you make connections others miss and communicate revolutionary ideas with detached clarity.",
        "Pisces": "Your mind drifts fluidly between intuition and imagination — your thinking is poetic, psychic, and deeply empathic."
    },
    "Venus": {
        "Aries": "In love you are bold, direct, and passionate — you pursue what you desire with honest, refreshing urgency.",
        "Taurus": "You love with enduring sensuality and devotion — beauty, comfort, and physical affection are essential to your heart.",
        "Gemini": "You need intellectual spark and playful wit in love — a partner who stimulates your mind captivates you completely.",
        "Cancer": "You love with tender, nurturing devotion — emotional security and creating a true home are your heart's greatest desires.",
        "Leo": "You love with dramatic flair and royal generosity — you adore grand gestures and being adored in return.",
        "Virgo": "You express love through service and thoughtful attention to detail — devotion for you is practical and quietly profound.",
        "Libra": "Partnership is your art form — you seek beauty, harmony, and a relationship that feels both aesthetically and spiritually balanced.",
        "Scorpio": "Your love is all-consuming and intensely loyal — you give everything and need the same depth of commitment in return.",
        "Sagittarius": "Love must be an adventure — you need freedom, inspiration, and a partner who matches your enthusiasm for discovery.",
        "Capricorn": "You approach love seriously and with long-term intention — stability, loyalty, and shared ambition matter most to your heart.",
        "Aquarius": "You love as an equal and a friend — intellectual freedom and a relationship built on mutual respect and shared ideals is your ideal.",
        "Pisces": "Your love is romantic, compassionate, and nearly transcendent — you seek a soul-level connection that feels like a poem."
    },
    "Mars": {
        "Aries": "Your drive is explosive and immediate — a force of pure ambition, courage, and competitive fire.",
        "Taurus": "Your drive is slow-building but unstoppable — deliberate, patient, and relentlessly persistent.",
        "Gemini": "Your energy scatters brilliantly in multiple directions — you thrive on variety, words, and mental challenges.",
        "Cancer": "Your drive is fueled by emotion and protection — you fight fiercely for what and who you love.",
        "Leo": "Your ambition burns bright and proud — you are driven to perform, create, and lead on the grandest stage.",
        "Virgo": "Your energy is precise and efficient — you direct your effort with careful analysis and serve with disciplined dedication.",
        "Libra": "Your drive is activated by fairness and connection — you work best collaboratively and fight for what is just.",
        "Scorpio": "Your willpower is extraordinary — focused, strategic, and capable of enduring extraordinary depths to achieve your goals.",
        "Sagittarius": "Your drive is fueled by freedom and meaning — you move boldly toward ideals, adventures, and expanded horizons.",
        "Capricorn": "Your ambition is disciplined and long-sighted — you climb steadily, strategically, and with relentless determination.",
        "Aquarius": "Your drive is channeled toward innovation and revolution — you fight for ideas, communities, and a better future.",
        "Pisces": "Your energy is diffuse and spiritually oriented — you are driven by compassion, creativity, and the desire to dissolve suffering."
    }
}

# ─── Main Reading Generator ───────────────────────────────────────────────────

def generate_reading(chart_data: dict) -> dict:
    """Generate a complete, rich astrological reading from chart data."""
    if not chart_data.get("success"):
        return {}

    sun = chart_data.get("sun_sign", "")
    moon = chart_data.get("moon_sign", "")
    rising = chart_data.get("rising_sign", "")
    planets = chart_data.get("planets", {})
    name = chart_data.get("name", "")
    first_name = name.split()[0] if name else "You"

    sun_profile = SUN_PROFILES.get(sun, {})

    # Big Three summary
    big_three_summary = (
        f"{first_name}, your cosmic blueprint is written across three essential pillars. "
        f"Your {sun} Sun illuminates your core identity — the essential self you are here to express and become. "
        f"Your {moon} Moon governs your emotional landscape, your instincts, and the private world of your inner life. "
        f"Your {rising} Rising is the face you show the world — your social mask, your first impression, and the lens through which you experience life."
    )

    # Element balance
    element_counts = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
    for p_data in planets.values():
        el = p_data.get("element", "")
        if el in element_counts:
            element_counts[el] += 1
    dominant_element = max(element_counts, key=element_counts.get)

    # Modality balance
    modality_counts = {"Cardinal": 0, "Fixed": 0, "Mutable": 0}
    for p_data in planets.values():
        mod = p_data.get("modality", "")
        if mod in modality_counts:
            modality_counts[mod] += 1
    dominant_modality = max(modality_counts, key=modality_counts.get)

    # Retrograde planets
    retrogrades = [name for name, data in planets.items() if data.get("retrograde")]

    retrograde_text = ""
    if retrogrades:
        retrograde_text = (
            f"At the time of your birth, {', '.join(retrogrades[:-1]) + ' and ' + retrogrades[-1] if len(retrogrades) > 1 else retrogrades[0]} "
            f"{'were' if len(retrogrades) > 1 else 'was'} retrograde. Retrograde planets invite you to turn inward, revisit, and deepen your relationship "
            f"with the themes those planets govern before expressing them outwardly in the world."
        )

    # Mercury, Venus, Mars specific readings
    mercury_sign = planets.get("Mercury", {}).get("sign", "")
    venus_sign = planets.get("Venus", {}).get("sign", "")
    mars_sign = planets.get("Mars", {}).get("sign", "")

    mercury_reading = PLANET_IN_SIGN.get("Mercury", {}).get(mercury_sign, "")
    venus_reading = PLANET_IN_SIGN.get("Venus", {}).get(venus_sign, "")
    mars_reading = PLANET_IN_SIGN.get("Mars", {}).get(mars_sign, "")

    # Jupiter & Saturn
    jupiter_sign = planets.get("Jupiter", {}).get("sign", "")
    saturn_sign = planets.get("Saturn", {}).get("sign", "")

    jupiter_text = (
        f"Jupiter in {jupiter_sign} expands your vision through the lens of {jupiter_sign}'s energy, "
        f"bringing luck, wisdom, and abundance to the areas of life this sign governs most powerfully."
        if jupiter_sign else ""
    )
    saturn_text = (
        f"Saturn in {saturn_sign} places your greatest lessons, disciplines, and long-term mastery in "
        f"the domain of {saturn_sign} — challenging you to earn, through patience and integrity, what you most need to grow."
        if saturn_sign else ""
    )

    # Ascendant house ruler
    houses = chart_data.get("houses", {})

    # Life path summary
    life_path = (
        f"The interplay of your {sun} Sun, {moon} Moon, and {rising} Rising creates a uniquely layered personality. "
        f"The dominant {dominant_element} element in your chart colors your approach with "
        f"{dominant_element.lower()} qualities — " +
        {
            "Fire": "passion, spontaneity, and visionary drive",
            "Earth": "groundedness, practicality, and steadfast reliability",
            "Air": "intellectual curiosity, communicative brilliance, and social adaptability",
            "Water": "emotional depth, intuitive wisdom, and empathic sensitivity"
        }.get(dominant_element, "diverse energies") +
        f". Your {dominant_modality} modality gives you a natural inclination to " +
        {
            "Cardinal": "initiate, lead, and set new directions in motion",
            "Fixed": "commit, persist, and see every endeavor through to its completion",
            "Mutable": "adapt, mediate, and bring synthesizing wisdom to every situation"
        }.get(dominant_modality, "engage with life in your own way") + "."
    )

    return {
        "name": name,
        "first_name": first_name,
        "sun_sign": sun,
        "moon_sign": moon,
        "rising_sign": rising,
        "sun_profile": sun_profile,
        "sun_traits": sun_profile.get("traits", []),
        "sun_keyword": sun_profile.get("keyword", ""),
        "sun_dates": sun_profile.get("dates", ""),
        "sun_ruler": sun_profile.get("ruler", ""),
        "sun_element": sun_profile.get("element", ""),
        "sun_modality": sun_profile.get("modality", ""),
        "sun_color": sun_profile.get("color", "#8B5CF6"),
        "sun_stone": sun_profile.get("stone", ""),
        "sun_symbol": sun_profile.get("symbol", ""),
        "sun_strengths": sun_profile.get("strengths", ""),
        "sun_challenges": sun_profile.get("challenges", ""),
        "sun_love": sun_profile.get("love", ""),
        "sun_career": sun_profile.get("career", ""),
        "moon_interpretation": MOON_INTERPRETATIONS.get(moon, ""),
        "rising_interpretation": RISING_INTERPRETATIONS.get(rising, ""),
        "big_three_summary": big_three_summary,
        "element_balance": element_counts,
        "dominant_element": dominant_element,
        "dominant_element_desc": ELEMENT_DESC.get(dominant_element, ""),
        "dominant_modality": dominant_modality,
        "dominant_modality_desc": MODALITY_DESC.get(dominant_modality, ""),
        "retrograde_text": retrograde_text,
        "mercury_sign": mercury_sign,
        "venus_sign": venus_sign,
        "mars_sign": mars_sign,
        "mercury_reading": mercury_reading,
        "venus_reading": venus_reading,
        "mars_reading": mars_reading,
        "jupiter_sign": jupiter_sign,
        "saturn_sign": saturn_sign,
        "jupiter_text": jupiter_text,
        "saturn_text": saturn_text,
        "life_path": life_path,
        "planets": planets,
        "houses": houses,
    }
