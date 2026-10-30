from models import Event

events_db = {
    "hackathon": Event(
        id="hackathon",
        name="Hackathon",
        description="A 24-hour coding marathon to solve real-world problems.",
        min_year=2,
        max_year=4,
        allowed_branches=["CSE", "IT", "AI&DS", "ECE"],
        min_team_size=2,
        max_team_size=4,
        max_teams=20,
        fee=500.0,
        date="2026-10-15",
        time="10:00 AM",
        venue="Main Auditorium",
        rules=["Bring your own laptops", "Teams must submit code before deadline"]
    ),
    "coding-contest": Event(
        id="coding-contest",
        name="Coding Contest",
        description="Competitive programming challenge.",
        min_year=1,
        max_year=4,
        allowed_branches=["CSE", "IT", "AI&DS", "ECE", "EEE", "MECH", "CIVIL"],
        min_team_size=1,
        max_team_size=1,
        max_teams=100,
        fee=100.0,
        date="2026-10-16",
        time="09:00 AM",
        venue="Lab Complex",
        rules=["No internet allowed during contest", "Use C, C++, Java, or Python"]
    ),
    "robotics-challenge": Event(
        id="robotics-challenge",
        name="Robotics Challenge",
        description="Build and race your own line-following or sumo robot.",
        min_year=2,
        max_year=4,
        allowed_branches=["ECE", "EEE", "MECH", "CSE", "AI&DS"],
        min_team_size=3,
        max_team_size=5,
        max_teams=15,
        fee=750.0,
        date="2026-10-16",
        time="02:00 PM",
        venue="Open Ground",
        rules=["Robots must meet size restrictions", "Autonomous operation only"]
    ),
    "ai-quiz": Event(
        id="ai-quiz",
        name="AI Quiz",
        description="Test your knowledge on Artificial Intelligence and Machine Learning.",
        min_year=1,
        max_year=4,
        allowed_branches=["CSE", "IT", "AI&DS", "ECE"],
        min_team_size=1,
        max_team_size=2,
        max_teams=50,
        fee=150.0,
        date="2026-10-17",
        time="11:00 AM",
        venue="Seminar Hall",
        rules=["No mobile phones allowed", "Multiple choice and rapid fire rounds"]
    )
}
