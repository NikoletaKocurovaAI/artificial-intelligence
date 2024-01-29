from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .forms import RegistrationForm, LoginForm, RegisterRobotForm, RobotDetailForm
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
    """
    This ..

    :param request:
    :return:
    :raises
    """
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
    # TODO if not.user.is_authenticated

    if request.method == "GET":
        robots_runs = RobotRun.objects.filter().values()
        page_number = request.GET.get('page')

    if request.method == "POST":
        robots_runs = RobotRun.get_filtered_robot_runs(RobotRun(), status=request.POST.get("selected_filter"))
        page_number = 1

    return render(request, "robot_run.html", {"data_robots_runs": RobotRun.add_robot_name(RobotRun(), robots_runs),
                                              "data_robots_names": Robot.objects.filter().values(),
                                              "data_robots_runs_statuses": RobotRun.get_robots_runs_statuses(RobotRun()),
                                              "data_robots_runs2": Paginator(robots_runs, per_page=3).get_page(page_number)})


@login_required
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
        Robot(name=request.POST.get("name"), motor_type=request.POST.get("motor_type")).save()

        return render(request, "register_robot.html", {"form": form})


@login_required
def show_robot_detail(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    if request.method == "POST":
        robot_detail_id = request.POST.get("selected_page")
        robot_to_delete = request.POST.get("robot_detail_robot_name")
        robot_next_run = request.POST.get("robot_detail_next_run_datetime")
        robot_id_next_run = request.POST.get("robot_detail_robot_id_for_next_run")

        if robot_detail_id:
            return render(request, "robot_detail.html", {"data": Robot.get_by_id(Robot(), robot_detail_id),
                                                         "form": RobotDetailForm()})

        if robot_to_delete:
            Robot.objects.filter(name=robot_to_delete).delete()

        if robot_next_run:
            robot = Robot.objects.get(id=int(robot_id_next_run))
            robot.next_run = robot_next_run
            robot.save()

        return redirect("robot-run")
