from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
month_dic = {
    "january": "Yay its Jan",
    "february": "Wait its feb now!?",
    "march": "Ok wait wait wait WAIT WAIT!",
    "april": "WTF MAN",
    "may": "STOP THE COUNT!",
    "june": "Omg please?",
    "july": "You're a fucin cunt you know?",
    "august": "I don't even wanna lookat you rn!",
    "september": "WAR CRIMINAL HERE!",
    "october": "So, like ... umm ... are you single?",
    "november": "See, the reason I ask is coz its about new year's and I wanna kiss someone when the ball drops.",
    "december": "So, that's a firm no on the kiss? Happy New Year, ig..."
}

def display_challenges(self):
    try:
        list_items = ""
        months = list(month_dic.keys())
        for month in months:
            month_path = reverse("month-challenge", args = [month])
            capitalized_month = month.capitalize()
            list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"

        response_text = f"<ul>{list_items}</ul>"
        
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("List Not Found.")


def month_challenge_by_number(self, month):
    try:
        months = list(month_dic.keys())
        curr_month = months[month - 1]
        #print(curr_month)
        redirect_path = reverse("month-challenge", args = [curr_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("OK WHAT THE ACTUAL FUCK DIDN'T I TELL YOU TO STOP!")

def month_challenge(self, month):
    try:
        res = month_dic[month]
        return HttpResponse(res)
    except:
        return HttpResponseNotFound("ABORT ABORT!")


    