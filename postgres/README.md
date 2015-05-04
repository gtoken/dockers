For boot2docker on MAC, run `$(boot2docker shellinit 2> /dev/null)`
Also put `$(boot2docker shellinit 2> /dev/null)` the bottom of your `~/.bash_profile`

docker run --name gtoken-postgres [-e POSTGRES_PASSWORD=mysecretpassword] -d postgres