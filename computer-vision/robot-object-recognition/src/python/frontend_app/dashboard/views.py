from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import RegistrationForm, LoginForm, RegisterRobotForm
from .models import Robot, RobotRun


def login_user(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # TODO if GET, POST
    form = LoginForm()

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        # user = authenticate(request, username=username, password=password)
        # if user
        # login(request, user), return robot_run.html

        return render(request, "login.html", {"form": form})

    return render(request, "login.html", {"form": form})


def register_user(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # TODO if GET, POST
    # request.POST data passed via form
    # user = form.save() stores data into DB
    # if form.is_valid()

    form = RegistrationForm()

    return render(request, "register.html", {"form": form})


# login required
def logout_user(request):
    # TODO logout(request)

    return redirect("login") # GET ?


# login required
def show_robot_run(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # TODO robot name
    # TODO refactor
    if request.method == "GET":
        robots_runs = RobotRun.objects.filter().values()

    if request.method == "POST":
        status = request.POST.get("selected_filter")

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

    # TODO if robot, else raise does not exist
    # TODO if not.user.is_authenticated

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

    if request.method == "POST":
        # TODO validate if the name does not exist yet
        # if not redirect to the robot detail
        # else redirect to the register robot

        name = request.POST.get("name")
        motor_type = request.POST.get("motor_type")

        robot = Robot(name=name, motor_type=motor_type)
        robot.save()

        return render(request, "register_robot.html", {"form": form})


# login required
def show_robot_detail(request):
    # TODO if robot, else raise does not exist
    if request.method == "POST":
        robot_id = request.POST.get("selected_page")

        robot = Robot.objects.filter(id=robot_id).values()

        robot_payload = []

        for item in robot:
            robot_payload.append({"name": item.get("name"), "motor_type": item.get("motor_type")})

        return render(request, "robot_detail.html", {"data": robot_payload[0]})
