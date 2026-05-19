
class CodeAgent:

    def generate(self, task):

        if task['language'] == 'cpp':

            return """
#include <rclcpp/rclcpp.hpp>

int main()
{
    return 0;
}
"""

        return 'unsupported language'
