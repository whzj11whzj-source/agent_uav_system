
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

class FlightController : public rclcpp::Node
{
public:
    FlightController()
    : Node("flight_controller")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(
            "/cmd_vel", 10);

        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(100),
            std::bind(&FlightController::timer_callback, this));
    }

private:
    void timer_callback()
    {
        geometry_msgs::msg::Twist msg;

        msg.linear.x = 1.0;
        msg.linear.y = 0.0;
        msg.linear.z = 0.5;

        publisher_->publish(msg);

        RCLCPP_INFO(this->get_logger(), "Send velocity command");
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<FlightController>());
    rclcpp::shutdown();
    return 0;
}
