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
    # TODO refactor
    # TODO if robot, else raise does not exist
    # TODO if not.user.is_authenticated
    if request.method == "GET":
        robots_runs = RobotRun.objects.filter().values()

    if request.method == "POST":
        status = request.POST.get("selected_filter")

        if status == "all":
            robots_runs = RobotRun.objects.filter().values()
        else:
            robots_runs = RobotRun.objects.filter(status=status).values()

    robots = Robot.objects.filter().values()

    robots_runs_statuses = RobotRun.objects.filter().values('status')

    all_robots_runs_statuses = []

    for item in robots_runs_statuses:
        all_robots_runs_statuses.append(item.get("status"))

    distinct_robots_runs_statuses = list(set(all_robots_runs_statuses))

    postprocessed_robots_runs_statuses = []

    for item in distinct_robots_runs_statuses:
        postprocessed_robots_runs_statuses.append({"status": item})

    postprocessed_robots_runs_statuses.append({"status": "all"})

    return render(request, "robot_run.html", {"data_robots_runs": robots_runs,
                                              "data_robots_names": robots,
                                              "data_robots_runs_statuses": postprocessed_robots_runs_statuses})


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

    # TODO if robot, else raise does not exist
    if request.method == "POST":
        # TODO validate if the name does not exist yet
        # if not redirect to the robot detail
        # else redirect to the register robot

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
        else:
            name = request.POST.get("robot_name")
            # TODO: delete

            return redirect("robot-run")
