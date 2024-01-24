from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import RegistrationForm, LoginForm, RegisterRobotForm
from .models import Robot, RobotRun


def register_user(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    if request.method == "GET":
        return render(request, "register.html", {"form": RegistrationForm()})

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, "registration/login.html", {"form": LoginForm()})
        else:
            return render(request, "register.html", {"form": RegistrationForm()})


@login_required
def logout_user(request):
    logout(request)

    return redirect("login")


@login_required
def show_robot_run(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # TODO robot name
    # TODO if robot, else raise does not exist
    # TODO if not.user.is_authenticated
    if request.method == "GET":
        robots_runs = RobotRun.objects.filter().values()

    if request.method == "POST":
        status = request.POST.get("selected_filter")

        robots_runs = RobotRun.get_filtered_robot_runs(RobotRun(), status)

    robots = Robot.objects.filter().values()

    robots_runs_statuses = RobotRun.get_robots_runs_statuses(RobotRun())

    return render(request, "robot_run.html", {"data_robots_runs": robots_runs,
                                              "data_robots_names": robots,
                                              "data_robots_runs_statuses": robots_runs_statuses})


#@login_required
def register_robot(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    form = RegisterRobotForm()

    if request.method == "GET":
        return render(request, "register_robot.html", {"form": form})

    if request.method == "POST":
        name = request.POST.get("name")
        motor_type = request.POST.get("motor_type")

        robot = Robot(name=name, motor_type=motor_type)
        robot.save()

        return render(request, "register_robot.html", {"form": form})


@login_required
def show_robot_detail(request):
    # TODO if robot, else raise does not exist
    if request.method == "POST":
        robot_id = request.POST.get("selected_page")

        # redirect from robot-run to robot-detail
        if robot_id:
            robot = Robot.objects.filter(id=robot_id).values()

            robot_payload = []

            for item in robot:
                robot_payload.append({"name": item.get("name"), "motor_type": item.get("motor_type")})

            return render(request, "robot_detail.html", {"data": robot_payload[0]})
        # redirect from robot-detail to robot run
        else:
            name = request.POST.get("robot_name")

            Robot.objects.filter(name=name).delete()

            return redirect("robot-run")
