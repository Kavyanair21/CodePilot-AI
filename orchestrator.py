from planner import ai_plan, plan_task

from agent import (
    explain_agent,
    bug_agent,
    optimization_agent,
    complexity_agent,
    security_agent,
    fix_agent
)
def orchestrate(task, code):

    from planner import ai_plan

    plan = ai_plan(task)

    report = {}

    for step in plan:

        if step == "explain":
            report["Explanation"] = explain_agent(code)

        elif step == "bugs":
            report["Bug Detection"] = bug_agent(code)

        elif step == "optimize":
            report["Optimization"] = optimization_agent(code)

        elif step == "complexity":
            report["Complexity"] = complexity_agent(code)

        elif step == "security":
            report["Security"] = security_agent(code)

        elif step == "fix":
            report["Fixed Code"] = fix_agent(code)

    return report
    try:
        plan = ai_plan(task)
    except Exception:
        plan = plan_task(task)