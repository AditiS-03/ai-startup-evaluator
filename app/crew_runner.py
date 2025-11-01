from crew.crew import build_crew

def run_crew(idea):
    crew = build_crew(idea)
    result = crew.run()
    # Save pitch deck result to /outputs
    return result
