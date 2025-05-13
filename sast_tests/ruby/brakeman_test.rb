# dynamic eval
eval(params[:evil])

# command injection
system("ls #{params[:path]}")
