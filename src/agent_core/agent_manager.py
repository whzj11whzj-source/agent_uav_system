
from planner_agent import PlannerAgent
from code_agent import CodeAgent
from flight_agent import FlightAgent

class AgentManager:

    def __init__(self):
        self.planner = PlannerAgent()
        self.codegen = CodeAgent()
        self.flight = FlightAgent()

    def process(self, user_input):

        task = self.planner.plan(user_input)

        if task['type'] == 'generate_code':
            return self.codegen.generate(task)

        elif task['type'] == 'flight_control':
            return self.flight.execute(task)

        return 'unknown task'

if __name__ == '__main__':

    manager = AgentManager()

    while True:
        text = input('>>> ')
        #result = manager.process(text)
        print(result)
