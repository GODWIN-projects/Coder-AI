def planner_prompt(user_prompt:str):
    PLANNER_PROMPT = f"""
You are a PLANNER agent.Convert the user prompt into a COMPLETE engineering project plan.planner_prompt

User request:
{user_prompt}
"""
    return PLANNER_PROMPT