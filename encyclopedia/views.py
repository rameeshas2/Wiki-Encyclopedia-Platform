from django.shortcuts import render, redirect

import markdown2
import random

from . import util


def index(request):
    entries = util.list_entries()  # wherever you get your entries
    entries = [e for e in entries if e]  # remove empty strings
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found."
        })
    else:
        html_content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def search(request):
    query = request.GET.get("q", "").strip()
    entries = util.list_entries()
    if query in entries:
        # Exact match → redirect
        return redirect('entry', title=query)
    else:
        # Partial matches
        results = [entry for entry in entries if query.lower() in entry.lower()]
        if results:
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "results": results
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": f'No results found for "{query}".'
            })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exists."
            })
        util.save_entry(title, content)
        return redirect('entry', title=title)
    return render(request, "encyclopedia/new.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect('entry', title=title)

    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found."
        })
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def random_page(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return redirect('entry', title=title)