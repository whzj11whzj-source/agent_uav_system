
class PlannerAgent:

    def plan(self, text):

        text = text.lower()

        if '生成代码' in text:
            return {
                'type': 'generate_code',
                'language': 'cpp'
            }

        if '起飞' in text:
            return {
                'type': 'flight_control',
                'action': 'takeoff'
            }

        return {
            'type': 'unknown'
        }
