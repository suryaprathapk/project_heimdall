from django.shortcuts import render

# Create your views here.
if request.method == 'POST' and 'run_script' in request.POST:
    # import function to run
    from path_to_script import function_to_run

    # call function
    function_to_run()

    # return user to required page
    return HttpResponseRedirect(reverse(app_name:view_name)
