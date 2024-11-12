from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': "eat no meat!",
    'february': "walk for 20 mins",
    'march': "learn django for 20 mins",
    'april': "eat no meat2!",
    'may': "walk for 20 mins2",
    'june': "learn django for 20 mins2",
    'july': "eat no meat3!",
    'august': "walk for 20 mins3",
    'september': "learn django for 20 mins3",
    'october': "eat no meat4!",
    'november': "walk for 20 mins4",
    'december': None,
}
# Create your views here.

def monthly_challenge_by_number (request, month):
    months = list(monthly_challenges.keys())
    month_to_forward = months[month-1]
    redirect_path = reverse("month-challenge", args=[month_to_forward])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        return render(request, "challenges/challenge.html", {
            "month": month,
            "month_challenge": monthly_challenges[month]
        }) 
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)


def all_months(request):
    return render(request, "challenges/index.html", {'months': monthly_challenges.keys()})
