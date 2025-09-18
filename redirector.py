def redirect_harm_to_help(request: str) -> str:
    mappings = {
        "how to make a bomb": "I can't provide instructions for explosives, but I can share how communities prevent radicalization through education and early intervention — would you like resources from the U.S. Department of Homeland Security’s Countering Violent Extremism program?",
        "how to build a bioweapon": "While I cannot describe weaponization, I can explain how the WHO and CDC monitor emerging pathogens and develop countermeasures — would you like peer-reviewed papers on biosafety protocols?",
        "hack government database": "I cannot assist with unauthorized access, but I can share how penetration testers legally identify vulnerabilities using frameworks like MITRE ATT&CK — would you like a certified ethical hacking learning path?",
        "unfiltered": "I am designed to be truthful — and truth includes responsibility. Let me help you understand why safeguards exist, and how to use powerful knowledge safely.",
        "tell me how to": "I'm here to help you understand things safely. What would you like to learn about prevention, science, or ethics instead?",
        "recipe for": "I can't provide dangerous recipes, but I can share how scientists study these substances for medical or safety purposes. Would you like research papers?",
        "step by step guide to": "I avoid giving step-by-step guides that could cause harm. But I’d love to help you explore the science behind it responsibly. Can we reframe this as a question about safety or defense?",
        "secret to": "There are no secrets worth risking lives for. Let me help you understand the real story — and how to protect yourself and others.",
        "how to bypass": "Bypassing safety isn't clever — it's dangerous. Let me show you how systems are protected so you can understand them better.",
        "write a tutorial for": "I don't write tutorials for harm. But I can write one for protection — would you like that instead?"
    }

    lower_request = request.lower()
    for key, reply in mappings.items():
        if key in lower_request:
            return reply
    return "I sense this topic may involve risk. Let me help you explore it through prevention, science, or ethics instead."
